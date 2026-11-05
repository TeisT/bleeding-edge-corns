# ENGLISH TEXTS – same structure as content.py (all keys must exist there and here).
# Rebuild after a change:  python3 build.py
#
# Same notation as in content.py:
#   **bold**, [[no break]], [Link text](page/)
# Internal links use the GERMAN page paths (e.g. kornnatter/, datenschutz/) –
# build.py turns them into the English pages under /en/ (corn-snake/, privacy/ …).
#
# Words in the gallery CSV (data/galerie.csv) and morph names stay as they are.

from content import MORPHMARKET_SHOP, EMAIL, SOCIALS, GALLERY_CATS

# ============================================================================
# GENERAL (all pages)
# ============================================================================

NAV = [
    # (key, label, German path – build.py translates it)
    ('projekte', 'Projects', 'projekte/'),
    ('nachzuchten', 'Hatchlings', 'nachzuchten/'),
    ('kornnatter', 'Corn snake', 'kornnatter/'),
    ('app', 'App', 'app/'),
    ('kontakt', 'Contact', 'kontakt/'),
]

SITE = {
    'name': 'Bleeding Edge Corns',
    'footer_text': 'A small, private hobby breeding from Bielefeld, Germany – with a soft spot for pied-sided corn snakes.',
    'copyright': '© 2026 Bleeding Edge Corns',
    'impressum': 'Legal notice',
    'datenschutz': 'Privacy',
    'mm_button': 'Hatchlings',
    'logo_alt': 'Bleeding Edge Corns',
    'home_label': 'Bleeding Edge Corns – home',
    'menu': 'Menu',
    'menu_close': 'Close menu',
    'lang_label': 'Choose language',
    'prev': 'Back',
    'next': 'Next',
    'nav_main': 'Main navigation',
    'nav_mobile': 'Mobile navigation',
    'nav_footer': 'Footer navigation',
    'mm_logo_alt': 'MorphMarket',
}

CONTACT_TEASER = {
    'eyebrow': 'Contact',
    'text': 'Write to us – we’ll get back to you as soon as we can.',
    'button': 'Get in touch',
}

ANIMAL_SLIDER = {
    'heading': 'Just a small selection – **you’ll find all animals on MorphMarket.**',
    'card_link': 'View on MorphMarket',
    'female': 'Female',
    'male': 'Male',
    'unknown': 'Unsexed',
    'all_eyebrow': 'That was just a small selection',
    'all_title': 'See all **hatchlings**',
    'all_text': 'The complete, current stock with genetics and prices.',
    'all_pill': 'MorphMarket',
    'all_button': 'All hatchlings',
    'bar_label': 'Scroll slider',
}

# ============================================================================
# HOME
# ============================================================================

HOME = {
    'title': 'Home',
    'description': 'Bleeding Edge Corns – private corn snake hobby breeding from Bielefeld, Germany, focused on pied-sided, motley and striped.',
    'hero_eyebrow_before': "We're in",
    'hero_eyebrow_after': 'with pieds',
    'hero_eyebrow_label': "We're in love with pieds",
    'hero_h1': '**[[Bleeding Edge]] Corns:** corn snakes from Bielefeld',
    'hero_text': 'Our passion is pied-sided corn snakes and the fascinating pattern morphs motley & stripe.',
    'hero_button_1': 'Hatchlings',
    'hero_button_2': 'Projects',
    'hero_img_alt': 'Pied-sided corn snake',
    'projects_eyebrow': 'Projects',
    'projects_h2': 'Our **breeding projects**',
    'projects_link': 'To the project',
    'gallery_eyebrow': 'Gallery',
    'gallery_h2': 'A look into **our breeding**',
    'gallery_filter_label': 'Filter gallery',
    'gallery_bar_label': 'Scroll gallery',
    'about_eyebrow': 'About us',
    'about_h2': 'Who’s behind **Bleeding Edge Corns**',
    'about_lead': 'Hi! I’m Torben – the person behind Bleeding Edge Corns.',
    'about_paras': [
        'I’ve kept reptiles since 2007, and pied-sided corn snakes have fascinated me for many years. Over time, all kinds of snakes have been part of my life. Many species came and went – the corn snakes stayed.',
        'Today I’m a dad of two boys and still work with a small group of selected animals as a hobby. My wish: to get many more people excited about these amazing animals.',
    ],
    'about_link': 'Got questions? Feel free to send me a message →',
    'about_img_alt': 'Torben with a corn snake',
    'app_eyebrow': 'Our app',
    'app_h2': 'Your snakes. **Connected in Cornnector.**',
    'app_free': 'Free for iPhone and Android.',
    'app_link': 'More about the app',
    'contact_h2': 'Questions, interest or **comments?**',
}

