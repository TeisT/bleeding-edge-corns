# Inhalte der Website (Texte 1:1 aus den Logikblöcken der Design-Dateien).
# Mini-Markdown: "**fett**" in Titeln/Texten, in langen Texten zusätzlich
# "## " (Zwischenüberschrift), "#### " (kleine Überschrift), "- " (Liste), "> " (Hinweisbox).

MORPHMARKET_SHOP = 'https://www.morphmarket.com/stores/andreasp/'
EMAIL = 'kontakt@bleeding-edge-corns.de'

SOCIALS = [
    # (Icon, Bezeichnung, URL) – URLs noch offen
    ('instagram', 'Instagram', '#'),
    ('facebook', 'Facebook', '#'),
    ('youtube', 'YouTube', '#'),
]

NAV = [
    # (Schlüssel, Label, Pfad)
    ('projekte', 'Projekte', 'projekte/'),
    ('nachzuchten', 'Nachzuchten', 'nachzuchten/'),
    ('kornnatter', 'Kornnatter', 'kornnatter/'),
    ('app', 'App', 'app/'),
    ('kontakt', 'Kontakt', 'kontakt/'),
]

# ---------------------------------------------------------------- Projekte
PROJECTS = [
    {
        'slug': 'hypo-diffused-high-pieds',
        'title': 'Hypo Diffused High Pieds',
        'title_md': 'Hypo Diffused **High Pieds**',
        'teaser': 'Kontrastarme Tiere mit hohem Weißanteil an den Flanken und leuchtendem Rot.',
        'img_start': 'img/slots/start-projekt-1.webp',
        'img_list': 'img/slots/projekte-1.webp',
        'list_lead': 'Unser Schwerpunkt liegt auf der Entwicklung hochwertiger Hypo Diffused High Pied Kornnattern.',
        'list_paras': ['Dabei stehen nicht nur außergewöhnliche Tiere im Mittelpunkt, sondern vor allem Gesundheit, Qualität und eine nachvollziehbare Genetik.'],
        'genes': ['Hypo', 'Diffused', 'Pied Sided', 'Charcoal'],
        'goal_label': 'Zuchtziel',
        'goal': 'Die intensive rote Grundfarbe der Diffused-Linie mit einem möglichst hohen Weißanteil der Pied-Sided-Zeichnung kombinieren.',
        'detail_lead': 'Unser Ziel ist es, Kornnattern zu entwickeln, die eine kräftige rote Färbung mit einem möglichst hohen Weißanteil der Pied-Sided-Zeichnung verbinden.',
        'detail_body': [
            'Besonders wichtig sind uns dabei klare Kontraste, harmonische Zeichnungen und eine gleichbleibend hohe Qualität über mehrere Generationen.',
            'Jede Verpaarung wird sorgfältig geplant und dokumentiert. Dabei beobachten wir nicht nur die sichtbaren Merkmale, sondern auch die genetischen Eigenschaften der Elterntiere. So entstehen Nachzuchten mit nachvollziehbarer Abstammung und einer möglichst stabilen Vererbung. Für uns bedeutet erfolgreiche Zucht nicht, möglichst viele Tiere hervorzubringen, sondern jede Generation gezielt weiterzuentwickeln.',
        ],
        # (Datei, Breite bei 900px Höhe, Bildunterschrift – offen, aktuell Projekttitel)
        'gallery': [('pied-1.jpg', 1565, ''), ('pied-2.jpg', 1173, ''), ('pied-3.jpg', 1522, ''), ('pied-4.jpg', 1170, ''), ('pied-5.jpg', 1170, '')],
    },
    {
        'slug': 'diffused-motley-striped-pieds',
        'title': 'Diffused Motley & Striped Pieds',
        'title_md': 'Diffused **Motley & Striped Pieds**',
        'teaser': 'Diffused mit Motley- und Stripe-Zeichnung auf Pied-Sided-Basis.',
        'img_start': 'img/slots/start-projekt-2.webp',
        'img_list': 'img/slots/projekte-2.webp',
        'list_lead': 'In diesem Projekt verbinden wir unsere High-Pied-Linien mit den Zeichnungsmerkmalen Motley und Striped.',
        'list_paras': [],
        'genes': ['Diffused', 'Pied Sided', 'Charcoal', 'Motley', 'Striped'],
        'goal_label': 'Zuchtziel',
        'goal': 'Unterschiedliche Muster mit intensiven Farben und hohem Weißanteil kombinieren und so neue, charakterstarke Linien aufbauen.',
        'detail_lead': 'Durch die Kombination der Gene Motley und Striped möchten wir Tiere entwickeln, die nicht nur durch ihre Farben, sondern auch durch ihre außergewöhnlichen Zeichnungen überzeugen.',
        'detail_body': [
            '## Die offene Frage dieses Projekts',
            'Ein besonderer Schwerpunkt dieses Projekts liegt auf einer Beobachtung, die uns bereits seit 2011 beschäftigt. Während sich die gewünschte Genetik zuverlässig vererben lässt, scheint die Ausprägung der Pied-Sided-Zeichnung in Kombination mit Motley oder Striped häufig deutlich schwächer auszufallen als bei klassischen Pieds.',
            'Ob diese Zeichnungsgene die Ausbildung der weißen Seitenbereiche tatsächlich beeinflussen oder lediglich andere genetische Faktoren dafür verantwortlich sind, ist bislang nicht eindeutig geklärt. Langfristig möchten wir besser verstehen, wie sich diese Gene gegenseitig beeinflussen und ob sich trotz Motley oder Striped stabile High-Pied-Linien entwickeln lassen.',
        ],
        'gallery': [('pied-motley-1.jpg', 1170, ''), ('pied-motley-2.jpg', 867, ''), ('pied-motley-3.jpg', 1441, ''), ('pied-motley-4.jpg', 1089, ''), ('pied-motley-5.jpg', 1170, ''), ('pied-motley-6.jpg', 1235, ''), ('pied-motley-7.jpg', 1075, '')],
    },
    {
        'slug': 'vanishing-motley-striped',
        'title': 'Vanishing Motley & Striped',
        'title_md': '**Vanishing** Motley & Striped',
        'teaser': 'Eine Zeichnung, die sich fast vollständig auflöst.',
        'img_start': 'img/slots/start-projekt-3.webp',
        'img_list': 'img/slots/projekte-3.webp',
        'list_lead': 'Aus einem einzelnen Jungtier entstand ein Projekt, das ursprünglich gar nicht geplant war.',
        'list_paras': ['Eine außergewöhnliche Veränderung der Zeichnung weckte sofort unsere Aufmerksamkeit. Seitdem verfolgen wir die Entwicklung dieses Tieres mit besonderem Interesse und möchten herausfinden, ob sich hinter diesem Merkmal eine neue genetische Besonderheit verbirgt.'],
        'genes': ['Motley', 'Striped', 'Vanishing (ungeklärt)'],
        'goal_label': 'Offene Frage',
        'goal': 'Lässt sich das Merkmal vererben? Dann könnte daraus eine völlig neue Zuchtlinie entstehen.',
        'detail_lead': '',
        'detail_body': [
            'Manche Projekte entstehen nicht durch Planung, sondern durch Zufall. In einem Gelege fiel uns ein Jungtier auf, dessen Zeichnung sich deutlich von allen Geschwistern unterschied. Mit jeder Häutung verändert sich das Erscheinungsbild weiter, sodass die Zeichnung zunehmend verschwindet und das Tier immer einzigartiger wirkt.',
            'Ob es sich dabei um eine neue genetische Mutation, eine seltene Kombination vorhandener Gene oder lediglich um eine außergewöhnliche Einzelerscheinung handelt, lässt sich derzeit noch nicht sicher beurteilen. Genau das macht dieses Projekt so spannend. Wir dokumentieren die Entwicklung sorgfältig und werden das Tier in den kommenden Jahren weiter beobachten. Sollte sich das Merkmal vererben lassen, könnte daraus eine völlig neue Zuchtlinie entstehen.',
        ],
        'gallery': [('vanish-1.jpg', 921, ''), ('vanish-2.jpg', 1486, ''), ('vanish-3.jpg', 1322, '')],
    },
]

