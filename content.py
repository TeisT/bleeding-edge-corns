# ALLE TEXTE DER WEBSITE – nach Seiten sortiert.
# Nach einer Änderung neu bauen:  python3 build.py
#
# Schreibweisen in Texten:
#   **fett**              → fett
#   [[Wort Wort]]         → diese Wörter nicht umbrechen
#   [Linktext](seite/)    → Link (interne Seiten relativ zur Startseite, z. B. kornnatter/ oder datenschutz/)
# In langen Texten (Kornnatter, Rechtliches) zusätzlich am Zeilenanfang:
#   "## " Zwischenüberschrift, "#### " kleine Überschrift, "- " Listenpunkt, "> " Hinweisbox
#   (Rechtliches: Zeilen mit "|" werden als Adressblock untereinander gesetzt)
#
# Wichtig: Texte stehen in Anführungszeichen. Kommt im Text selbst ein ' vor, den Text in "…" setzen
# (oder umgekehrt). Kommas zwischen den Einträgen nicht löschen.

# ============================================================================
# ALLGEMEIN (alle Seiten)
# ============================================================================
MORPHMARKET_SHOP = 'https://www.morphmarket.com/stores/andreasp/'
EMAIL = 'kontakt@bleeding-edge-corns.com'

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

# Texte, die auf mehreren Seiten vorkommen
SITE = {
    'name': 'Bleeding Edge Corns',
    'footer_text': 'Eine kleine, private Hobbyzucht aus Bielefeld – mit einem Herz für Pied-Sided Kornnattern.',
    'copyright': '© 2026 Bleeding Edge Corns',
    'impressum': 'Impressum',
    'datenschutz': 'Datenschutz',
    'mm_button': 'Nachzuchten',          # MorphMarket-Button im Header, Menü und unten (mobil)
    'logo_alt': 'Bleeding Edge Corns',
    'home_label': 'Bleeding Edge Corns – Startseite',
    'menu': 'Menü',
    'menu_close': 'Menü schließen',
    'lang_label': 'Sprache wählen',
    'prev': 'Zurück',
    'next': 'Weiter',
    # nur für Screenreader (unsichtbar)
    'nav_main': 'Hauptnavigation',
    'nav_mobile': 'Mobile Navigation',
    'nav_footer': 'Footer-Navigation',
    'mm_logo_alt': 'MorphMarket',
}

# Kontakt-Teaser unten auf den Seiten (Überschrift steht bei der jeweiligen Seite)
CONTACT_TEASER = {
    'eyebrow': 'Kontakt',
    'text': 'Schreib uns – wir melden uns schnellstmöglich.',
    'button': 'Kontakt aufnehmen',
}

# Nachzuchten-Slider (Startseite und Seite „Nachzuchten“)
ANIMAL_SLIDER = {
    'heading': 'Nur ein kleiner Ausschnitt – **alle Tiere findest du auf MorphMarket.**',
    'card_link': 'Auf MorphMarket ansehen',
    'female': 'Weibchen',
    'male': 'Männchen',
    'unknown': 'Unbestimmt',
    'all_eyebrow': 'Dies war nur eine kleine Auswahl',
    'all_title': 'Alle **Nachzuchten** ansehen',
    'all_text': 'Der komplette, aktuelle Bestand mit Genetik und Preisen.',
    'all_pill': 'MorphMarket',
    'all_button': 'Alle Nachzuchten',
    'bar_label': 'Slider scrollen',
}

# ============================================================================
# STARTSEITE
# ============================================================================