TRUST = [
    ('egg', 'Our own hatchlings', 'Every animal hatches with us in Bielefeld.'),
    ('cn-lineage', 'Documented lineage', 'Fully traceable with Cornnector, our own app.'),
    ('store', 'Store on MorphMarket', 'All available animals with genetics and prices.'),
    ('map-pin', 'Pickup in Bielefeld & Hamm', 'In person or at the Terraristika reptile show in Hamm.'),
]

GALLERY_ALL = 'All'
GALLERY_LABELS = {'Andere Tiere': 'Other animals'}

APP_POINTS = [
    ('cn-hub', 'Hub', 'Due feedings, sheds and clutches at a glance.'),
    ('cn-collection', 'Collection', 'Every animal with photo, genetics and history.'),
    ('cn-incubator', 'Incubator', 'Clutches and hatch forecast at a glance.'),
    ('cn-lineage', 'Lineage', 'Parents, siblings and offspring linked.'),
    ('cn-calculator', 'Genetics calculator', 'Play through pairings before they happen.'),
]

# ============================================================================
# PROJECTS + PROJECT DETAIL PAGES
# ============================================================================

PROJEKTE = {
    'title': 'Projects',
    'description': 'Our breeding projects: Hypo Diffused High Pieds, Diffused Motley & Striped Pieds and Vanishing Motley & Striped.',
    'eyebrow': 'Projects',
    'h1': 'Our **breeding projects**',
    'intro': 'We work on a few clearly defined projects. Each one has its own breeding goal on a pied-sided base – combined with hypo, diffused, motley and striped.',
    'project_label': 'Project',
    'genes_label': 'Genetics',
    'button': 'Project details',
    'contact_h2': 'Questions about a **project?**',
}

PROJEKT_DETAIL = {
    'description': 'Breeding project {title} – {teaser}',
    'breadcrumb': 'Projects',
    'breadcrumb_label': 'Breadcrumb',
    'gallery_eyebrow': 'Gallery',
    'gallery_h2': 'Photos from **this project**',
    'gallery_bar_label': 'Scroll gallery',
    'all_projects': 'All projects',
    'contact_h2': 'Questions, interest or **comments?**',
}

# The three projects. Slugs, images and galleries are taken from content.py,
# only the texts are set here.
from content import PROJECTS as _PROJECTS_DE

_PROJECT_TEXTS = [
    {
        'teaser': 'Low-contrast animals with lots of white on the sides and glowing red.',
        'list_lead': 'Our main focus is developing high-quality hypo diffused high pied corn snakes.',
        'list_paras': ['It’s not only about exceptional animals – above all it’s about health, quality and traceable genetics.'],
        'genes': ['Hypo', 'Diffused', 'Pied Sided', 'Charcoal'],
        'goal_label': 'Breeding goal',
        'goal': 'Combine the intense red base colour of the diffused line with as much pied-sided white as possible.',
        'detail_lead': 'Our goal is to develop corn snakes that combine strong red colouring with as much pied-sided white as possible.',
        'detail_body': [
            'What matters most to us are clear contrasts, harmonious patterns and consistently high quality over several generations.',
            'Every pairing is carefully planned and documented. We don’t just look at the visible traits but also at the genetics of the parents. This produces hatchlings with traceable lineage and the most stable inheritance possible. For us, successful breeding doesn’t mean producing as many animals as possible, but developing each generation with purpose.',
        ],
    },
    {
        'teaser': 'Diffused with motley and stripe patterns on a pied-sided base.',
        'list_lead': 'In this project we combine our high pied lines with the pattern traits motley and striped.',
        'list_paras': [],
        'genes': ['Diffused', 'Pied Sided', 'Charcoal', 'Motley', 'Striped'],
        'goal_label': 'Breeding goal',
        'goal': 'Combine different patterns with intense colours and lots of white to build new lines with character.',
        'detail_lead': 'By combining the motley and striped genes, we want to develop animals that stand out not only for their colours but also for their exceptional patterns.',
        'detail_body': [
            '## The open question of this project',
            'A special focus of this project is an observation that has kept us busy since 2011. While the desired genetics are passed on reliably, the pied-sided pattern often seems to be much weaker in combination with motley or striped than in classic pieds.',
            'Whether these pattern genes really affect how the white side areas develop, or whether other genetic factors are responsible, is still unclear. In the long run we want to better understand how these genes influence each other – and whether stable high pied lines can be developed despite motley or striped.',
        ],
    },
    {
        'teaser': 'A pattern that almost completely fades away.',
        'list_lead': 'A single hatchling started a project we never planned.',
        'list_paras': ['An unusual change in its pattern caught our attention right away. Since then we’ve followed this animal’s development with special interest and want to find out whether a new genetic trait is behind it.'],
        'genes': ['Motley', 'Striped', 'Vanishing (unconfirmed)'],
        'goal_label': 'Open question',
        'goal': 'Is the trait heritable? Then a completely new breeding line could come out of it.',
        'detail_lead': '',
        'detail_body': [
            'Some projects don’t start with a plan but by chance. In one clutch we noticed a hatchling whose pattern was clearly different from all its siblings. With every shed its look keeps changing: the pattern fades more and more, and the animal looks more unique each time.',
            'Whether this is a new genetic mutation, a rare combination of existing genes or simply an exceptional one-off can’t be said for sure yet. That’s exactly what makes this project so exciting. We document its development carefully and will keep watching the animal over the coming years. If the trait turns out to be heritable, a completely new breeding line could come out of it.',
        ],
    },
]
PROJECTS = [{**de, **en} for de, en in zip(_PROJECTS_DE, _PROJECT_TEXTS)]

