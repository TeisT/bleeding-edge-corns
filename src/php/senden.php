<?php
// Kontaktformular-Versand (wird nach dist/kontakt/senden.php kopiert).
// Erwartet POST von kontakt/index.html (fetch, FormData), antwortet mit JSON {ok: bool}.
// Voraussetzung: PHP mit funktionierendem mail() auf dem Webserver. Empfänger/Absender unten anpassen.

declare(strict_types=1);

const EMPFAENGER = 'kontakt@bleeding-edge-corns.de';
// Absender muss zur Domain des Servers passen, sonst landen Mails im Spam.
const ABSENDER = 'website@bleeding-edge-corns.de';
const THEMEN = ['Nachzucht', 'Projekte', 'Haltung', 'Sonstiges'];

header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

function antwort(int $status, bool $ok, string $fehler = ''): void
{
    http_response_code($status);
    echo json_encode($fehler === '' ? ['ok' => $ok] : ['ok' => $ok, 'fehler' => $fehler]);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    antwort(405, false, 'method');
}

// Honeypot: Bots füllen das versteckte Feld aus → so tun, als sei alles gut.
if (trim((string)($_POST['website'] ?? '')) !== '') {
    antwort(200, true);
}

$feld = static fn(string $k, int $max): string => mb_substr(trim((string)($_POST[$k] ?? '')), 0, $max);
// Zeilenumbrüche aus Einzeilern entfernen (Header-Injection)
$einzeilig = static fn(string $s): string => trim(preg_replace('/[\r\n]+/', ' ', $s) ?? '');

$name    = $einzeilig($feld('name', 200));
$email   = $einzeilig($feld('email', 200));
$thema   = $einzeilig($feld('thema', 40));
$tier    = $einzeilig($feld('tier', 40));
$msg     = $feld('msg', 10000);
$consent = ($_POST['consent'] ?? '') === '1';

if ($name === '' || $msg === '' || !$consent || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    antwort(422, false, 'validierung');
}
if (!in_array($thema, THEMEN, true)) {
    $thema = 'Sonstiges';
}

$betreff = 'Website-Anfrage: ' . $thema . ($tier !== '' ? ' (' . $tier . ')' : '');
$text = "Neue Nachricht über das Kontaktformular\n\n"
      . "Thema:   {$thema}\n"
      . ($tier !== '' ? "Tier-ID: {$tier}\n" : '')
      . "Name:    {$name}\n"
      . "E-Mail:  {$email}\n\n"
      . "Nachricht:\n{$msg}\n";

$header = [
    'From' => 'Bleeding Edge Corns Website <' . ABSENDER . '>',
    'Reply-To' => $email,
    'Content-Type' => 'text/plain; charset=UTF-8',
    'Content-Transfer-Encoding' => '8bit',
    'MIME-Version' => '1.0',
];

$ok = mail(EMPFAENGER, '=?UTF-8?B?' . base64_encode($betreff) . '?=', $text, $header);
antwort($ok ? 200 : 500, $ok, $ok ? '' : 'versand');
