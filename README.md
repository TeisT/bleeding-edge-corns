# Bleeding Edge Corns – Website

Statische Website (9 Seitentypen, 11 HTML-Seiten), umgesetzt nach dem Design-Handoff
(`~/Downloads/design_handoff_bleeding_edge_corns`). Ersetzt https://www.torben-teismann.de/bloodbook/.

## Build

Nur Python 3 (Standardbibliothek), kein Node, keine Abhängigkeiten:

```bash
python3 build.py
```

Standard ist der **Teststand**: alle Seiten mit `noindex` und `robots.txt` „Disallow“, damit nichts bei Google landet.
Für die echte Website `python3 build.py --live` verwenden (bricht ab, solange Nachzuchten-Fotos fehlen).

Nachzuchten-Fotos lokal ablegen: `python3 build.py --fotos` (lädt das erste Foto je Tier von MorphMarket nach
`src/img/nachzuchten/<ID>.jpg`, verkleinert auf 1200 px, löscht Fotos nicht mehr angebotener Tiere). Passiert bei `--import` automatisch.

**Zweisprachig:** Deutsch unter `/`, Englisch unter `/en/` mit englischen Pfaden (`/en/projects/`, `/en/hatchlings/`,
`/en/corn-snake/`, `/en/contact/`, `/en/imprint/`, `/en/privacy/`). Der DE/EN-Schalter verlinkt jeweils dieselbe Seite.

Ergebnis liegt in `dist/` und wird komplett hochgeladen. Alle Links sind relativ, die Seite läuft also
auch in einem Unterordner (z. B. `/bloodbook/`). Saubere URLs über Ordner: `/projekte/`, `/nachzuchten/` …

Lokal ansehen (mit PHP, damit das Formular antwortet):

```bash
/Applications/MAMP/bin/php/php8.3.28/bin/php -S 127.0.0.1:8471 -t dist
```

## Struktur

| Pfad | Inhalt |
|---|---|
| `content_en.py` | Englische Texte, gleiche Struktur wie `content.py` (Bilder, Slugs, Galerien werden aus `content.py` übernommen). Englisch orientiert sich an der Cornnector-Anleitung. |
| `content.py` | **Alle Texte** der Website, nach Seiten sortiert (inkl. Überschriften, Buttons, Formular- und Fehlermeldungen, Seitentitel). Schreibweisen oben in der Datei erklärt. |
| `data/nachzuchten.csv` | Nachzuchten aus MorphMarket. Neuen Export übernehmen mit `python3 build.py --import ~/Downloads/<export>.csv`. Dabei bleiben nur die benötigten Spalten erhalten (keine Preise, Aufrufzahlen oder privaten Notizen, weil das Repository öffentlich ist). Nur aktive, öffentliche „For Sale“-Inserate werden gezeigt, „Blood“ wird zu „Diffused“, IDs werden auf 3 Stellen aufgefüllt (`NZ-2026-39` → `NZ-2026-039`). |
| `data/galerie.csv` | Galerie der Startseite: `Datei;Bildunterschrift;Kategorie` (mehrere Kategorien durch Komma getrennt, ein Foto erscheint dann bei jedem dieser Filter), Reihenfolge = Reihenfolge auf der Seite. Fotos liegen in `src/img/galerie/`, Bildgrößen liest der Build selbst aus. Lässt sich in Excel/Numbers bearbeiten (als CSV speichern). |
| `build.py` | Seiten-Templates und Bausteine (Header, Footer, Kontakt-Teaser, Slider …) |
| `src/assets/style.css` | gesamtes CSS (Breakpoints Mobil < 640, Tablet 640–1023, Desktop ≥ 1024) |
| `src/assets/main.js` | Header-Scrollzustand, Burger-Menü, Reveal, Slider, Galerie-Filter, Akkordeons, Formular, Scrollspy |
| `src/assets/fonts.css`, `src/fonts/` | Roboto lokal (kein Google-Fonts-Aufruf) |
| `src/icons/` | Lucide-Icons (v0.460.0), werden beim Build inline eingesetzt |
| `src/img/` | Bilder (Logo verkleinert, Über-uns als JPG) |
| `src/php/senden.php` | Formularversand → `dist/kontakt/senden.php` |

## GitHub und Teststand

Repository: https://github.com/TeisT/bleeding-edge-corns (öffentlich).
Bei jedem Push auf `main` baut GitHub Actions (`.github/workflows/pages.yml`) die Seite und veröffentlicht sie unter
https://teist.github.io/bleeding-edge-corns/. Das PHP-Formular funktioniert dort nicht (GitHub Pages ist rein statisch).
`dist/` wird nicht eingecheckt.

## Abweichungen vom Design (bewusst)

- **Galerie Startseite:** im Design nur Platzhalter. Jetzt echte Fotos (4 von der alten Seite + Projektfotos),
  Breite aus dem Seitenverhältnis. Filter ohne Fotos (z. Z. „Andere Tiere“) werden ausgeblendet. Unter den Fotos steht nur die Bildunterschrift (ohne Kategorie).
  Liste in `data/galerie.csv`.
- **Schriften lokal:** Abschnitt „Google Fonts“ in der Datenschutzerklärung entfernt, folgende Abschnitte neu nummeriert.
- **Kontaktdaten** (E-Mail, MorphMarket) sind auf der Kontaktseite klickbar.
- **Formular** schickt per `fetch` an `kontakt/senden.php` (PHP `mail()`, Honeypot gegen Spam). Fehler beim
  Versand zeigt einen Hinweis unter dem Button.

## Offene Punkte

- **E-Mail:** Adressen stehen auf `@bleeding-edge-corns.com` (Domain wird noch registriert, Website später auf www.bleeding-edge-corns.com).
- Prüfen, ob `mail()` auf dem Server funktioniert (sonst SMTP/Formular-Dienst).
- Impressum/Datenschutz: Platzhalter (Max Mustermann, Hosting-Anbieter) ersetzen – **in `content.py` und `content_en.py`** – und rechtlich prüfen lassen.
- Social-Links (`SOCIALS` in `content.py`) stehen auf `#`.
- App-Screenshots (1179 × 2556): Pfade in `APP_FEATURES[*].screenshot` und `APP_SCREENSHOT_HOME` eintragen.
- Bildunterschriften der Projekt-Galerien (dritter Wert in `gallery`, sonst Projekttitel).
- Nachzuchten-Fotos einmal mit `python3 build.py --fotos` laden (Datenschutz Abschnitt 6 ist schon auf lokale Fotos umgestellt).
- Galerie Startseite: Fotos und Filter final zuordnen (`data/galerie.csv`).