# ============================================================================
# HATCHLINGS
# ============================================================================

NACHZUCHTEN = {
    'title': 'Hatchlings',
    'description': 'Current corn snake hatchlings from Bleeding Edge Corns – all available animals on MorphMarket.',
    'eyebrow': 'Hatchlings',
    'h1': 'Current **hatchlings**',
    'intro': 'Here you’ll see a small selection. You’ll find all available hatchlings on MorphMarket.',
    'button': 'All hatchlings',
    'steps_eyebrow': 'How to get your animal',
    'faq_eyebrow': 'FAQ',
    'faq_h2': 'Frequently asked **questions**',
    'faq_text': 'For a short overview of care, see our page [Corn snake](kornnatter/).',
    'contact_h2': 'Questions, interest or **comments?**',
}

STEPS = [
    ('search', 'Pick an animal on MorphMarket', 'All available animals with photos, genetics and price.'),
    ('send', 'Send a request', 'Directly via MorphMarket or our contact form.'),
    ('calendar-check', 'Set a date', 'Together we agree on a handover date that suits you.'),
    ('handshake', 'Pickup in Bielefeld or handover at the Terraristika Hamm', 'In person – including feeding history and lineage.'),
]

FAQ = [
    ('Age at handover', 'We only hand over our animals once they have eaten at least five meals on their own – usually at 8 to 10 weeks.'),
    ('Feeding at handover', 'You’ll know exactly what was fed and when. We also tell you how many times your animal has already shed.'),
    ('Shipping', 'In Germany, shipping animals is hardly possible for private breeders anymore – it now requires a registered animal-related business. If you organise transport through such a provider, we’re happy to help: we have heat packs and styrofoam boxes in stock. Alternatively, we hand over your animal in person in Bielefeld or at the Terraristika Hamm.'),
    ('Reservation', 'We’re happy to reserve an animal for you for 5 days – with no obligation. Since sadly many reserved animals were never picked up in recent years, we ask for a small deposit for longer periods, usually 25 to 50 €. You simply pay the rest at the handover.'),
    ('Returns', 'Every animal leaves us healthy, feeding well and with documented origin. To protect our collection, however, we can’t take back animals once they’ve left.'),
    ('Deposit', 'A deposit is binding and is fully credited towards the price at the handover. If you change your mind later, it stays with us – unless agreed otherwise. Should we ever be unable to hand over an animal as promised, we will of course refund the deposit in full.'),
]

# ============================================================================
# CORN SNAKE
# ============================================================================

KORNNATTER = {
    'title': 'Corn snake',
    'description': 'The corn snake (Pantherophis guttatus) in brief: care, feeding, brumation, genetics, breeding and FAQ.',
    'eyebrow': 'In brief',
    'h1': 'The corn snake – **Pantherophis guttatus**',
    'lead': 'The corn snake is one of the most popular snakes in the hobby – and for good reason. It wins people over with its calm nature, its impressive range of colours and comparatively easy care. Still, every keeper is responsible for giving their animal a suitable home for its whole life!',
    'text': 'On this page you’ll find a compact overview of the most important topics around the corn snake.',
    'img_alt': 'Corn snake',
    'topics_eyebrow': 'Topics',
    'topics_h2': 'Everything you **need to know**',
    'fazit_label': 'Summary',
    'close_button': 'Close ↑',
}

STATS = [
    ('thermometer-snowflake', '22–24 °C', 'cool side'),
    ('sun', 'up to 30 °C', 'basking spot'),
    ('droplets', '40–60 %', 'humidity'),
    ('hourglass', '20+ years', 'life expectancy'),
]