# ---------------------------------------------------------------- Startseite
TRUST = [
    ('egg', 'Eigene Zuchten', 'Alle Tiere schlüpfen bei uns in Bielefeld.'),
    ('git-branch', 'Dokumentierte Abstammung', 'Über unsere eigene App genau nachvollziehbar.'),
    ('store', 'Store auf MorphMarket', 'Alle verfügbaren Tiere mit Genetik und Preisen.'),
    ('map-pin', 'Übergabe in Bielefeld & Hamm', 'Persönlich vor Ort oder auf der Terraristika Hamm.'),
]

GALLERY_CATS = ['Alle', 'Diffused', 'Charcoal', 'Motley & Striped', 'Andere Tiere']
# Galerie Startseite: (Datei in img/galerie/, Breite, Höhe, Label, Kategorie).
# Die ersten vier stammen aus dem Design, der Rest aus den Projekt-Galerien
# (Label = Projekttitel). Kategorien ohne Fotos werden als Filter ausgeblendet.
HOME_GALLERY = [
    ('start-projekt-detail-1.jpg', 1200, 1200, 'Hypo Diffused Motley-x-Striped het Charcoal', 'Diffused'),
    ('start-vanish-projekte.jpg', 1211, 902, 'Hypo Diffused Motley-x-Striped', 'Charcoal'),
    ('start-pied-projekte.jpg', 1211, 902, 'Striped Pied', 'Motley & Striped'),
    ('pied-1.jpg', 1565, 900, 'Hypo Diffused High Pied', 'Diffused'),
    ('start-motley-projekte.jpg', 1211, 902, 'Motley Pied', 'Motley & Striped'),
    ('pied-3.jpg', 1522, 900, 'Hypo Diffused High Pied', 'Diffused'),
    ('pied-motley-3.jpg', 1441, 900, 'Diffused Motley & Striped Pied', 'Motley & Striped'),
    ('vanish-2.jpg', 1486, 900, 'Vanishing Motley & Striped', 'Motley & Striped'),
    ('pied-2.jpg', 1173, 900, 'Hypo Diffused High Pied', 'Diffused'),
    ('pied-motley-6.jpg', 1235, 900, 'Diffused Motley & Striped Pied', 'Motley & Striped'),
]

APP_POINTS = [
    ('layout-dashboard', 'Hub', 'Alle Tiere, Gelege und Termine auf einen Blick.'),
    ('library', 'Collection', 'Jedes Tier mit Fotos, Abstammung und genauer Genetik.'),
    ('git-fork', 'Lineage', 'Die Abstammung über Generationen zurückverfolgen.'),
    ('search', 'Filter & Suche', 'Tiere gezielt nach Geschlecht, Genetik, Alter oder Tags finden.'),
]

# ---------------------------------------------------------------- Nachzuchten
STEPS = [
    ('search', 'Tier auf MorphMarket aussuchen', 'Alle verfügbaren Tiere mit Fotos, Genetik und Preis.'),
    ('send', 'Anfrage senden', 'Direkt über MorphMarket oder unser Kontaktformular.'),
    ('calendar-check', 'Termin vereinbaren', 'Wir stimmen gemeinsam einen passenden Übergabetermin ab.'),
    ('handshake', 'Abholung in Bielefeld oder Übergabe auf der Terraristika Hamm', 'Persönlich – inklusive Futterhistorie und Abstammung.'),
]