HOME = {
    'title': 'Startseite',
    'description': 'Bleeding Edge Corns – private Kornnattern-Hobbyzucht aus Bielefeld mit Schwerpunkt Pied-Sided, Motley und Striped.',
    # Bühne
    'hero_eyebrow_before': "We're in",   # dazwischen das Herz-Icon
    'hero_eyebrow_after': 'with pieds',
    'hero_eyebrow_label': "We're in love with pieds",
    'hero_h1': '**[[Bleeding Edge]] Corns:** Kornnattern aus Bielefeld',
    'hero_text': 'Unsere Leidenschaft gilt Pied-Sided Kornnattern und den faszinierenden Zeichnungsvarianten Motley & Stripe.',
    'hero_button_1': 'Nachzuchten',
    'hero_button_2': 'Projekte',
    'hero_img_alt': 'Pied-Sided Kornnatter',
    # Projekte
    'projects_eyebrow': 'Projekte',
    'projects_h2': 'Unsere **Zuchtprojekte**',
    'projects_link': 'Zum Projekt',
    # Galerie
    'gallery_eyebrow': 'Galerie',
    'gallery_h2': 'Einblicke in **unsere Zucht**',
    'gallery_filter_label': 'Galerie filtern',
    'gallery_bar_label': 'Galerie scrollen',
    # Über uns
    'about_eyebrow': 'Über uns',
    'about_h2': 'Wer hinter **Bleeding Edge Corns** steckt',
    'about_lead': 'Hi! Ich bin Torben – der Kopf hinter Bleeding Edge Corns.',
    'about_paras': [
        'Seit 2007 halte ich Reptilien, und Pied-Sided Kornnattern faszinieren mich schon seit vielen Jahren. Über die Zeit haben mich ganz unterschiedliche Schlangen begleitet. Viele Arten kamen und gingen – die Kornnattern sind geblieben.',
        'Heute bin ich Vater von zwei Jungs und arbeite als Hobby weiterhin mit einer kleinen Gruppe ausgewählter Tiere. Mein Wunsch: noch viele Menschen für diese spannenden Tiere zu begeistern.',
    ],
    'about_link': 'Du hast Fragen? Dann schreib mir gerne eine Nachricht\u00a0→',
    'about_img_alt': 'Torben mit einer Kornnatter',
    # App
    'app_eyebrow': 'Unsere App',
    'app_h2': 'Deine Nattern. **Im Cornnector verbunden.**',
    'app_free': 'Kostenlos für iPhone und Android.',
    'app_link': 'Mehr zur App',
    # Kontakt-Teaser
    'contact_h2': 'Fragen, Interesse oder **Anmerkungen?**',
}

# Vertrauensleiste: (Icon, Titel, Text)
TRUST = [
    ('egg', 'Eigene Zuchten', 'Alle Tiere schlüpfen bei uns in Bielefeld.'),
    ('cn-lineage', 'Dokumentierte Abstammung', 'Mit Cornnector, unserer eigenen App, genau nachvollziehbar.'),
    ('store', 'Store auf MorphMarket', 'Alle verfügbaren Tiere mit Genetik und Preisen.'),
    ('map-pin', 'Übergabe in Bielefeld & Hamm', 'Persönlich vor Ort oder auf der Terraristika Hamm.'),
]

# Galerie Startseite: Fotos, Bildunterschriften und Kategorien stehen in data/galerie.csv
# (Spalten Datei;Bildunterschrift;Kategorie – mehrere Kategorien durch Komma trennen;
# Reihenfolge der Zeilen = Reihenfolge auf der Seite,
# Fotos liegen in src/img/galerie/). Hier nur die Reihenfolge der Filter-Buttons:
# erst „Alle“, dann diese Kategorien, danach neue Kategorien aus der CSV in der Reihenfolge ihres Auftretens.
# Kategorien ohne Foto werden ausgeblendet.
GALLERY_ALL = 'Alle'
GALLERY_CATS = ['Diffused', 'Charcoal', 'Motley & Striped', 'Vanish', 'Andere Tiere']
GALLERY_LABELS = {}   # Beschriftung der Filter-Buttons, falls abweichend von der Kategorie (nur Englisch nötig)