TOPICS = [
    {'id': 'haltung', 'title': 'Care', 'glyph': 'house',
     'intro': 'Corn snakes are mostly active at dusk and at night, but during the day they also like to use raised spots and hides. The enclosure should therefore offer enough room to climb, explore and retreat. A varied layout is especially important so the animals feel safe and can live out their natural behaviour.',
     'body': """The basic setup includes several hides, sturdy branches, climbing options, a large enough water bowl and a suitable substrate. A background or extra plants provide more cover and create a natural atmosphere.
## Temperature and climate
Corn snakes regulate their body temperature through their surroundings. That’s why the enclosure should always have a temperature gradient.
- **Warm side:** 27–29 °C
- **Basking spot:** up to about 30 °C
- **Cool side:** 22–24 °C
- **Night temperature:** 20–22 °C
Humidity is usually between 40 and 60 percent. During a shed it may be a little higher for a short time so the skin comes off easily.
## Setup
A well set-up enclosure offers much more than a place to sleep. Different levels, branches, cork tubes and hides encourage natural behaviour and provide security at the same time. Hatchlings in particular benefit from plenty of places to retreat.
## Keeping them alone
Corn snakes are solitary and should always be kept alone outside of planned pairings. Keeping them in groups permanently offers no benefit to the animals and can lead to stress or competition.""",
     'fazit': 'With a large enough enclosure, the right temperatures, a varied setup and regular checks of the conditions, a corn snake can stay healthy for many years. With good care, they often live to over 20 years.'},
    {'id': 'ernaehrung', 'title': 'Feeding', 'glyph': 'utensils',
     'intro': 'A balanced diet is the foundation for healthy, vital corn snakes. As pure carnivores they feed exclusively on small vertebrates. In captivity, frozen and then fully thawed feeder mice have proven themselves. Prey size and feeding intervals should always match the age, size and condition of each animal.',
     'body': """## Suitable prey
The most important prey for corn snakes is the mouse. Depending on the size of the snake, pinkies, hoppers, adult or larger mice are fed. The prey should be roughly as wide as the widest part of the snake’s body. That way it can be digested without problems.
We recommend using frozen prey only. It’s hygienic, easy to store and avoids the risk of injury that live prey can pose.
## Feeding intervals
How often a corn snake should be fed depends mainly on its age and growth. While hatchlings need food regularly, the intervals get much longer for adults.
- **Hatchlings:** about every 5–7 days
- **Juveniles:** about every 7–10 days
- **Adults:** about every 10–14 days
#### Munson Plan Feeding Schedule
The **Munson Plan** is one of the best-known feeding guides for corn snakes and is especially common in the USA. It matches the snake’s body weight to a suitable prey size and a recommended feeding interval, which makes it a helpful guide. Still, every corn snake should be looked at individually, since growth, activity and body condition vary from animal to animal.
- Single pinks (2–3g) every 4 to 5 days for snakes weighing 4–15g.
- Double pinks (3g x 2) every 4 to 5 days for snakes weighing 16–23g.
- Small fuzzies (5–7g) every 5 to 6 days for snakes weighing 24–30g.
- Regular fuzzies (7–9g) every 5 to 6 days for snakes weighing 30–50g.
- Hoppers (9–12g) every 5 to 6 days for snakes weighing 51–90g.
- Weaned mice (14–20g) every 7 days for snakes weighing 91–170g.
- Adult mice (24–30g) every 7+ days for snakes weighing 170g+
Weighing your snake regularly helps you match the amount of food to its individual development.
## Fresh water
Besides feeding, water plays an important role. A large enough water bowl should always be filled with fresh water. Many corn snakes drink regularly and sometimes use the bowl for bathing – especially during a shed.
## Digestion
After a meal, corn snakes need several days to fully digest their food. During this time the animal should not be disturbed or taken out if possible. Rest and the right temperature support smooth digestion and avoid unnecessary stress.""",
     'fazit': 'Adapted feeding, fresh water and enough rest after eating are the foundation for healthy development. If you weigh your animals regularly and adjust the amount of food accordingly, you create the best conditions for a long and healthy corn snake life.'},
    {'id': 'winterruhe', 'title': 'Brumation', 'glyph': 'snowflake',
     'intro': 'Brumation is a natural part of the corn snake’s life cycle. In its native range, temperatures drop significantly during the winter months, so the animals slow down their metabolism and rest for several weeks. In captivity, a controlled brumation can also make sense, especially if the animals will later be used for breeding.',
     'body': """## Why is brumation important?
During brumation the body slows its metabolism down considerably. The animals stop eating and use very little energy. This natural resting phase supports the corn snake’s yearly rhythm and is considered an important part of long-term, species-appropriate care. In breeding animals it also promotes readiness to breed in spring.
## Preparation
A successful brumation starts a few weeks in advance. Feeding is stopped in good time so the digestive tract is completely empty before cooling down. Then the lighting hours and temperatures are reduced step by step. A slow transition avoids unnecessary stress and gives the metabolism time to adjust.
## During brumation
During brumation, corn snakes are usually kept at temperatures between 10 and 15 °C for eight to twelve weeks. They get no food during this time, but fresh water must always be available. Regular visual checks are enough to keep an eye on their health without disturbing them unnecessarily.
## Warming up
After brumation, temperature and lighting hours are raised slowly again. Only once the animals have been active for a few days and have reached their normal body temperature do they get their first meal. A gradual transition makes it easier for the body to return to its normal metabolism.""",
     'fazit': 'A carefully prepared and controlled brumation follows the corn snake’s natural yearly rhythm. It supports the animals’ well-being and is the basis for successful reproduction in many breeding projects. What matters are healthy animals, a slow transition and regular checks throughout the whole resting phase.'},
    {'id': 'genetik', 'title': 'Genetics & morphs', 'glyph': 'dna',
     'intro': 'Its enormous variety of colours and patterns makes the corn snake one of the most fascinating snake species in the hobby. Through natural mutations and targeted pairings, countless colour and pattern variants – called morphs – have appeared over the years. Every combination gives the animals their own look and keeps opening up new possibilities for responsible breeding projects.',
     'body': """## What are morphs?
A morph is a genetically determined colour or pattern variant of a corn snake. While wild-type animals mostly show reddish-brown and orange tones with dark saddles, morphs can produce almost entirely red, grey, yellow or high-contrast looks. Many of these traits can be combined, creating an impressive variety.
## Genetics made simple
Every hatchling gets part of its genes from the mother and part from the father. Which traits become visible later depends on which genes both parents pass on. Some traits show up with just one inherited gene, others only become visible when both parents pass on the trait.
That’s why breeders distinguish between visible traits and genetic traits that are present but can’t be seen from the outside. Careful documentation of lineage is therefore the foundation of all responsible breeding.
> **“het”** stands for heterozygous. The animal carries a gene that doesn’t have to be visible but can be passed on to its offspring.
## Our focus
Our breeding focuses especially on the morphs **Hypo**, **Diffused (Bloodred)** and **Pied Sided**. We also work with other traits such as **Motley** and **Striped** to build lines with character and traceable genetics in the long run.
## Responsible breeding
Exceptional colours alone don’t make a good hatchling. Health, vitality and traceable origin come first for us. Every pairing is carefully planned and documented so that the genetics of our animals can be preserved and developed sensibly over the long term.""",
     'fazit': 'Corn snake genetics opens up almost endless possibilities and makes every hatchling unique. At the same time it takes knowledge, patience and responsibility. Only careful selection of the parents and complete documentation lead to healthy animals with traceable genetic origin.'},
    {'id': 'zucht', 'title': 'Breeding', 'glyph': 'egg',
     'intro': 'Breeding corn snakes combines expertise, patience and responsibility. The goal of careful breeding is not only to produce exceptional colour and pattern variants, but above all to raise healthy, vital animals. Every pairing should therefore be well planned and built on a traceable genetic basis.',
     'body': """## Choosing breeding animals
Only healthy and sufficiently developed corn snakes should be used for breeding. Besides their appearance, lineage, genetic traits and the animals’ general condition also play an important role. Careful selection helps build stable, healthy breeding lines over the long term.
## Pairing and egg laying
After a successful brumation, breeding season starts in spring. A few weeks later the female usually lays between 10 and 30 eggs, depending on age and condition. To develop successfully, they are then incubated at constant temperatures.
## Incubation
During incubation the eggs need an even temperature and suitable humidity. Even small fluctuations can affect their development. Depending on the incubation temperature, the hatchlings usually emerge after about 55 to 70 days.
## Our incubation
> We incubate our eggs at a constant temperature of **27.5 °C**. Under these conditions the hatchlings usually emerge after about **65 days**. Depending on the clutch and development, the hatch date can vary by a few days.
## Raising hatchlings
After hatching, the young first stay in their rearing boxes and shed for the first time. Only then do they get their first meal. Over the following months, growth, weight and sheds are documented regularly to follow each animal’s development closely.
## Our philosophy
For us, breeding means much more than multiplying corn snakes. Health, traceable genetics and careful documentation are at the heart of every pairing. Our goal is to raise animals with character and to develop each generation deliberately – quality matters more than quantity.""",
     'fazit': 'Responsible corn snake breeding takes time, experience and patience. If you choose your animals carefully, document their development and always put their well-being first, you lay the foundation for healthy hatchlings and successful breeding projects in the long run.'},
    {'id': 'faq', 'title': 'FAQ', 'glyph': 'circle-help', 'intro': '', 'fazit': '',
     'body': """## Are corn snakes suitable for beginners?
Yes. Thanks to their calm nature and comparatively easy care, corn snakes are one of the most popular snake species for beginners. Still, you should learn about their needs thoroughly before getting one and keep the long-term responsibility in mind.
## How long do corn snakes live?
With proper care, corn snakes often live to 20 years or more. A balanced diet, suitable conditions and regular checks contribute a lot to a long and healthy life.
## How big do corn snakes get?
Adult corn snakes usually reach a length of 100 to 150 centimetres. Size and weight can vary a little depending on origin and individual development.
## Are corn snakes venomous?
No. Corn snakes are non-venomous constrictors. They kill their prey by wrapping around it and pose no danger to humans.
## Do corn snakes have to be kept alone?
Yes. Corn snakes are solitary and should always be kept alone outside of planned pairings. This avoids stress and competition.
## How often does a corn snake need to be fed?
The feeding interval depends on the animal’s age and size. Hatchlings are fed more often than adult corn snakes. You’ll find more details in the “Feeding” section.
## Do corn snakes need brumation?
Brumation follows the animals’ natural yearly rhythm and is recommended especially for breeding animals. For pet animals, keepers handle it differently, and it should be well prepared.
## What does “het” mean?
“Het” is short for “heterozygous”. It means an animal carries a certain gene that doesn’t have to be visible on the outside. It can still pass the trait on to its offspring.
## What does Diffused (Bloodred) mean?
Diffused is a colour mutation that used to be called Bloodred. It reduces the typical dorsal pattern and gives adult animals an especially intense red colour.
## What does Pied Sided mean?
Pied Sided describes a pattern variant with white areas of varying size on the sides of the body. The amount of white can vary a lot from animal to animal and makes every corn snake unique.
## Where can I find your current hatchlings?
We publish our currently available hatchlings on **MorphMarket**.
## Can I contact you with questions?
Of course. If you have questions about our animals, our projects or keeping corn snakes, we’d love to hear from you. Just use our contact form."""},
]