FAQ = [
    ('Alter bei Abgabe', 'Wir geben unsere Tiere erst ab, wenn sie mindestens fünf Mahlzeiten selbstständig gefressen haben – in der Regel mit 8 bis 10 Wochen.'),
    ('Futter bei Übergabe', 'Du erfährst genau, was und wann zuletzt gefüttert wurde. Außerdem geben wir dir mit, wie oft sich dein Tier bereits gehäutet hat.'),
    ('Versand', 'Für private Züchter ist der Tierversand in Deutschland kaum noch möglich – dafür wird inzwischen ein Gewerbe mit Tierbezug vorausgesetzt. Wenn du den Transport über einen entsprechenden Anbieter organisierst, unterstützen wir dich gerne: Heatpacks und Styroporboxen haben wir vorrätig. Alternativ übergeben wir dein Tier persönlich in Bielefeld oder auf der Terraristika Hamm.'),
    ('Reservierung', 'Wir reservieren dir ein Tier gerne für 5 Tage – ganz unverbindlich. Da in den letzten Jahren leider viele reservierte Tiere nie abgeholt wurden, bitten wir für längere Zeiträume um eine kleine Anzahlung von in der Regel 25 bis 50 €. Den Restbetrag begleichst du einfach bei der Übergabe.'),
    ('Rückgabe', 'Jedes Tier verlässt uns gesund, futterfest und mit dokumentierter Herkunft. Zum Schutz unseres Bestandes können wir abgegebene Tiere allerdings nicht zurücknehmen.'),
    ('Anzahlung', 'Eine Anzahlung ist verbindlich und wird bei der Übergabe vollständig auf den Kaufpreis angerechnet. Entscheidest du dich später doch anders, verbleibt sie bei uns – sofern nichts anderes vereinbart wurde. Sollten wir ein Tier einmal nicht wie zugesagt abgeben können, erstatten wir dir die Anzahlung natürlich vollständig.'),
]

# ---------------------------------------------------------------- Kornnatter
STATS = [
    ('thermometer-snowflake', '22–24 °C', 'kühle Seite'),
    ('sun', 'bis 30 °C', 'Sonnenplatz'),
    ('droplets', '40–60 %', 'Luftfeuchte'),
    ('hourglass', '20+ Jahre', 'Lebenserwartung'),
]