APP_POINTS = [
    ('cn-hub', 'Hub', 'Fällige Fütterungen, Häutungen und Gelege auf einen Blick.'),
    ('cn-collection', 'Bestand', 'Jedes Tier mit Foto, Genetik und Verlauf.'),
    ('cn-incubator', 'Inkubator', 'Gelege mit Schlupfprognose im Blick.'),
    ('cn-lineage', 'Stammbaum', 'Eltern, Geschwister und Nachzuchten verknüpft.'),
    ('cn-calculator', 'Genetikrechner', 'Verpaarungen durchspielen, bevor sie stattfinden.'),
]

# ============================================================================
# PROJEKTE + PROJEKT-DETAILSEITEN
# ============================================================================

PROJEKTE = {
    'title': 'Projekte',
    'description': 'Unsere Zuchtprojekte: Hypo Diffused High Pieds, Diffused Motley & Striped Pieds und Vanishing Motley & Striped.',
    'eyebrow': 'Projekte',
    'h1': 'Unsere **Zuchtprojekte**',
    'intro': 'Wir arbeiten an wenigen, klar definierten Projekten. Jedes verfolgt ein eigenes Zuchtziel auf Pied-Sided-Basis – kombiniert mit Hypo, Diffused, Motley und Striped.',
    'project_label': 'Projekt',          # „Projekt 1“, „Projekt 2“ …
    'genes_label': 'Genetik',
    'button': 'Details zum Projekt',
    'contact_h2': 'Fragen zu einem **Projekt?**',
}

# Projekt-Detailseiten (gemeinsame Texte; Inhalte je Projekt stehen in PROJECTS)
PROJEKT_DETAIL = {
    'description': 'Zuchtprojekt {title} – {teaser}',   # {title} und {teaser} werden ersetzt
    'breadcrumb': 'Projekte',
    'breadcrumb_label': 'Brotkrumen',
    'gallery_eyebrow': 'Galerie',
    'gallery_h2': 'Fotos aus **diesem Projekt**',
    'gallery_bar_label': 'Galerie scrollen',
    'all_projects': 'Alle Projekte',
    'contact_h2': 'Fragen, Interesse oder **Anmerkungen?**',
}

# Die drei Projekte (Projektseite, Detailseiten, Startseite, Navigation)
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

# ============================================================================
# NACHZUCHTEN
# ============================================================================

NACHZUCHTEN = {
    'title': 'Nachzuchten',
    'description': 'Aktuelle Kornnattern-Nachzuchten von Bleeding Edge Corns – alle verfügbaren Tiere auf MorphMarket.',
    'eyebrow': 'Nachzuchten',
    'h1': 'Aktuelle **Nachzuchten**',
    'intro': 'Hier siehst du eine kleine Auswahl. Alle verfügbaren Nachzuchten findest du auf MorphMarket.',
    'button': 'Alle Nachzuchten',
    'steps_eyebrow': 'So bekommst du dein Tier',
    'faq_eyebrow': 'FAQ',
    'faq_h2': 'Häufige **Fragen**',
    'faq_text': 'Einen kurzen Überblick zur Haltung findest du auf unserer Seite [Kornnatter](kornnatter/).',
    'contact_h2': 'Fragen, Interesse oder **Anmerkungen?**',
}

# Ablauf in 4 Schritten: (Icon, Titel, Text)
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

# ============================================================================
# KORNNATTER
# ============================================================================