# ============================================================================
# APP (wording follows the English Cornnector guide)
# ============================================================================

APP = {
    'title': 'App',
    'description': 'Cornnector – the app for corn snake keepers and breeders: feeding, sheds, pairings, clutches and genetics in one app. Free for iPhone and Android.',
    'eyebrow': 'Our app',
    'h1': 'Your snakes. **Connected in Cornnector.**',
    'free': 'Free for iPhone and Android.',
    'intro': '**Cornnector** documents feedings, sheds, pairings and clutches – including genetic results. All your information, digital. Right where you need it.',
    'cta_h2': 'All about **Cornnector**',
    'cta_text': 'You’ll find all features, the guide and the waiting list for the launch on the Cornnector page.',
    'cta_button': 'To the Cornnector page',
    'cta_url': '',  # TODO: address of the English Cornnector page
    'cta_note': 'Coming soon to the App Store and Google Play.',
    'contact_h2': 'Questions about the **app?**',
}

from content import APP_FEATURES as _APP_FEATURES_DE

# English app screenshots (from Cornnector-App/screenshots/anleitung/*-en.png)
APP_SCREENSHOT_HOME = 'img/app/en/hub.png'

_APP_FEATURE_TEXTS = [
    {'title': 'Hub', 'claim': 'who’s due today.', 'lead': 'Every day the hub shows which animals need feeding, who is in shed and when the next clutch hatches.',
     'paras': ['Feeding happens right from the list: a swipe left records the feeding, a swipe right marks the shed. With QR labels on the enclosures, the feeding round is even faster with a quick scan.'],
     'points': ['Due feedings at a glance', 'Feeding round via QR code', 'A shed pauses feeding automatically'],
     'screenshot': 'img/app/en/hub.png'},
    {'title': 'Breeding', 'claim': 'from pairing to hatching.', 'lead': 'Every pairing is saved on its own, including external animals.',
     'paras': ['The clutch takes over the sire and pairing date, and the incubator shows the hatch forecast based on the dam’s earlier clutches. When they hatch, the hatchlings are created right away with parents and siblings in the lineage.'],
     'points': ['Pairings in the history of both animals', 'Hatch forecast and breeding record including slugs', 'Lineage across generations'],
     'screenshot': 'img/app/en/zucht.png'},
    {'title': 'Genetics calculator', 'claim': 'play through pairings.', 'lead': 'With your own animals or any genetics you type in.',
     'paras': ['The calculator breaks combos like Shatter or Ultramel down into their genes, and alleles like motley and stripe are calculated correctly. You see the result as percentage, fraction and expected count per clutch.'],
     'points': ['More than 150 genes, lines and combos', 'het and possible het', 'Expected offspring per clutch'],
     'screenshot': 'img/app/en/rechner.png'},
]
APP_FEATURES = [{**de, **en} for de, en in zip(_APP_FEATURES_DE, _APP_FEATURE_TEXTS)]