TOPICS = [
    {'id': 'haltung', 'title': 'Haltung', 'glyph': 'house',
     'intro': 'Kornnattern sind überwiegend dämmerungs- und nachtaktiv, nutzen aber auch tagsüber gerne erhöhte Plätze und Verstecke. Das Terrarium sollte deshalb ausreichend Platz zum Klettern, Erkunden und Zurückziehen bieten. Besonders wichtig ist eine abwechslungsreiche Strukturierung, damit sich die Tiere sicher fühlen und ihr natürliches Verhalten ausleben können.',
     'body': """Zur Grundausstattung gehören mehrere Verstecke, stabile Äste, Klettermöglichkeiten, eine ausreichend große Wasserschale sowie ein geeigneter Bodengrund. Eine Rückwand oder zusätzliche Pflanzen sorgen für weitere Deckungsmöglichkeiten und schaffen eine natürliche Atmosphäre.
## Temperatur und Klima
Kornnattern regulieren ihre Körpertemperatur über die Umgebung. Deshalb sollte im Terrarium immer ein Temperaturgefälle vorhanden sein.
- **Warme Seite:** 27–29 °C
- **Sonnenplatz:** bis etwa 30 °C
- **Kühle Seite:** 22–24 °C
- **Nachttemperatur:** 20–22 °C
Die Luftfeuchtigkeit liegt meist zwischen 40 und 60 Prozent. Während der Häutung darf sie kurzfristig etwas höher sein, damit sich die Haut problemlos lösen kann.
## Einrichtung
Ein gut eingerichtetes Terrarium bietet deutlich mehr als nur einen Schlafplatz. Unterschiedliche Ebenen, Äste, Korkröhren und Verstecke fördern das natürliche Verhalten der Tiere und sorgen gleichzeitig für Sicherheit. Besonders Jungtiere profitieren von vielen Rückzugsmöglichkeiten.
## Einzelhaltung
Kornnattern sind Einzelgänger und sollten außerhalb geplanter Verpaarungen grundsätzlich einzeln gehalten werden. Eine dauerhafte Gruppenhaltung bietet den Tieren keinen Vorteil und kann zu Stress oder Konkurrenzverhalten führen.""",
     'fazit': 'In einem ausreichend großen Terrarium, passenden Temperaturen, abwechslungsreicher Einrichtung und einer regelmäßigen Kontrolle der Haltungsbedingungen lässt sich eine Kornnatter viele Jahre gesund halten. Bei guter Pflege erreichen die Tiere häufig ein Alter von über 20 Jahren.'},
    {'id': 'ernaehrung', 'title': 'Ernährung', 'glyph': 'utensils',
     'intro': 'Eine ausgewogene Ernährung ist die Grundlage für gesunde und vitale Kornnattern. Als reine Fleischfresser ernähren sie sich ausschließlich von kleinen Wirbeltieren. In der Terrarienhaltung haben sich tiefgefrorene und anschließend vollständig aufgetaute Futtermäuse bewährt. Die Futtergröße und die Fütterungsintervalle sollten dabei immer an Alter, Größe und Kondition des jeweiligen Tieres angepasst werden.',
     'body': """## Geeignete Futtertiere
Das wichtigste Futtertier für Kornnattern ist die Maus. Je nach Größe der Schlange werden Baby-, Springer-, adulte oder größere Mäuse verfüttert. Das Beutetier sollte dabei ungefähr den Umfang der breitesten Körperstelle der Schlange besitzen. So kann die Nahrung problemlos verdaut werden.
Wir empfehlen ausschließlich tiefgefrorene Futtertiere zu verwenden. Sie sind hygienisch, einfach zu lagern und vermeiden das Verletzungsrisiko, das von lebenden Futtertieren ausgehen kann.
## Fütterungsintervalle
Wie häufig eine Kornnatter gefüttert werden sollte, hängt in erster Linie vom Alter und Wachstum des Tieres ab. Während Jungtiere regelmäßig Nahrung benötigen, verlängern sich die Fütterungsintervalle bei adulten Tieren deutlich.
- **Jungtiere:** etwa alle 5–7 Tage
- **Halbwüchsige Tiere:** etwa alle 7–10 Tage
- **Adulte Tiere:** etwa alle 10–14 Tage
#### Munson Plan Feeding Schedule
Der **Munson Plan** zählt zu den bekanntesten Fütterungsempfehlungen für Kornnattern und wird besonders in den USA häufig verwendet. Er ordnet das Körpergewicht der Schlange einer passenden Futtergröße sowie einem empfohlenen Fütterungsintervall zu und bietet damit eine hilfreiche Orientierung. Dennoch sollte jede Kornnatter individuell betrachtet werden, da Wachstum, Aktivität und Körperkondition von Tier zu Tier unterschiedlich sein können.
- Single pinks (2–3g) every 4 to 5 days for snakes weighing 4–15g.
- Double pinks (3g x 2) every 4 to 5 days for snakes weighing 16–23g.
- Small fuzzies (5–7g) every 5 to 6 days for snakes weighing 24–30g.
- Regular fuzzies (7–9g) every 5 to 6 days for snakes weighing 30–50g.
- Hoppers (9–12g) every 5 to 6 days for snakes weighing 51–90g.
- Weaned mice (14–20g) every 7 days for snakes weighing 91–170g.
- Adult mice (24–30g) every 7+ days for snakes weighing 170g+
Eine regelmäßige Gewichtskontrolle hilft dabei, die Futtermenge an die individuelle Entwicklung der Schlange anzupassen.
## Frisches Wasser
Neben der Fütterung spielt die Wasserversorgung eine wichtige Rolle. Eine ausreichend große Wasserschale sollte jederzeit mit frischem Wasser gefüllt sein. Viele Kornnattern trinken regelmäßig und nutzen die Schale gelegentlich auch zum Baden – insbesondere während der Häutung.
## Verdauung
Nach einer Mahlzeit benötigen Kornnattern mehrere Tage, um die Nahrung vollständig zu verdauen. Während dieser Zeit sollte das Tier möglichst nicht gestört oder herausgenommen werden. Ruhe und eine passende Temperatur unterstützen eine problemlose Verdauung und vermeiden unnötigen Stress.""",
     'fazit': 'Eine angepasste Fütterung, frisches Wasser und ausreichend Ruhe nach dem Fressen bilden die Grundlage für eine gesunde Entwicklung. Wer das Gewicht seiner Tiere regelmäßig kontrolliert und die Futtermenge entsprechend anpasst, schafft optimale Voraussetzungen für ein langes und gesundes Leben der Kornnatter.'},
    {'id': 'winterruhe', 'title': 'Winterruhe', 'glyph': 'snowflake',
     'intro': 'Die Winterruhe ist ein natürlicher Bestandteil des Lebenszyklus der Kornnatter. In ihrem ursprünglichen Verbreitungsgebiet sinken die Temperaturen während der Wintermonate deutlich ab, wodurch die Tiere ihren Stoffwechsel reduzieren und mehrere Wochen ruhen. Auch in der Terrarienhaltung kann eine kontrollierte Winterruhe sinnvoll sein, insbesondere wenn Tiere später zur Zucht eingesetzt werden sollen.',
     'body': """## Warum ist die Winterruhe wichtig?
Während der Winterruhe fährt der Körper seinen Stoffwechsel deutlich herunter. Die Tiere nehmen keine Nahrung mehr auf und verbrauchen nur wenig Energie. Diese natürliche Ruhephase unterstützt den Jahresrhythmus der Kornnatter und gilt als wichtiger Bestandteil einer langfristig artgerechten Haltung. Bei Zuchttieren fördert sie zudem die Fortpflanzungsbereitschaft im Frühjahr.
## Vorbereitung
Eine erfolgreiche Winterruhe beginnt bereits einige Wochen vorher. Die Fütterung wird rechtzeitig eingestellt, damit der Verdauungstrakt vor der Abkühlung vollständig entleert ist. Anschließend werden Beleuchtungsdauer und Temperaturen schrittweise reduziert. Ein langsamer Übergang vermeidet unnötigen Stress und ermöglicht dem Stoffwechsel, sich an die veränderten Bedingungen anzupassen.
## Durchführung
Während der Winterruhe werden Kornnattern meist für acht bis zwölf Wochen bei Temperaturen zwischen 10 und 15 °C gehalten. Die Tiere erhalten in dieser Zeit kein Futter, frisches Wasser muss jedoch jederzeit zur Verfügung stehen. Regelmäßige Sichtkontrollen reichen aus, um den Gesundheitszustand zu überwachen, ohne die Tiere unnötig zu stören.
## Aufwärmphase
Nach der Winterruhe werden Temperatur und Beleuchtungsdauer langsam wieder erhöht. Erst wenn die Tiere einige Tage aktiv sind und ihre normale Körpertemperatur erreicht haben, erfolgt die erste Fütterung. Ein schrittweiser Übergang erleichtert dem Organismus die Rückkehr in den normalen Stoffwechsel.""",
     'fazit': 'Eine sorgfältig vorbereitete und kontrolliert durchgeführte Winterruhe orientiert sich am natürlichen Jahresrhythmus der Kornnatter. Sie trägt zum Wohlbefinden der Tiere bei und bildet für viele Zuchtprojekte die Grundlage einer erfolgreichen Fortpflanzung. Wichtig sind dabei gesunde Tiere, eine langsame Umstellung und eine regelmäßige Kontrolle während der gesamten Ruhephase.'},
    {'id': 'genetik', 'title': 'Genetik & Morphs', 'glyph': 'dna',
     'intro': 'Die enorme Farben- und Mustervielfalt macht die Kornnatter zu einer der faszinierendsten Schlangenarten in der Terraristik. Durch natürliche Mutationen und gezielte Verpaarungen sind im Laufe der Jahre zahlreiche Farb- und Zeichnungsvarianten entstanden, die als Morphs bezeichnet werden. Jede Kombination verleiht den Tieren ein individuelles Erscheinungsbild und eröffnet immer wieder neue Möglichkeiten für verantwortungsvolle Zuchtprojekte.',
     'body': """## Was sind Morphs?
Als Morph bezeichnet man eine genetisch bedingte Farb- oder Zeichnungsvariante einer Kornnatter. Während Wildformen überwiegend rotbraune und orange Farbtöne mit dunklen Sattelflecken besitzen, können Morphs nahezu vollständig rote, graue, gelbe oder kontrastreiche Erscheinungsbilder hervorbringen. Viele dieser Merkmale lassen sich miteinander kombinieren und ergeben eine beeindruckende Vielfalt.
## Genetik einfach erklärt
Jedes Jungtier erhält einen Teil seiner Gene von der Mutter und einen Teil vom Vater. Welche Merkmale später sichtbar werden, hängt davon ab, welche Gene beide Elterntiere weitergeben. Einige Eigenschaften setzen sich bereits mit einem vererbten Gen durch, andere werden erst sichtbar, wenn beide Eltern das entsprechende Merkmal vererben.
Aus diesem Grund unterscheiden Züchter zwischen sichtbaren Merkmalen und genetischen Anlagen, die zwar vorhanden sind, äußerlich jedoch nicht zu erkennen sind. Eine sorgfältige Dokumentation der Abstammung bildet deshalb die Grundlage jeder verantwortungsvollen Zucht.
> **„het“** steht für heterozygot. Das Tier trägt ein Gen, das äußerlich nicht sichtbar sein muss, aber an Nachkommen weitergegeben werden kann.
## Unsere Schwerpunkte
Unsere Zucht konzentriert sich insbesondere auf die Morphs **Hypo**, **Diffused (Bloodred)** und **Pied Sided**. Darüber hinaus arbeiten wir mit weiteren Merkmalen wie **Motley** und **Striped**, um langfristig charakterstarke und genetisch nachvollziehbare Linien aufzubauen.
## Verantwortungsvolle Zucht
Außergewöhnliche Farben allein machen noch keine gute Nachzucht aus. Gesundheit, Vitalität und eine nachvollziehbare Herkunft stehen für uns an erster Stelle. Jede Verpaarung wird sorgfältig geplant und dokumentiert, damit die genetischen Eigenschaften unserer Tiere langfristig erhalten und sinnvoll weiterentwickelt werden können.""",
     'fazit': 'Die Genetik der Kornnatter eröffnet nahezu unbegrenzte Möglichkeiten und macht jede Nachzucht einzigartig. Gleichzeitig erfordert sie Wissen, Geduld und Verantwortung. Nur durch eine sorgfältige Auswahl der Elterntiere und eine lückenlose Dokumentation entstehen gesunde Tiere mit einer nachvollziehbaren genetischen Herkunft.'},
    {'id': 'zucht', 'title': 'Zucht', 'glyph': 'egg',
     'intro': 'Die Zucht von Kornnattern verbindet Fachwissen, Geduld und Verantwortung. Ziel einer sorgfältigen Nachzucht ist nicht allein die Entstehung außergewöhnlicher Farb- und Zeichnungsvarianten, sondern vor allem die Aufzucht gesunder und vitaler Tiere. Jede Verpaarung sollte deshalb gut geplant und auf einer nachvollziehbaren genetischen Grundlage erfolgen.',
     'body': """## Auswahl der Zuchttiere
Nur gesunde und ausreichend entwickelte Kornnattern sollten zur Zucht eingesetzt werden. Neben dem äußeren Erscheinungsbild spielen auch Abstammung, genetische Merkmale und die allgemeine Kondition der Tiere eine wichtige Rolle. Eine sorgfältige Auswahl trägt dazu bei, stabile und langfristig gesunde Zuchtlinien aufzubauen.
## Paarung und Eiablage
Nach einer erfolgreichen Winterruhe beginnt im Frühjahr die Paarungszeit. Einige Wochen später legt das Weibchen – abhängig von Alter und Kondition – meist zwischen 10 und 30 Eier. Für eine erfolgreiche Entwicklung werden diese anschließend in einem Inkubator bei konstanten Temperaturen ausgebrütet.
## Inkubation
Während der Brutzeit benötigen die Eier eine gleichmäßige Temperatur und eine angepasste Luftfeuchtigkeit. Bereits kleine Schwankungen können die Entwicklung beeinflussen. Je nach Inkubationstemperatur schlüpfen die Jungtiere in der Regel nach etwa 55 bis 70 Tagen.
## Unsere Inkubation
> Wir inkubieren unsere Eier bei einer konstanten Temperatur von **27,5 °C**. Unter diesen Bedingungen schlüpfen die Jungtiere in der Regel nach etwa **65 Tagen**. Je nach Gelege und Entwicklung kann der Schlupftermin um wenige Tage variieren.
## Aufzucht der Jungtiere
Nach dem Schlupf verbleiben die Jungtiere zunächst in ihren Aufzuchtboxen und häuten sich zum ersten Mal. Erst danach erfolgt die erste Fütterung. In den folgenden Monaten werden Wachstum, Gewicht und Häutungen regelmäßig dokumentiert, um die Entwicklung jedes einzelnen Tieres aufmerksam zu begleiten.
## Unsere Philosophie
Für uns bedeutet Zucht weit mehr als das Vermehren von Kornnattern. Gesundheit, eine nachvollziehbare Genetik und eine sorgfältige Dokumentation stehen im Mittelpunkt jeder Verpaarung. Unser Ziel ist es, charakterstarke Tiere aufzuziehen und jede Generation bewusst weiterzuentwickeln – Qualität ist dabei wichtiger als Quantität.""",
     'fazit': 'Verantwortungsvolle Kornnatterzucht erfordert Zeit, Erfahrung und Geduld. Wer seine Tiere sorgfältig auswählt, ihre Entwicklung dokumentiert und das Wohl der Tiere stets in den Mittelpunkt stellt, schafft die Grundlage für gesunde Nachzuchten und langfristig erfolgreiche Zuchtprojekte.'},
    {'id': 'faq', 'title': 'FAQ', 'glyph': 'circle-help', 'intro': '', 'fazit': '',
     'body': """## Sind Kornnattern für Anfänger geeignet?
Ja. Aufgrund ihres ruhigen Wesens und der vergleichsweise einfachen Haltung gelten Kornnattern als eine der beliebtesten Schlangenarten für Einsteiger. Dennoch sollte man sich vor der Anschaffung intensiv mit den Bedürfnissen der Tiere beschäftigen und die langfristige Verantwortung berücksichtigen.
## Wie alt werden Kornnattern?
Bei artgerechter Haltung erreichen Kornnattern häufig ein Alter von 20 Jahren oder mehr. Eine ausgewogene Ernährung, passende Haltungsbedingungen und regelmäßige Kontrollen tragen wesentlich zu einem langen und gesunden Leben bei.
## Wie groß werden Kornnattern?
Ausgewachsene Kornnattern erreichen in der Regel eine Länge zwischen 100 und 150 Zentimetern. Größe und Gewicht können je nach Herkunft und individueller Entwicklung etwas variieren.
## Sind Kornnattern giftig?
Nein. Kornnattern gehören zu den ungiftigen Würgeschlangen. Sie töten ihre Beute durch Umschlingen und stellen für den Menschen keine Gefahr dar.
## Müssen Kornnattern einzeln gehalten werden?
Ja. Kornnattern sind Einzelgänger und sollten außerhalb geplanter Verpaarungen grundsätzlich einzeln gehalten werden. So lassen sich Stress und Konkurrenzverhalten vermeiden.
## Wie oft muss eine Kornnatter gefüttert werden?
Das Fütterungsintervall richtet sich nach Alter und Größe des Tieres. Jungtiere werden häufiger gefüttert als adulte Kornnattern. Ausführliche Informationen findest du im Abschnitt „Ernährung“.
## Brauchen Kornnattern eine Winterruhe?
Eine Winterruhe orientiert sich am natürlichen Jahresrhythmus der Tiere und ist insbesondere für Zuchttiere empfehlenswert. Bei reinen Liebhabertieren wird sie unterschiedlich gehandhabt und sollte gut vorbereitet werden.
## Was bedeutet „het“?
„Het“ ist die Abkürzung für „heterozygot“. Das bedeutet, dass ein Tier ein bestimmtes Gen trägt, dieses äußerlich jedoch nicht sichtbar sein muss. Es kann das Merkmal aber an seine Nachkommen weitergeben.
## Was bedeutet Diffused (Bloodred)?
Diffused ist eine Farbmutation, die früher häufig als Bloodred bezeichnet wurde. Sie reduziert die typische Rückenzeichnung und sorgt für eine besonders intensive rote Färbung ausgewachsener Tiere.
## Was bedeutet Pied Sided?
Pied Sided beschreibt eine Zeichnungsvariante mit unterschiedlich stark ausgeprägten weißen Bereichen an den Körperseiten. Der Weißanteil kann von Tier zu Tier deutlich variieren und macht jede Kornnatter einzigartig.
## Wo finde ich eure aktuellen Nachzuchten?
Unsere aktuell verfügbaren Nachzuchten veröffentlichen wir über **Morphmarket**.
## Kann ich euch bei Fragen kontaktieren?
Natürlich. Wenn du Fragen zu unseren Tieren, unseren Projekten oder zur Haltung von Kornnattern hast, freuen wir uns über deine Nachricht. Nutze dafür einfach unser Kontaktformular."""},
]