KORNNATTER = {
    'title': 'Kornnatter',
    'description': 'Die Kornnatter (Pantherophis guttatus) kurz erklärt: Haltung, Ernährung, Winterruhe, Genetik, Zucht und FAQ.',
    'eyebrow': 'Kurz erklärt',
    'h1': 'Die Kornnatter – **Pantherophis guttatus**',
    'lead': 'Die Kornnatter gehört zu den beliebtesten Schlangen in der Terraristik – und das aus gutem Grund. Sie überzeugt durch ihr ruhiges Wesen, ihre beeindruckende Farbenvielfalt und eine vergleichsweise unkomplizierte Haltung. Dennoch trägt jeder Halter die Verantwortung, seinem Tier dauerhaft eine artgerechte Umgebung zu bieten!',
    'text': 'Auf dieser Seite findest du einen kompakten Überblick über die wichtigsten Themen rund um die Kornnatter.',
    'img_alt': 'Kornnatter',
    'topics_eyebrow': 'Themen',
    'topics_h2': 'Alles, was du **wissen musst**',
    'fazit_label': 'Fazit',
    'close_button': 'Schließen ↑',
}

# Kennzahlen: (Icon, Wert, Beschriftung)
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

# ============================================================================
# APP
# ============================================================================

APP = {
    'title': 'App',
    'description': 'Cornnector – die App für Kornnattern-Halter und -Züchter: Fütterung, Häutung, Verpaarung, Gelege und Genetik in einer App. Kostenlos für iPhone und Android.',
    'eyebrow': 'Unsere App',
    'h1': 'Deine Nattern. **Im Cornnector verbunden.**',
    'free': 'Kostenlos für iPhone und Android.',   # Zeile direkt unter der Überschrift
    'intro': '**Cornnector** dokumentiert Fütterungen, Häutungen, Verpaarungen und Gelege – inklusive genetischer Ergebnisse. Alle Informationen digital. Direkt dort, wo du sie brauchst.',
    # Abschluss unter den Funktionen: Link zur Cornnector-Seite
    'cta_h2': 'Alles über **Cornnector**',
    'cta_text': 'Alle Funktionen, die Anleitung und die Warteliste für den Start findest du auf der Cornnector-Seite.',
    'cta_button': 'Zur Cornnector-Seite',
    'cta_url': '',  # TODO: Adresse der Cornnector-Seite eintragen (z. B. 'https://cornnector.de/')
    'cta_note': 'Bald im App Store und bei Google Play.',
    'contact_h2': 'Fragen zur **App?**',
}

# Die drei Funktionen (Zickzack auf der App-Seite). Screenshots aus der Cornnector-App (1179 × 2556).
APP_FEATURES = [
    {'icon': 'cn-hub', 'title': 'Hub', 'claim': 'wer heute dran ist.', 'lead': 'Der Hub zeigt jeden Tag, welche Tiere gefüttert werden müssen, wer in der Häutung ist und wann das nächste Gelege schlüpft.',
     'paras': ['Gefüttert wird direkt aus der Liste: Ein Wisch nach links trägt die Fütterung ein, ein Wisch nach rechts markiert die Häutung. Mit QR-Etiketten am Terrarium geht die Fütterungsrunde per Scan noch schneller.'],
     'points': ['Fällige Fütterungen auf einen Blick', 'Fütterungsrunde per QR-Code', 'Häutung pausiert die Fütterung automatisch'],
     'screenshot': 'img/app/hub.png', 'demo': 'swipe'},  # demo = animierte Geste im Kachel-Phone
    {'icon': 'cn-incubator', 'title': 'Zucht', 'claim': 'von der Verpaarung bis zum Schlupf.', 'lead': 'Jede Verpaarung wird einzeln festgehalten, auch mit externen Tieren.',
     'paras': ['Das Gelege übernimmt Vater und Verpaarungsdatum, der Inkubator zeigt die Schlupfprognose aus den bisherigen Gelegen der Mutter. Beim Schlupf entstehen die Nachzuchten direkt mit Eltern und Geschwistern im Stammbaum.'],
     'points': ['Verpaarungen im Verlauf beider Tiere', 'Schlupfprognose und Zuchtbilanz inklusive Slugs', 'Stammbaum über Generationen'],
     'screenshot': 'img/app/zucht.png', 'demo': 'menu'},
    {'icon': 'cn-calculator', 'title': 'Genetikrechner', 'claim': 'Verpaarungen durchspielen.', 'lead': 'Mit deinen Tieren oder mit jeder Genetik, die du eintippst.',
     'paras': ['Kombis wie Shatter oder Ultramel zerlegt der Rechner in ihre Gene, Allele wie Motley und Stripe werden richtig gerechnet. Das Ergebnis siehst du als Prozent, Bruch und erwartete Anzahl pro Gelege.'],
     'points': ['Mehr als 150 Gene, Linien und Kombis', 'het und possible het', 'Erwartete Nachzucht pro Gelege'],
     'screenshot': 'img/app/rechner.png', 'demo': 'calc'},
]
APP_SCREENSHOT_HOME = 'img/app/hub.png'  # Screenshot im Smartphone-Mockup auf der Startseite