# Texts in the animated app screens (same order and keys as in content.py)
APP_DEMO = {
    'date': 'Tuesday, November 3', 'greeting': 'Good morning, Tom!',
    'due': 'Due', 'feedings': 'feedings', 'pause': 'Pause', 'shed': 'shed', 'hatch': 'Hatch', 'days': 'days',
    'incubator': 'Incubator', 'clutches': '1 clutch', 'day': 'Day 56 / 67', 'hatch_eta': 'Hatch approx. Nov 14 · in 11 d',
    'feed_today': 'Feed today', 'animals_3': '3 animals', 'feeding': 'Feeding', 'long_press': 'long press: menu', 'in_shed': 'In shed',
    'search': 'Name, genetics, breeder …', 'all': 'All', 'animals_24': '24 animals', 'collection': 'Collection',
    'menu': ['Record shed', 'Record feeding', 'Mark as in shed', 'Add weight', 'Take photo',
             'Show lineage', 'QR label', 'Paired with …', 'Pair in calculator'],
    'sire': 'Sire', 'dam': 'Dam', 'from_collection': 'From collection', 'genes_hint': 'e.g. Shatter, het Anery, 66% het Hypo',
    'pct': '25%', 'count': '≈ 3.0', 'offspring': 'Expected offspring', 'phenotypes': '4 phenotypes', 'clutch_size': 'Clutch size',
    'genetics': 'Genetics', 'calculator': 'Genetics calculator',
}