# ---------------------------------------------------------------- App
APP_FEATURES = [
    {'icon': 'layout-dashboard', 'title': 'Hub', 'claim': 'alles Wichtige auf einen Blick.', 'lead': 'Der Hub ist die zentrale Übersicht der App.',
     'paras': ['Hier findest du auf einen Blick die wichtigsten Informationen zu deinem Bestand – von der Anzahl deiner Tiere über aktuelle Gelege bis hin zu anstehenden Ereignissen. So hast du jederzeit einen schnellen Überblick darüber, was gerade passiert und worauf du achten solltest.'],
     'points': ['Lorem ipsum dolor sit amet', 'Laufende Inkubationen mit Schlupftermin', 'Letzte Einträge im Bestand'],
     'screenshot': ''},  # z. B. 'img/app/hub.jpg' (1179 × 2556)
    {'icon': 'library', 'title': 'Collection', 'claim': 'dein Bestand. Übersichtlich organisiert.', 'lead': 'In der Collection findest du alle deine Tiere an einem Ort.',
     'paras': ['Mit verschiedenen Filtern und Suchmöglichkeiten kannst du deinen Bestand gezielt nach Merkmalen wie Geschlecht, Genetik, Alter oder individuellen Tags durchsuchen.', 'So findest du schnell genau die Tiere, nach denen du gerade suchst – auch wenn dein Bestand wächst.'],
     'points': ['Lorem ipsum dolor sit amet', 'Fotohistorie über alle Lebensphasen', 'Genetik inklusive het-Angaben'],
     'screenshot': ''},
    {'icon': 'git-fork', 'title': 'Lineage', 'claim': 'Abstammung einfach nachvollziehen.', 'lead': 'Lineage verbindet die Tiere deines Bestands miteinander und macht ihre Abstammung übersichtlich sichtbar.',
     'paras': ['Eltern, Nachkommen und genetische Informationen lassen sich direkt miteinander verknüpfen und nachvollziehen. So entsteht mit der Zeit eine vollständige Übersicht über die Entwicklung deiner Zucht und die Linien hinter jedem Tier.'],
     'points': ['Eltern, Geschwister und Gelege verknüpft', 'Stammbaum über mehrere Generationen', 'Nachvollziehbare Herkunft bei der Übergabe'],
     'screenshot': ''},
]
APP_SCREENSHOT_HOME = ''  # Screenshot im Smartphone-Mockup auf der Startseite