# Texte in den animierten App-Screens (Kacheln auf der App-Seite)
APP_DEMO = {
    'date': 'Dienstag, 3. November', 'greeting': 'Guten Morgen, Tom!',
    'due': 'Fällig', 'feedings': 'Fütterungen', 'pause': 'Pause', 'shed': 'Häutung', 'hatch': 'Schlupf', 'days': 'Tage',
    'incubator': 'Inkubator', 'clutches': '1 Gelege', 'day': 'Tag 56 / 67', 'hatch_eta': 'Schlupf ca. 14. Nov. · in 11 T',
    'feed_today': 'Heute füttern', 'animals_3': '3 Tiere', 'feeding': 'Fütterung', 'long_press': 'lange drücken: Menü', 'in_shed': 'In Häutung',
    'search': 'Name, Genetik, Züchter …', 'all': 'Alle', 'animals_24': '24 Tiere', 'collection': 'Bestand',
    # Tiermenü (Reihenfolge fest: Häutung, Fütterung, In Häutung, Gewicht, Foto, Abstammung, QR, Verpaart, Rechner)
    'menu': ['Häutung eintragen', 'Fütterung eintragen', 'In Häutung markieren', 'Gewicht eintragen', 'Foto aufnehmen',
             'Abstammung zeigen', 'QR-Etikett', 'Verpaart mit …', 'Im Rechner verpaaren'],
    'sire': 'Vater', 'dam': 'Mutter', 'from_collection': 'Aus Bestand', 'genes_hint': 'z. B. Shatter, het Anery, 66% het Hypo',
    'pct': '25 %', 'count': '≈ 3,0', 'offspring': 'Erwartete Nachzucht', 'phenotypes': '4 Phänotypen', 'clutch_size': 'Gelegegröße',
    'genetics': 'Genetik', 'calculator': 'Genetikrechner',
}

# ============================================================================
# KONTAKT
# ============================================================================

KONTAKT = {
    'title': 'Kontakt',
    'description': 'Kontakt zu Bleeding Edge Corns – Fragen zu Nachzuchten, Projekten oder Haltung.',
    'eyebrow': 'Kontakt',
    'h1': 'Fragen, Interesse oder **Anmerkungen?**',
    'text': 'Schreib uns – wir melden uns schnellstmöglich.',
    # Formular
    'topic_label': 'Worum geht es?',
    'name_label': 'Name *',
    'name_placeholder': 'Vor- und Nachname',
    'email_label': 'E-Mail *',
    'email_placeholder': 'name@beispiel.de',
    'animal_label': 'Tier-ID',            # nur beim Thema „Nachzucht“
    'animal_hint': 'optional, z. B. NZ-2026-039',
    'animal_placeholder': 'NZ-2026-',
    'msg_label': 'Nachricht *',
    'msg_placeholder': 'Deine Nachricht an uns',
    'consent': 'Ich bin mit der Verarbeitung meiner Angaben zur Beantwortung meiner Anfrage einverstanden. Mehr dazu in der [Datenschutzerklärung](datenschutz/). *',
    'required_note': '* Pflichtfelder',
    'submit': 'Nachricht senden',
    # Fehlermeldungen
    'err_name': 'Bitte gib deinen Namen ein.',
    'err_email_empty': 'Bitte gib deine E-Mail-Adresse ein.',
    'err_email_invalid': 'Bitte gib eine gültige E-Mail-Adresse ein.',
    'err_msg': 'Bitte schreib uns eine Nachricht.',
    'err_consent': 'Bitte stimme der Verarbeitung deiner Angaben zu.',
    'err_send': 'Die Nachricht konnte leider nicht gesendet werden. Bitte versuch es später noch einmal oder schreib uns direkt an {email}.',
    # Nach dem Absenden
    'success_h2': 'Danke für deine **Nachricht.**',
    'success_text': 'Wir melden uns schnellstmöglich bei dir.',
    'success_button': 'Weitere Nachricht senden',
}