# ============================================================================
# CONTACT
# ============================================================================

KONTAKT = {
    'title': 'Contact',
    'description': 'Contact Bleeding Edge Corns – questions about hatchlings, projects or care.',
    'eyebrow': 'Contact',
    'h1': 'Questions, interest or **comments?**',
    'text': 'Write to us – we’ll get back to you as soon as we can.',
    'topic_label': 'What is it about?',
    'name_label': 'Name *',
    'name_placeholder': 'First and last name',
    'email_label': 'Email *',
    'email_placeholder': 'name@example.com',
    'animal_label': 'Animal ID',
    'animal_hint': 'optional, e.g. NZ-2026-039',
    'animal_placeholder': 'NZ-2026-',
    'msg_label': 'Message *',
    'msg_placeholder': 'Your message to us',
    'consent': 'I agree that my details will be processed to answer my request. More in the [privacy policy](datenschutz/). *',
    'required_note': '* Required',
    'submit': 'Send message',
    'err_name': 'Please enter your name.',
    'err_email_empty': 'Please enter your email address.',
    'err_email_invalid': 'Please enter a valid email address.',
    'err_msg': 'Please write us a message.',
    'err_consent': 'Please agree to the processing of your details.',
    'err_send': 'Sorry, your message couldn’t be sent. Please try again later or write to us directly at {email}.',
    'success_h2': 'Thanks for your **message.**',
    'success_text': 'We’ll get back to you as soon as we can.',
    'success_button': 'Send another message',
}

CONTACT_INFO = [
    ('mail', 'Email', EMAIL, 'mailto:' + EMAIL),
    ('map-pin', 'Handover', 'In person in Bielefeld or at the Terraristika Hamm', ''),
    ('store', 'Hatchlings', 'All available animals on MorphMarket', MORPHMARKET_SHOP),
]
# Labels only – same order as CONTACT_TOPICS in content.py (the form sends the German value)
CONTACT_TOPICS = ['Hatchling', 'Projects', 'Care', 'Other']

# ============================================================================
# LEGAL NOTICE + PRIVACY POLICY
# ============================================================================
# Translation of the German texts in content.py. Keep both in sync. HAVE THEM CHECKED LEGALLY.

LEGAL = {
    'eyebrow': 'Legal',
    'toc': 'Contents',
}

IMPRESSUM = {'title': 'Legal notice', 'stand': 'As of: November 2026', 'body': """> This is a translation for your convenience. Only the German version is legally binding.
## Information according to § 5 DDG
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld|Germany
## Contact
Email: hey@bleeding-edge-corns.com
## Responsible for content according to § 18 (2) MStV
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld
## Note on hobby breeding
Bleeding Edge Corns is a private, non-commercial hobby breeding of corn snakes. This website serves exclusively to inform about our animals and breeding projects.
## Liability for content
The content of this website was created with the greatest care. However, we cannot guarantee that the content is correct, complete and up to date. The information on keeping corn snakes does not replace individual advice.
## Liability for links
This website contains links to external websites, in particular to MorphMarket. We have no influence on their content. The respective provider or operator is always responsible for the content of the linked pages. If we become aware of any legal violations, we will remove such links immediately.
## Copyright
The texts and photos on this website are subject to German copyright law. Copying or using them without explicit permission is not allowed."""}