# ---------------------------------------------------------------- Kontakt
CONTACT_INFO = [
    ('mail', 'E-Mail', EMAIL, 'mailto:' + EMAIL),
    ('map-pin', 'Übergabe', 'Persönlich in Bielefeld oder auf der Terraristika Hamm', ''),
    ('store', 'Nachzuchten', 'Alle verfügbaren Tiere auf MorphMarket', MORPHMARKET_SHOP),
]
CONTACT_TOPICS = ['Nachzucht', 'Projekte', 'Haltung', 'Sonstiges']

# ---------------------------------------------------------------- Rechtliches
# Zeilen mit "|" = Adressblock, "> " = Hinweis, "- " = Liste. RECHTLICH PRÜFEN LASSEN.
# Abschnitt "Google Fonts" ist entfallen: Roboto wird lokal ausgeliefert (src/fonts).
IMPRESSUM = {'title': 'Impressum', 'stand': 'Stand: September 2026', 'body': """## Angaben gemäß § 5 DDG
Max Mustermann|Musterstraße 12|12345 Musterstadt|Deutschland
## Kontakt
E-Mail: hallo@example.de
## Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV
Max Mustermann|Musterstraße 12|12345 Musterstadt
## Hinweis zur Hobbyzucht
Bleeding Edge Corns ist eine private, nicht gewerbliche Hobbyzucht von Kornnattern. Diese Website dient ausschließlich der Information über unsere Tiere und Zuchtprojekte.
## Haftung für Inhalte
Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Die Angaben zur Haltung von Kornnattern ersetzen keine individuelle Beratung.
## Haftung für Links
Diese Website enthält Links zu externen Websites, insbesondere zu MorphMarket. Auf deren Inhalte haben wir keinen Einfluss. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.
## Urheberrecht
Die Texte und Fotos auf dieser Website unterliegen dem deutschen Urheberrecht. Eine Vervielfältigung oder Verwendung ist ohne ausdrückliche Zustimmung nicht gestattet."""}