# Kontaktinfos links: (Icon, Beschriftung, Text, Link oder '')
CONTACT_INFO = [
    ('mail', 'E-Mail', EMAIL, 'mailto:' + EMAIL),
    ('map-pin', 'Übergabe', 'Persönlich in Bielefeld oder auf der Terraristika Hamm', ''),
    ('store', 'Nachzuchten', 'Alle verfügbaren Tiere auf MorphMarket', MORPHMARKET_SHOP),
]
CONTACT_TOPICS = ['Nachzucht', 'Projekte', 'Haltung', 'Sonstiges']

# ============================================================================
# IMPRESSUM + DATENSCHUTZ
# ============================================================================

LEGAL = {
    'eyebrow': 'Rechtliches',
    'toc': 'Inhalt',
}

# Zeilen mit "|" = Adressblock, "> " = Hinweis, "- " = Liste. RECHTLICH PRÜFEN LASSEN.
# Abschnitt "Google Fonts" ist entfallen: Roboto wird lokal ausgeliefert (src/fonts).
IMPRESSUM = {'title': 'Impressum', 'stand': 'Stand: November 2026', 'body': """## Angaben gemäß § 5 DDG
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld|Deutschland
## Kontakt
E-Mail: hey@bleeding-edge-corns.com
## Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld
## Hinweis zur Hobbyzucht
Bleeding Edge Corns ist eine private, nicht gewerbliche Hobbyzucht von Kornnattern. Diese Website dient ausschließlich der Information über unsere Tiere und Zuchtprojekte.
## Haftung für Inhalte
Die Inhalte dieser Website wurden mit größter Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Die Angaben zur Haltung von Kornnattern ersetzen keine individuelle Beratung.
## Haftung für Links
Diese Website enthält Links zu externen Websites, insbesondere zu MorphMarket. Auf deren Inhalte haben wir keinen Einfluss. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber verantwortlich. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.
## Urheberrecht
Die Texte und Fotos auf dieser Website unterliegen dem deutschen Urheberrecht. Eine Vervielfältigung oder Verwendung ist ohne ausdrückliche Zustimmung nicht gestattet."""}

DATENSCHUTZ = {'title': 'Datenschutz', 'stand': 'Stand: November 2026', 'body': """## 1. Verantwortlicher
Verantwortlich für die Verarbeitung personenbezogener Daten auf dieser Website ist:
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld|Deutschland|E-Mail: hey@bleeding-edge-corns.com
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
Hosting-Anbieter:|Mittwald CM Service GmbH & Co. KG|Königsberger Straße 4–6|32339 Espelkamp|Deutschland
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
## 6. Links zu MorphMarket
Die Fotos unserer Nachzuchten liegen auf unserem eigenen Webserver. Beim Aufruf der Seiten werden keine Daten an MorphMarket übermittelt.
Klickst du auf eine Nachzucht oder einen MorphMarket-Button, wirst du auf die Website von MorphMarket weitergeleitet. Erst dann werden Daten an MorphMarket übertragen, und es gelten die Datenschutzbestimmungen von MorphMarket.
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