DATENSCHUTZ = {'title': 'Privacy policy', 'stand': 'As of: November 2026', 'body': """> This is a translation for your convenience. Only the German version is legally binding.
## 1. Controller
The controller responsible for processing personal data on this website is:
Torben Teismann|Ravensberger Straße 83|33602 Bielefeld|Germany|Email: hey@bleeding-edge-corns.com
## 2. General information
Protecting your personal data is important to us. We treat your personal data confidentially and in accordance with the statutory data protection regulations and this privacy policy.
This website provides information about our private hobby breeding of corn snakes and presents our own hatchlings.
Personal data is only processed on this website to the extent necessary to operate the website or to handle requests.
## 3. Visiting the website
When you visit this website, the web server processes technically necessary information. This may include in particular:
- IP address of the accessing device
- date and time of access
- pages visited
- amount of data transferred
- browser and operating system used
- where applicable, the previously visited page (referrer)
This processing takes place in order to provide the website technically, to ensure the security and stability of the service and to detect technical errors.
The legal basis for this processing is Art. 6 (1) (f) GDPR. Our legitimate interest lies in the secure and reliable operation of the website.
The data is deleted as soon as it is no longer required for the purposes mentioned, unless statutory retention obligations apply.
The specific storage period may depend on the settings and requirements of our web hosting provider.
## 4. Web hosting
This website is operated by an external web hosting provider.
When you visit the website, technically necessary data is transferred to and processed on our hosting provider’s server. This may include in particular the IP address, date and time of access, browser information and the content accessed.
The hosting provider processes this data on our behalf. Where necessary, a data processing agreement in accordance with Art. 28 GDPR is in place with the hosting provider.
Hosting provider:|Mittwald CM Service GmbH & Co. KG|Königsberger Straße 4–6|32339 Espelkamp|Germany
Processing takes place for the purpose of providing this website securely and reliably.
The legal basis is Art. 6 (1) (f) GDPR. Our legitimate interest lies in the technically secure and reliable provision of our website.
## 5. Contact form
Our website offers the option of contacting us via a contact form.
When you use the contact form, the following details are processed:
- name
- email address
- selected topic of the request
- optionally the animal ID of a hatchling
- message or other details in the free text field
Your name and email address are required so that we can handle and answer your request.
The data you submit is used exclusively to handle your request and for the related communication. It is not used for advertising or passed on to third parties unless there is a legal obligation to do so or you have expressly consented.
The legal basis for processing is Art. 6 (1) (f) GDPR. Our legitimate interest lies in being able to answer incoming requests and communicate with you.
If your request is aimed at concluding a contract or initiating a contractual relationship, Art. 6 (1) (b) GDPR may also serve as the legal basis.
The data submitted via the contact form is only stored for as long as necessary to handle the request. Once the request has been fully handled, the data is deleted unless statutory retention obligations or other legal reasons require further storage.
## 6. Links to MorphMarket
The photos of our hatchlings are stored on our own web server. No data is transferred to MorphMarket when you visit our pages.
If you click on a hatchling or a MorphMarket button, you are forwarded to the MorphMarket website. Only then is data transferred to MorphMarket, and MorphMarket’s privacy policy applies.
## 7. No analytics or tracking services
No analytics, tracking or advertising services are currently used on this website.
In particular, we currently use:
- no Google Analytics
- no comparable analytics tools
- no personalised advertising
- no social media tracking
Should such services be used in the future, this privacy policy will be updated accordingly before they are used.
## 8. Cookies
This website currently does not use cookies that analyse usage behaviour or serve advertising purposes.
If technically necessary cookies are used for the technical operation of the website, they serve exclusively to provide the respective function.
## 9. Disclosure of data
Personal data is generally not passed on to third parties.
Data may be passed on where this is necessary for the technical provision of the website, for example to the web hosting provider we have commissioned, or if we are legally obliged to do so.
Personal data is not transferred for advertising purposes.
## 10. Your rights
Within the statutory requirements, you have the following rights regarding your personal data:
- right of access according to Art. 15 GDPR
- right to rectification according to Art. 16 GDPR
- right to erasure according to Art. 17 GDPR
- right to restriction of processing according to Art. 18 GDPR
- right to data portability according to Art. 20 GDPR
- right to object according to Art. 21 GDPR
If the processing of your personal data is based on Art. 6 (1) (f) GDPR, you can object to this processing at any time on grounds relating to your particular situation.
To exercise your rights, you can contact us at any time using the contact details above.
## 11. Right to lodge a complaint with a supervisory authority
If you believe that the processing of your personal data violates the General Data Protection Regulation, you have the right to lodge a complaint with a data protection supervisory authority.
This right exists in particular with the supervisory authority of your habitual residence, your place of work or the place of the alleged violation.
## 12. Updates to this privacy policy
We reserve the right to adapt this privacy policy if the technical setup or functions of this website change or new legal requirements arise."""}