DATENSCHUTZ = {'title': 'Datenschutz', 'stand': 'Stand: September 2026', 'body': """## 1. Verantwortlicher
Verantwortlich für die Verarbeitung personenbezogener Daten auf dieser Website ist:
Max Mustermann|Musterstraße 12|12345 Musterstadt|Deutschland|E-Mail: hallo@example.de
## 2. Allgemeine Hinweise
Der Schutz deiner persönlichen Daten ist uns wichtig. Wir behandeln deine personenbezogenen Daten vertraulich und entsprechend den gesetzlichen Datenschutzvorschriften sowie dieser Datenschutzerklärung.
Diese Website dient der Information über unsere private Hobbyzucht von Kornnattern sowie der Vorstellung eigener Nachzuchten.
Personenbezogene Daten werden auf dieser Website nur verarbeitet, soweit dies für den Betrieb der Website oder die Bearbeitung von Anfragen erforderlich ist.
## 3. Aufruf der Website
Beim Aufruf dieser Website werden durch den Webserver technisch notwendige Informationen verarbeitet. Dazu können insbesondere gehören:
- IP-Adresse des zugreifenden Geräts
- Datum und Uhrzeit des Zugriffs
- aufgerufene Seiten
- übertragene Datenmenge
- verwendeter Browser und Betriebssystem
- gegebenenfalls die zuvor besuchte Seite (Referrer)
Die Verarbeitung erfolgt, um die Website technisch bereitzustellen, die Sicherheit und Stabilität des Angebots zu gewährleisten und technische Fehler zu erkennen.
Rechtsgrundlage für diese Verarbeitung ist Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse liegt im sicheren und zuverlässigen Betrieb der Website.
Die Daten werden gelöscht, sobald sie für die genannten Zwecke nicht mehr erforderlich sind, sofern keine gesetzlichen Aufbewahrungspflichten entgegenstehen.
Die konkrete Speicherdauer kann von den Einstellungen und Vorgaben unseres Webhosting-Anbieters abhängen.
## 4. Webhosting
Diese Website wird bei einem externen Webhosting-Anbieter betrieben.
Beim Aufruf der Website werden technisch notwendige Daten an den Server unseres Hosting-Anbieters übertragen und dort verarbeitet. Dazu können insbesondere IP-Adresse, Datum und Uhrzeit des Zugriffs, Browserinformationen und aufgerufene Inhalte gehören.
Der Hosting-Anbieter verarbeitet diese Daten in unserem Auftrag. Soweit erforderlich, besteht mit dem Hosting-Anbieter ein Vertrag zur Auftragsverarbeitung gemäß Art. 28 DSGVO.
Hosting-Anbieter:|[Name des Hosting-Anbieters eintragen]
Die Verarbeitung erfolgt zum Zweck der sicheren und zuverlässigen Bereitstellung dieser Website.
Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse besteht in der technisch sicheren und zuverlässigen Bereitstellung unseres Internetangebots.
## 5. Kontaktformular
Auf unserer Website besteht die Möglichkeit, über ein Kontaktformular mit uns in Verbindung zu treten.
Bei der Nutzung des Kontaktformulars werden folgende Angaben verarbeitet:
- Name
- E-Mail-Adresse
- gewähltes Thema der Anfrage
- optional die Tier-ID einer Nachzucht
- Nachricht bzw. sonstige Angaben im Freitextfeld
Die Angabe des Namens und der E-Mail-Adresse ist erforderlich, damit wir die Anfrage bearbeiten und beantworten können.
Die von dir übermittelten Daten werden ausschließlich zur Bearbeitung deiner Anfrage und für die damit verbundene Kommunikation verwendet. Eine Nutzung zu Werbezwecken oder eine Weitergabe an Dritte erfolgt nicht, sofern hierfür keine gesetzliche Verpflichtung besteht oder du ausdrücklich eingewilligt hast.
Rechtsgrundlage für die Verarbeitung ist Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse besteht darin, eingehende Anfragen beantworten und mit dir kommunizieren zu können.
Sofern deine Anfrage auf den Abschluss eines Vertrags oder die Anbahnung eines Vertragsverhältnisses gerichtet ist, kann zusätzlich Art. 6 Abs. 1 lit. b DSGVO als Rechtsgrundlage dienen.
Die über das Kontaktformular übermittelten Daten werden nur so lange gespeichert, wie dies für die Bearbeitung der Anfrage erforderlich ist. Nach abschließender Bearbeitung der Anfrage werden die Daten gelöscht, sofern keine gesetzlichen Aufbewahrungspflichten oder andere rechtliche Gründe für eine weitere Speicherung bestehen.
## 6. Bilder und Links zu MorphMarket
> Dieser Abschnitt entfällt, sobald die Fotos der Nachzuchten lokal auf dem eigenen Webserver gespeichert werden.
Auf den Seiten „Startseite“ und „Nachzuchten“ zeigen wir Fotos unserer aktuellen Nachzuchten. Diese Fotos werden derzeit direkt von Servern der Plattform MorphMarket geladen. Dabei kann insbesondere die IP-Adresse des zugreifenden Geräts an MorphMarket bzw. deren Dienstleister übermittelt werden.
Klickst du auf eine Nachzucht oder einen MorphMarket-Button, wirst du auf die Website von MorphMarket weitergeleitet. Dort gelten die Datenschutzbestimmungen von MorphMarket.
Rechtsgrundlage ist Art. 6 Abs. 1 lit. f DSGVO. Unser berechtigtes Interesse besteht in einer aktuellen und übersichtlichen Darstellung unserer verfügbaren Nachzuchten.
## 7. Keine Analyse- oder Tracking-Dienste
Auf dieser Website werden derzeit keine Analyse-, Tracking- oder Werbedienste eingesetzt.
Insbesondere verwenden wir derzeit:
- kein Google Analytics
- keine vergleichbaren Analysewerkzeuge
- keine personalisierte Werbung
- kein Social-Media-Tracking
Sollten zukünftig entsprechende Dienste eingesetzt werden, wird diese Datenschutzerklärung vor deren Einsatz entsprechend angepasst.
## 8. Cookies
Diese Website verwendet derzeit keine Cookies, die einer Analyse des Nutzungsverhaltens oder zu Werbezwecken dienen.
Soweit für den technischen Betrieb der Website technisch notwendige Cookies eingesetzt werden sollten, dienen diese ausschließlich der Bereitstellung der jeweiligen Funktion.
## 9. Weitergabe von Daten
Eine Weitergabe personenbezogener Daten an Dritte erfolgt grundsätzlich nicht.
Eine Weitergabe kann erfolgen, soweit dies zur technischen Bereitstellung der Website erforderlich ist, beispielsweise an den von uns beauftragten Webhosting-Anbieter, oder wenn wir hierzu gesetzlich verpflichtet sind.
Eine Übermittlung personenbezogener Daten zu Werbezwecken findet nicht statt.
## 10. Deine Rechte
Du hast im Rahmen der gesetzlichen Voraussetzungen folgende Rechte hinsichtlich deiner personenbezogenen Daten:
- Recht auf Auskunft gemäß Art. 15 DSGVO
- Recht auf Berichtigung gemäß Art. 16 DSGVO
- Recht auf Löschung gemäß Art. 17 DSGVO
- Recht auf Einschränkung der Verarbeitung gemäß Art. 18 DSGVO
- Recht auf Datenübertragbarkeit gemäß Art. 20 DSGVO
- Recht auf Widerspruch gemäß Art. 21 DSGVO
Wenn die Verarbeitung deiner personenbezogenen Daten auf Art. 6 Abs. 1 lit. f DSGVO beruht, kannst du aus Gründen, die sich aus deiner besonderen Situation ergeben, jederzeit Widerspruch gegen diese Verarbeitung einlegen.
Zur Ausübung deiner Rechte kannst du dich jederzeit über die oben genannten Kontaktdaten an uns wenden.
## 11. Beschwerderecht bei einer Aufsichtsbehörde
Wenn du der Ansicht bist, dass die Verarbeitung deiner personenbezogenen Daten gegen die Datenschutz-Grundverordnung verstößt, hast du das Recht, dich bei einer Datenschutzaufsichtsbehörde zu beschweren.
Das Beschwerderecht besteht insbesondere bei der Datenschutzaufsichtsbehörde deines gewöhnlichen Aufenthaltsortes, deines Arbeitsplatzes oder des Ortes, an dem der mutmaßliche Verstoß stattgefunden hat.
## 12. Aktualität dieser Datenschutzerklärung
Wir behalten uns vor, diese Datenschutzerklärung anzupassen, wenn sich die technische Ausstattung oder die Funktionen dieser Website ändern oder neue rechtliche Anforderungen hinzukommen."""}
