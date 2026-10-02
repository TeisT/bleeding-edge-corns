#!/usr/bin/env python3
"""Statischer Build für die Website "Bleeding Edge Corns".

Nur Python-Standardbibliothek. Aufrufe:
  python3 build.py                     Teststand: alle Seiten mit noindex (Suchmaschinen gesperrt)
  python3 build.py --live              echte Website: ohne noindex
  python3 build.py --import <csv>      MorphMarket-Export übernehmen (nur benötigte Spalten) und bauen
Erzeugt dist/ (komplett statisch, relative Links → läuft in jedem Unterordner).
Inhalte: content.py, Nachzuchten: data/nachzuchten.csv.
"""
import argparse
import csv
import html
import re
import shutil
from pathlib import Path

import content as C

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
DIST = ROOT / 'dist'
SITE_NAME = 'Bleeding Edge Corns'


# ------------------------------------------------------------------ Helfer
def esc(s):
    return html.escape(s, quote=True)


def md(s):
    """Inline-Markdown: **fett** → <strong>. Text wird escaped."""
    parts = esc(s).split('**')
    return ''.join(f'<strong>{p}</strong>' if i % 2 else p for i, p in enumerate(parts))


_icon_cache = {}


def icon(name, size=24, stroke=1.5, cls=''):
    """Lucide-Icon (src/icons/*.svg) inline, aria-hidden."""
    if name not in _icon_cache:
        svg = (SRC / 'icons' / f'{name}.svg').read_text()
        svg = re.sub(r'<!--.*?-->', '', svg, flags=re.S)
        inner = re.search(r'<svg[^>]*>(.*)</svg>', svg, re.S).group(1)
        _icon_cache[name] = re.sub(r'\s+', ' ', inner).strip()
    c = f'icon {cls}'.strip()
    return (f'<svg class="{c}" xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 24 24" '
            f'fill="none" stroke="currentColor" stroke-width="{stroke}" stroke-linecap="round" stroke-linejoin="round" '
            f'aria-hidden="true" focusable="false">{_icon_cache[name]}</svg>')


def eyebrow(text, cls=''):
    c = f'eyebrow {cls}'.strip()
    return f'<div class="{c}">{esc(text)}</div>'


def dmax(px):
    """Max-Breite nur auf Desktop (≥ 1024 px Containerbreite), darunter volle Breite."""
    return f'style="--dmax:{px}px"'


def reveal(delay=0):
    return f'data-reveal="{delay}"'


class Page:
    def __init__(self, path, depth):
        self.path = path  # z. B. 'projekte/index.html'
        self.root = '../' * depth if depth else './'

    def url(self, p):
        return self.root + p


# ------------------------------------------------------------------ Daten
# Nur diese Spalten des MorphMarket-Exports landen im Projekt (und damit öffentlich auf GitHub).
# Preise, Aufrufzahlen, private Notizen usw. werden beim Import verworfen.
CSV_COLUMNS = ['Animal_Id*', 'Title*', 'Sex', 'State', 'Visibility', 'Enabled', 'Photo_Urls', 'Mm_Url**']


def import_csv(src):
    rows = list(csv.DictReader(open(src, encoding='utf-8-sig')))
    missing = [c for c in CSV_COLUMNS if rows and c not in rows[0]]
    if missing:
        raise SystemExit(f'Spalten fehlen im Export: {", ".join(missing)}')
    with open(ROOT / 'data' / 'nachzuchten.csv', 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)
    print(f'{len(rows)} Zeilen aus {src} übernommen → data/nachzuchten.csv')


def load_animals():
    """Nachzuchten aus dem MorphMarket-Export (nur aktive, öffentliche Inserate)."""
    rows = list(csv.DictReader(open(ROOT / 'data' / 'nachzuchten.csv', encoding='utf-8-sig')))
    out = []
    for r in rows:
        if r.get('State') != 'For Sale' or r.get('Visibility') != 'Public' or r.get('Enabled') != 'Active':
            continue
        aid = r['Animal_Id*'].strip()
        m = re.match(r'^(NZ-\d{4}-)(\d+)$', aid)
        if m:
            aid = m.group(1) + m.group(2).zfill(3)
        title = re.sub(r'\bBlood\b', 'Diffused', r['Title*'].strip())
        sex = r.get('Sex', '').strip().lower()
        sex_label, sex_icon = {'female': ('Weibchen', '♀'), 'male': ('Männchen', '♂')}.get(sex, ('Unbestimmt', ''))
        photos = r.get('Photo_Urls', '').split()
        out.append({'id': aid, 'title': title, 'sex': sex_label, 'sex_icon': sex_icon,
                    'photo': photos[0] if photos else '', 'url': r.get('Mm_Url**', '').strip() or C.MORPHMARKET_SHOP})
    return out


# ------------------------------------------------------------------ Bausteine
def mm_logo(pg, dark=False):
    f = ' mm-logo--dark' if dark else ''
    return f'<img class="mm-logo{f}" src="{pg.url("img/morphmarket-logo-white.svg")}" alt="MorphMarket" width="56" height="21">'


def mm_button(pg, label='Nachzuchten', cls='btn btn-primary', dark_logo=False):
    return (f'<a class="{cls} btn-mm" href="{C.MORPHMARKET_SHOP}" target="_blank" rel="noopener">{esc(label)} '
            f'<span class="nudge" aria-hidden="true">→</span> {mm_logo(pg, dark_logo)}</a>')


def header(pg, active):
    proj_sub = ''.join(f'<a class="subnav-link" href="{pg.url("projekte/" + p["slug"] + "/")}">{esc(p["title"])}</a>' for p in C.PROJECTS)
    items = []
    for key, label, href in C.NAV:
        cur = ' is-active' if key == active else ''
        aria = ' aria-current="page"' if key == active and active != 'projekte-detail' else ''
        if key == 'projekte':
            cur = ' is-active' if active in ('projekte', 'projekte-detail') else ''
            items.append(f'<div class="nav-item has-sub"><a class="nav-link{cur}" href="{pg.url(href)}" aria-haspopup="true"{aria}>{label}'
                         f'<span class="chev">{icon("chevron-right", 14, 1.75)}</span></a>'
                         f'<div class="subnav">{proj_sub}</div></div>')
        else:
            items.append(f'<div class="nav-item"><a class="nav-link{cur}" href="{pg.url(href)}"{aria}>{label}</a></div>')

    m_items = []
    for key, label, href in C.NAV:
        m_items.append(f'<a class="mnav-link" href="{pg.url(href)}">{label}<span aria-hidden="true">→</span></a>')
        if key == 'projekte':
            m_items.append('<div class="mnav-sub">' + ''.join(
                f'<a href="{pg.url("projekte/" + p["slug"] + "/")}">{esc(p["title"])}</a>' for p in C.PROJECTS) + '</div>')
    socials = ''.join(f'<a class="msocial" href="{u}" aria-label="{l}">{icon(i, 18)}</a>' for i, l, u in C.SOCIALS)

    return f'''<header class="site-header">
  <div class="wrap header-bar">
    <a class="logo" href="{pg.url('')}" aria-label="{SITE_NAME} – Startseite"><img src="{pg.url('img/logo.png')}" alt="{SITE_NAME}" width="560" height="400"></a>
    <nav class="main-nav" aria-label="Hauptnavigation">{''.join(items)}</nav>
    <div class="header-right">
      <div class="lang" role="group" aria-label="Sprache wählen"><button type="button" data-lang="de" aria-pressed="true">DE</button><button type="button" data-lang="en" aria-pressed="false">EN</button></div>
      {mm_button(pg, cls='header-cta')}
      <button type="button" class="burger" aria-label="Menü" aria-expanded="false" aria-controls="mobile-menu">{icon('menu', 26, 1.5, 'i-menu')}{icon('x', 26, 1.5, 'i-close')}</button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu" hidden>
    <div class="wrap mobile-menu-inner">
      <nav class="mnav" aria-label="Mobile Navigation">{''.join(m_items)}</nav>
      {mm_button(pg, cls='mmenu-cta')}
      <div class="msocials">{socials}</div>
    </div>
  </div>
</header>'''


def footer(pg):
    socials = ''.join(f'<a class="fsocial" href="{u}" aria-label="{l}">{icon(i, 18)}</a>' for i, l, u in C.SOCIALS)
    nav = ''.join(f'<a href="{pg.url(h)}">{l}</a>' for _, l, h in C.NAV)
    return f'''<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="footer-logo" href="{pg.url('')}" aria-label="{SITE_NAME} – Startseite"><img src="{pg.url('img/logo.png')}" alt="{SITE_NAME}" width="118" height="84"></a>
        <p>Eine kleine, private Hobbyzucht aus Bielefeld – mit einem Herz für Pied-Sided Kornnattern.</p>
        <div class="fsocials">{socials}</div>
      </div>
      <nav class="footer-nav" aria-label="Footer-Navigation">{nav}</nav>
    </div>
    <div class="footer-bottom">
      <span>© 2026 {SITE_NAME}</span>
      <div><a href="{pg.url('impressum/')}">Impressum</a><a href="{pg.url('datenschutz/')}">Datenschutz</a></div>
    </div>
  </div>
</footer>
<div class="mm-dock">{mm_button(pg, cls='mm-dock-btn')}</div>'''


def contact_teaser(pg, h2_html, bg='gray'):
    return f'''<section class="cta-section bg-{bg}" data-screen-label="Kontakt">
  <div class="wrap cta-inner" {reveal(0)}>
    {eyebrow('Kontakt')}
    <h2 class="h2">{h2_html}</h2>
    <p class="cta-text dmax" {dmax(520)}>Schreib uns – wir melden uns schnellstmöglich.</p>
    <a class="btn btn-primary cta-btn" href="{pg.url('kontakt/')}">Kontakt aufnehmen</a>
  </div>
</section>'''


def slider_arrows(theme):
    return (f'<div class="slider-arrows">'
            f'<button type="button" class="arrow arrow--{theme}" data-prev aria-label="Zurück">{icon("arrow-left", 20)}</button>'
            f'<button type="button" class="arrow arrow--{theme}" data-next aria-label="Weiter">{icon("arrow-right", 20)}</button></div>')


def slider_bar(theme, label):
    return (f'<div class="sbar sbar--{theme}" data-bar role="scrollbar" aria-label="{label}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">'
            f'<div class="sbar-track"><div class="sbar-thumb"></div></div></div>')


def animals_slider(pg, animals, theme):
    """Nachzuchten-Slider. theme 'light' (Startseite, #f7f7f7) oder 'dark' (Nachzuchten-Seite)."""
    cards = []
    for a in animals:
        sx = f'<span class="sex-icon" aria-hidden="true">{a["sex_icon"]}</span>' if a['sex_icon'] else '<span class="sex-icon" aria-hidden="true"></span>'
        cards.append(f'''<a class="acard" href="{esc(a["url"])}" target="_blank" rel="noopener">
          <div class="acard-img"><img src="{esc(a["photo"])}" alt="{esc(a["title"])}" loading="lazy" width="600" height="750"></div>
          <div class="acard-body">
            <span class="acard-id">{esc(a["id"])}</span>
            <div class="acard-title">{esc(a["title"])}</div>
            <div class="acard-sex">{sx}{esc(a["sex"])}</div>
            <div class="acard-foot"><span class="link-arrow">Auf MorphMarket ansehen<span aria-hidden="true">→</span></span></div>
          </div>
        </a>''')
    cards.append(f'''<a class="acard-all" href="{C.MORPHMARKET_SHOP}" target="_blank" rel="noopener">
        <div class="acard-all-eyebrow">Dies war nur eine kleine Auswahl</div>
        <div class="acard-all-mid">
          <div class="acard-all-title">Alle <strong>Nachzuchten</strong> ansehen</div>
          <div class="acard-all-text">Der komplette, aktuelle Bestand mit Genetik und Preisen.</div>
        </div>
        <span class="acard-all-pill">MorphMarket <span class="nudge" aria-hidden="true">→</span></span>
      </a>''')
    btn_cls = 'btn btn-primary' if theme == 'light' else 'btn btn-light'
    return f'''<section class="nz-slider nz-slider--{theme}" data-screen-label="Nachzuchten" data-slider>
  <div class="slider-stack">
    <div class="wrap slider-head">
      <h2 class="h2-slider dmax" {dmax(720)}>Nur ein kleiner Ausschnitt – <strong>alle Tiere findest du auf MorphMarket.</strong></h2>
      {slider_arrows('light' if theme == 'light' else 'dark')}
    </div>
    <div class="track" data-track>{''.join(cards)}</div>
    <div class="wrap slider-foot">
      {mm_button(pg, 'Alle Nachzuchten', btn_cls, dark_logo=(theme == 'dark'))}
      {slider_bar('light' if theme == 'light' else 'dark', 'Slider scrollen')}
    </div>
  </div>
</section>'''


def cells(items, padfirst=False, dark=False):
    """Vertrauensleiste / Ablauf: Icon, Titel, Text, Trennlinien zwischen den Spalten."""
    cls = 'cells' + (' cells--padfirst' if padfirst else '')
    out = [f'<div class="cell" {reveal(i * 80)}>{icon(ic, 26)}<div class="cell-title">{esc(t)}</div><div class="cell-text">{esc(d)}</div></div>'
           for i, (ic, t, d) in enumerate(items)]
    return f'<div class="{cls}">{"".join(out)}</div>'


def long_text(body):
    """Mini-Markdown (Kornnatter-Themen)."""
    out, lst = [], None
    for line in body.split('\n'):
        if line.startswith('- '):
            if lst is None:
                lst = []
                out.append(lst)
            lst.append(md(line[2:]))
            continue
        lst = None
        if line.startswith('#### '):
            out.append(f'<h4>{esc(line[5:])}</h4>')
        elif line.startswith('## '):
            out.append(f'<h3>{esc(line[3:])}</h3>')
        elif line.startswith('> '):
            out.append(f'<p class="note">{md(line[2:])}</p>')
        elif line.strip():
            out.append(f'<p>{md(line)}</p>')
    return ''.join(x if isinstance(x, str) else '<ul class="dlist">' + ''.join(f'<li>{i}</li>' for i in x) + '</ul>' for x in out)


def phone(slot_img, cls='phone'):
    img = f'<img src="{slot_img}" alt="" loading="lazy">' if slot_img else ''
    return f'<div class="{cls}"><div class="phone-screen">{img}<div class="phone-notch"></div></div></div>'


# ------------------------------------------------------------------ Layout
NOINDEX = True  # wird mit --live abgeschaltet


def layout(pg, title, description, active, body):
    full_title = f'{SITE_NAME} – {title}'
    robots = '\n<meta name="robots" content="noindex, nofollow">' if NOINDEX else ''
    return f'''<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">{robots}
<link rel="icon" type="image/png" href="{pg.url('img/logo.png')}">
<link rel="preload" href="{pg.url('fonts/roboto-latin-1.woff2')}" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{pg.url('assets/fonts.css')}">
<link rel="stylesheet" href="{pg.url('assets/style.css')}">
<script>document.documentElement.classList.add('js')</script>
<script src="{pg.url('assets/main.js')}" defer></script>
</head>
<body>
<div class="page">
{header(pg, active)}
<main id="inhalt">
{body}
</main>
{footer(pg)}
</div>
</body>
</html>
'''


# ------------------------------------------------------------------ Seiten
def page_home(animals):
    pg = Page('index.html', 0)
    u = pg.url
    proj_cards = ''.join(f'''<a class="pcard" href="{u('projekte/' + p['slug'] + '/')}" {reveal(i * 100)}>
        <div class="pcard-img"><img src="{u(p['img_start'])}" alt="{esc(p['title'])}" loading="lazy" width="606" height="758"></div>
        <div class="pcard-body">
          <h3>{esc(p['title'])}</h3>
          <p>{esc(p['teaser'])}</p>
          <span class="link-arrow">Zum Projekt<span aria-hidden="true">→</span></span>
        </div>
      </a>''' for i, p in enumerate(C.PROJECTS))

    used_cats = {g[4] for g in C.HOME_GALLERY}
    cats = [c for c in C.GALLERY_CATS if c == 'Alle' or c in used_cats]
    tabs = ''.join(f'<button type="button" role="tab" class="tab" aria-selected="{"true" if c == "Alle" else "false"}" data-filter="{esc(c)}">{esc(c)}</button>' for c in cats)
    figs = ''.join(f'''<figure class="gfig" data-cat="{esc(cat)}">
          <div class="gimg" style="aspect-ratio:{w} / {h}"><img src="{u('img/galerie/' + f)}" alt="{esc(label)}" loading="lazy" width="{w}" height="{h}"></div>
          <figcaption><span class="gcap-label">{esc(label)}</span><span class="gcap-cat">{esc(cat)}</span></figcaption>
        </figure>''' for f, w, h, label, cat in C.HOME_GALLERY)

    app_points = ''.join(f'''<div class="apoint" {reveal(120 + i * 80)}>{icon(ic, 26)}<div><div class="apoint-title">{esc(t)}</div><div class="apoint-text">{esc(d)}</div></div></div>'''
                         for i, (ic, t, d) in enumerate(C.APP_POINTS))
    shot = u(C.APP_SCREENSHOT_HOME) if C.APP_SCREENSHOT_HOME else ''

    body = f'''
<section class="hero" data-screen-label="Hero">
  <picture>
    <source media="(max-width: 639.98px)" srcset="{u('img/hero-mobil.jpg')} 1x, {u('img/hero-mobil-2x.jpg')} 2x">
    <source media="(max-width: 1023.98px)" srcset="{u('img/hero-tablet.jpg')} 1x, {u('img/hero-tablet-2x.jpg')} 2x">
    <img class="hero-img" src="{u('img/hero-desktop-wide.jpg')}" srcset="{u('img/hero-desktop-wide.jpg')} 1x, {u('img/hero-desktop-wide-2x.jpg')} 2x" alt="Pied-Sided Kornnatter" fetchpriority="high">
  </picture>
  <div class="wrap hero-wrap">
    <div class="hero-text">
      <div class="hero-eyebrow" {reveal(0)} aria-label="We're in love with pieds"><span>We're in</span>{icon('heart', 14, 1.75)}<span>with pieds</span></div>
      <h1 class="h1 hero-h1" {reveal(80)}><strong><span class="nowrap">Bleeding Edge</span> Corns:</strong> Kornnattern aus Bielefeld</h1>
      <p class="hero-p" {reveal(160)}>Unsere Leidenschaft gilt Pied-Sided Kornnattern und ihren faszinierenden Zeichnungsvarianten Motley &amp; Stripe.</p>
      <div class="hero-btns" {reveal(240)}>
        <a class="btn btn-primary" href="{u('nachzuchten/')}">Nachzuchten</a>
        <a class="btn btn-secondary" href="{u('projekte/')}">Projekte</a>
      </div>
    </div>
  </div>
</section>

<section class="trust" data-screen-label="Vertrauen">
  <div class="wrap">{cells(C.TRUST, padfirst=True)}</div>
</section>

<section class="sec bg-black" data-screen-label="Projekte">
  <div class="wrap stack-64">
    <div {reveal(0)}>
      {eyebrow('Projekte', 'mb18')}
      <h2 class="h2">Unsere <strong>Zuchtprojekte</strong></h2>
    </div>
    <div class="pcards">{proj_cards}</div>
  </div>
</section>

{animals_slider(pg, animals, 'light')}

<section class="sec gallery" data-screen-label="Galerie" data-slider>
  <div class="slider-stack gallery-stack">
    <div class="wrap gallery-head" {reveal(0)}>
      <div class="slider-head">
        <div>
          {eyebrow('Galerie', 'mb18')}
          <h2 class="h2">Einblicke in <strong>unsere Zucht</strong></h2>
        </div>
        {slider_arrows('light')}
      </div>
      <div class="tabs" role="tablist" aria-label="Galerie filtern">{tabs}</div>
    </div>
    <div class="track track--gallery" data-track>{figs}</div>
    <div class="wrap slider-foot slider-foot--end">{slider_bar('light', 'Galerie scrollen')}</div>
  </div>
</section>

<section class="sec bg-gray" data-screen-label="Über uns">
  <div class="wrap grid2 grid-1-1 about">
    <div class="about-img" {reveal(0)}><img src="{u('img/ueber-uns.jpg')}" alt="Torben mit einer Kornnatter" loading="lazy" width="1000" height="1000"></div>
    <div class="about-text dmax" {dmax(500)} {reveal(120)}>
      {eyebrow('Über uns')}
      <h2 class="h2">Wer hinter <strong>Bleeding Edge Corns</strong> steckt</h2>
      <p class="lead-20">Hi! Ich bin Torben – der Kopf hinter Bleeding Edge Corns.</p>
      <p class="body-18">Seit 2007 halte ich Reptilien, und Pied-Sided Kornnattern faszinieren mich schon seit vielen Jahren. Über die Zeit haben mich ganz unterschiedliche Schlangen begleitet. Viele Arten kamen und gingen – die Kornnattern sind geblieben.</p>
      <p class="body-18">Heute bin ich Vater von zwei Jungs und arbeite als Hobby weiterhin mit einer kleinen Gruppe ausgewählter Tiere. Mein Wunsch: noch viele Menschen für diese spannenden Tiere zu begeistern.</p>
      <a class="about-link" href="{u('kontakt/')}">Du hast Fragen? Dann schreib mir gerne eine Nachricht&nbsp;→</a>
    </div>
  </div>
</section>

<section class="sec bg-black app-teaser" data-screen-label="App">
  <div class="wrap grid2 grid-1-115">
    <div class="app-phone-wrap" {reveal(0)}>{phone(shot, 'phone phone--home')}</div>
    <div class="app-teaser-text">
      <div {reveal(80)}>
        {eyebrow('Unsere App', 'mb18')}
        <h2 class="h2">Jedes Tier. <strong>Lückenlos dokumentiert.</strong></h2>
      </div>
      <div class="apoints">{app_points}</div>
      <a class="link-arrow link-arrow--white" href="{u('app/')}" {reveal(200)}>Mehr zur App<span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

{contact_teaser(pg, 'Fragen, Interesse oder <strong>Anmerkungen?</strong>')}
'''
    return pg, layout(pg, 'Startseite', 'Bleeding Edge Corns – private Kornnattern-Hobbyzucht aus Bielefeld mit Schwerpunkt Pied-Sided, Motley und Striped.', 'home', body)


def page_projekte():
    pg = Page('projekte/index.html', 1)
    u = pg.url
    arts = []
    for i, p in enumerate(C.PROJECTS):
        dark = i == 1
        paras = ''.join(f'<p class="body-17">{esc(t)}</p>' for t in p['list_paras'])
        genes = ''.join(f'<span class="gene">{esc(g)}</span>' for g in p['genes'])
        btn = 'btn-light' if dark else 'btn-primary'
        arts.append(f'''<article id="projekt-{i + 1}" class="zz{' zz--dark' if dark else ''}{' zz--flip' if i % 2 else ''}">
      <div class="zz-img ratio-45" {reveal(0)}><img src="{u(p['img_list'])}" alt="{esc(p['title'])}" loading="lazy" width="872" height="1090"></div>
      <div class="zz-text dmax" {dmax(500)} {reveal(120)}>
        {eyebrow(f"Projekt {i + 1}", 'mbm12')}
        <h2 class="h2-zz">{md(p['title_md'])}</h2>
        <p class="lead-18">{esc(p['list_lead'])}</p>
        {paras}
        <div class="genes-block">{eyebrow('Genetik')}<div class="genes">{genes}</div></div>
        <div class="goal">{eyebrow(p['goal_label'])}<div class="goal-text">{esc(p['goal'])}</div></div>
        <a class="btn {btn} btn-arrow" href="{u('projekte/' + p['slug'] + '/')}">Details zum Projekt<span aria-hidden="true">→</span></a>
      </div>
    </article>''')
    body = f'''
<section class="intro-dark" data-screen-label="Projekte Intro">
  <div class="wrap grid2 grid-12-1 align-end gap-96">
    <div class="intro-left" {reveal(0)}>
      {eyebrow('Projekte')}
      <h1 class="h1">Unsere <strong>Zuchtprojekte</strong></h1>
    </div>
    <p class="body-18 c-e2" {reveal(100)}>Wir arbeiten an wenigen, klar definierten Projekten. Jedes verfolgt ein eigenes Zuchtziel auf Pied-Sided-Basis – kombiniert mit Hypo, Diffused, Motley und Striped.</p>
  </div>
</section>

<section class="sec clip-x" data-screen-label="Projekte Zickzack">
  <div class="wrap zz-list">{''.join(arts)}</div>
</section>

{contact_teaser(pg, 'Fragen zu einem <strong>Projekt?</strong>')}
'''
    return pg, layout(pg, 'Projekte', 'Unsere Zuchtprojekte: Hypo Diffused High Pieds, Diffused Motley & Striped Pieds und Vanishing Motley & Striped.', 'projekte', body)


def page_projekt(idx):
    p = C.PROJECTS[idx]
    pg = Page(f'projekte/{p["slug"]}/index.html', 2)
    u = pg.url
    blocks = ''.join(f'<h2 class="h2-24">{esc(t[3:])}</h2>' if t.startswith('## ') else f'<p class="body-17 lh18">{esc(t)}</p>' for t in p['detail_body'])
    lead = f'<p class="lead-20">{esc(p["detail_lead"])}</p>' if p['detail_lead'] else ''
    figs = ''.join(f'''<figure class="gfig">
          <div class="gimg gimg--dark" style="aspect-ratio:{w} / 900"><img src="{u('img/galerie/' + f)}" alt="{esc(cap or p['title'])}" loading="lazy" width="{w}" height="900"></div>
          <figcaption class="gcap-dark">{esc(cap or p['title'])}</figcaption>
        </figure>''' for f, w, cap in p['gallery'])

    def link(i, d):
        q = C.PROJECTS[i]
        lab = f'← Projekt {i + 1}' if d == 'prev' else f'Projekt {i + 1} →'
        return f'<a class="pnav-link pnav-link--{d}" href="{u("projekte/" + q["slug"] + "/")}"><span class="eyebrow">{lab}</span><span class="pnav-title">{esc(q["title"])}</span></a>'

    prev = link(idx - 1, 'prev') if idx > 0 else ''
    nxt = link(idx + 1, 'next') if idx < len(C.PROJECTS) - 1 else ''
    body = f'''
<section class="crumb-sec" data-screen-label="Breadcrumb">
  <div class="wrap"><nav class="crumb" aria-label="Brotkrumen" {reveal(0)}><a href="{u('projekte/')}">Projekte</a><span class="crumb-sep">/</span><span aria-current="page">{esc(p['title'])}</span></nav></div>
</section>

<section class="detail-sec" data-screen-label="Projekt Text">
  <div class="wrap grid2 grid-1-125 align-start">
    <div class="sticky-col" {reveal(0)}>
      {eyebrow(f"Projekt {idx + 1}")}
      <h1 class="h1-60">{md(p['title_md'])}</h1>
    </div>
    <div class="detail-text dmax" {dmax(620)} {reveal(120)}>{lead}{blocks}</div>
  </div>
</section>

<section class="sec-104 bg-black gallery" data-screen-label="Weitere Fotos" data-slider>
  <div class="slider-stack gallery-stack">
    <div class="wrap slider-head" {reveal(0)}>
      <div>
        {eyebrow('Galerie', 'mb18')}
        <h2 class="h2">Fotos aus <strong>diesem Projekt</strong></h2>
      </div>
      {slider_arrows('dark')}
    </div>
    <div class="track track--gallery" data-track>{figs}</div>
    <div class="wrap slider-foot slider-foot--end">{slider_bar('dark', 'Galerie scrollen')}</div>
  </div>
</section>

<section class="pnav-sec" data-screen-label="Projekt Navigation">
  <div class="wrap pnav">
    <div class="pnav-cell">{prev}</div>
    <a class="btn btn-secondary btn-allproj" href="{u('projekte/')}">{icon('layout-grid', 16)}Alle Projekte</a>
    <div class="pnav-cell pnav-cell--next">{nxt}</div>
  </div>
</section>

{contact_teaser(pg, 'Fragen, Interesse oder <strong>Anmerkungen?</strong>')}
'''
    return pg, layout(pg, p['title'], f'Zuchtprojekt {p["title"]} – {p["teaser"]}', 'projekte-detail', body)


def page_nachzuchten(animals):
    pg = Page('nachzuchten/index.html', 1)
    u = pg.url
    faq = ''.join(f'''<div class="faq-item{' is-open' if i == 0 else ''}">
        <button type="button" class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="faq-{i}" id="faq-q-{i}">{esc(q)}{icon('plus', 22, 1.5, 'i-plus')}{icon('minus', 22, 1.5, 'i-minus')}</button>
        <div class="faq-a" id="faq-{i}" role="region" aria-labelledby="faq-q-{i}"{'' if i == 0 else ' hidden'}><p>{esc(a)}</p></div>
      </div>''' for i, (q, a) in enumerate(C.FAQ))
    body = f'''
<section class="nz-intro" data-screen-label="Nachzuchten Intro">
  <div class="wrap grid2 grid-12-1 align-end gap-96">
    <div class="intro-left" {reveal(0)}>
      {eyebrow('Nachzuchten')}
      <h1 class="h1">Aktuelle <strong>Nachzuchten</strong></h1>
    </div>
    <div class="intro-right" {reveal(100)}>
      <p class="body-18">Hier siehst du eine kleine Auswahl. Alle verfügbaren Nachzuchten findest du auf MorphMarket.</p>
      {mm_button(pg, 'Alle Nachzuchten')}
    </div>
  </div>
</section>

{animals_slider(pg, animals, 'dark')}

<section class="steps" data-screen-label="Ablauf">
  <div class="wrap steps-inner">
    <div class="eyebrow" {reveal(0)}>So bekommst du dein Tier</div>
    {cells(C.STEPS)}
  </div>
</section>

<section class="sec bg-gray" data-screen-label="FAQ">
  <div class="wrap grid2 grid-1-16 align-start gap-96">
    <div class="sticky-col" {reveal(0)}>
      {eyebrow('FAQ')}
      <h2 class="h2">Häufige <strong>Fragen</strong></h2>
      <p class="body-16">Einen kurzen Überblick zur Haltung findest du auf unserer Seite <a class="text-link" href="{u('kornnatter/')}">Kornnatter</a>.</p>
    </div>
    <div class="faq" data-faq {reveal(100)}>{faq}</div>
  </div>
</section>

{contact_teaser(pg, 'Fragen, Interesse oder <strong>Anmerkungen?</strong>', 'white')}
'''
    return pg, layout(pg, 'Nachzuchten', 'Aktuelle Kornnattern-Nachzuchten von Bleeding Edge Corns – alle verfügbaren Tiere auf MorphMarket.', 'nachzuchten', body)


def page_kornnatter():
    pg = Page('kornnatter/index.html', 1)
    u = pg.url
    stats = ''.join(f'<div class="stat" {reveal(i * 70)}>{icon(ic, 24)}<div class="stat-v">{esc(v)}</div><div class="stat-l">{esc(l)}</div></div>'
                    for i, (ic, v, l) in enumerate(C.STATS))
    topics = []
    for t in C.TOPICS:
        intro = f'<p class="topic-intro">{esc(t["intro"])}</p>' if t['intro'] else ''
        fazit = f'<div class="fazit">{eyebrow("Fazit")}<p>{esc(t["fazit"])}</p></div>' if t['fazit'] else ''
        topics.append(f'''<div class="topic" data-topic="{t['id']}" id="{t['id']}">
        <button type="button" class="topic-head" aria-expanded="false" aria-controls="panel-{t['id']}">
          {icon(t['glyph'], 24)}<span class="topic-title">{esc(t['title'])}</span>{icon('plus', 24, 1.5, 'i-plus')}{icon('minus', 24, 1.5, 'i-minus')}
        </button>
        <div class="topic-panel" id="panel-{t['id']}" hidden>
          {intro}{long_text(t['body'])}{fazit}
          <div class="topic-close"><button type="button" class="btn-small" data-close>Schließen ↑</button></div>
        </div>
      </div>''')
    body = f'''
<section class="kn-intro" data-screen-label="Kornnatter Intro">
  <div class="wrap grid2 grid-11-1 align-center kn-grid">
    <div class="kn-text">
      <div class="eyebrow" {reveal(0)}>Kurz erklärt</div>
      <h1 class="h1" {reveal(80)}>Die Kornnatter – <strong>Pantherophis guttatus</strong></h1>
      <p class="lead-19" {reveal(160)}>Die Kornnatter gehört zu den beliebtesten Schlangen in der Terraristik – und das aus gutem Grund. Sie überzeugt durch ihr ruhiges Wesen, ihre beeindruckende Farbenvielfalt und eine vergleichsweise unkomplizierte Haltung. Dennoch trägt jeder Halter die Verantwortung, seinem Tier dauerhaft eine artgerechte Umgebung zu bieten!</p>
      <p class="body-17 lh17" {reveal(220)}>Auf dieser Seite findest du einen kompakten Überblick über die wichtigsten Themen rund um die Kornnatter.</p>
    </div>
    <div class="kn-img ratio-45" {reveal(120)}><img src="{u('img/slots/kornnatter-intro.webp')}" alt="Kornnatter" width="835" height="1044"></div>
  </div>
</section>

<section class="stats-sec" data-screen-label="Kennzahlen">
  <div class="wrap stats">{stats}</div>
</section>

<section class="sec" data-screen-label="Themen">
  <div class="wrap stack-64">
    <div {reveal(0)}>
      {eyebrow('Themen', 'mb18')}
      <h2 class="h2">Alles, was du <strong>wissen musst</strong></h2>
    </div>
    <div class="topics" data-topics>{''.join(topics)}</div>
  </div>
</section>
'''
    return pg, layout(pg, 'Kornnatter', 'Die Kornnatter (Pantherophis guttatus) kurz erklärt: Haltung, Ernährung, Winterruhe, Genetik, Zucht und FAQ.', 'kornnatter', body)


def page_app():
    pg = Page('app/index.html', 1)
    u = pg.url
    phones = []
    for i, f in enumerate(C.APP_FEATURES):
        shot = u(f['screenshot']) if f['screenshot'] else ''
        cls = 'app-ph app-ph--mid' if i == 1 else 'app-ph app-ph--side'
        phones.append(f'<div class="{cls}" {reveal(200 + i * 120)}><div class="app-ph-shift">{phone(shot, "phone phone--intro")}</div></div>')
    feats = []
    for i, f in enumerate(C.APP_FEATURES):
        shot = u(f['screenshot']) if f['screenshot'] else ''
        paras = ''.join(f'<p class="body-17">{esc(t)}</p>' for t in f['paras'])
        pts = ''.join(f'<li><span aria-hidden="true">—</span>{esc(t)}</li>' for t in f['points'])
        feats.append(f'''<article class="zz zz-app{' zz--dark' if i == 1 else ''}{' zz--flip' if i % 2 else ''}">
      <div class="zz-img app-tile" {reveal(0)}>{phone(shot, 'phone phone--tile')}</div>
      <div class="zz-text app-text" {reveal(120)}>
        <div class="app-icon">{icon(f['icon'], 26)}</div>
        <h2 class="h2-app"><strong>{esc(f['title'])}</strong> – {esc(f['claim'])}</h2>
        <p class="lead-18 lh16">{esc(f['lead'])}</p>
        {paras}
        <ul class="dash-list">{pts}</ul>
      </div>
    </article>''')
    body = f'''
<section class="app-intro" data-screen-label="App Intro">
  <div class="wrap app-intro-inner">
    <div class="eyebrow" {reveal(0)}>Unsere App</div>
    <h1 class="h1" {reveal(80)}>Jedes Tier. <strong>Lückenlos dokumentiert.</strong></h1>
    <p class="body-18 c-e2 dmax" {dmax(560)} {reveal(160)}>Für unsere Zucht haben wir eine eigene App entwickelt. Sie dokumentiert, wann ein Tier geschlüpft ist, wer seine Eltern sind und woher diese stammen.</p>
    <div class="app-phones">{''.join(phones)}</div>
  </div>
</section>

<section class="app-features clip-x" data-screen-label="App Features">
  <div class="wrap zz-list zz-list--app">{''.join(feats)}</div>
</section>

{contact_teaser(pg, 'Fragen zur <strong>App?</strong>')}
'''
    return pg, layout(pg, 'App', 'Unsere eigene Zucht-App: Hub, Collection und Lineage – jedes Tier lückenlos dokumentiert.', 'app', body)


def field_error(name):
    return f'<span class="ferr" role="alert" data-err="{name}" hidden>{icon("circle-alert", 15, 2)}<span></span></span>'


def page_kontakt():
    pg = Page('kontakt/index.html', 1)
    u = pg.url
    def info_val(v, h):
        if not h:
            return f'<span class="info-val">{esc(v)}</span>'
        ext = ' target="_blank" rel="noopener"' if h.startswith('http') else ''
        return f'<a class="info-val" href="{esc(h)}"{ext}>{esc(v)}</a>'
    info = ''.join(f'<div class="info-row">{icon(ic, 22)}<div class="info-txt"><span class="eyebrow">{esc(l)}</span>{info_val(v, h)}</div></div>'
                   for ic, l, v, h in C.CONTACT_INFO)
    topics = ''.join(f'<button type="button" class="tab" aria-pressed="{"true" if i == 0 else "false"}" data-topic-btn="{esc(t)}">{esc(t)}</button>' for i, t in enumerate(C.CONTACT_TOPICS))
    body = f'''
<section class="kontakt-sec" data-screen-label="Kontakt">
  <div class="wrap grid2 grid-1-115 align-start">
    <div class="kontakt-left">
      <div class="eyebrow" {reveal(0)}>Kontakt</div>
      <h1 class="h1-60" {reveal(80)}>Fragen, Interesse oder <strong>Anmerkungen?</strong></h1>
      <p class="body-18 lh165 dmax" {dmax(420)} {reveal(160)}>Schreib uns – wir melden uns schnellstmöglich.</p>
      <div class="info" {reveal(220)}>{info}</div>
    </div>

    <div class="form-box" {reveal(120)}>
      <form class="cform" action="senden.php" method="post" novalidate data-form>
        <div class="ftopic">
          <span class="ftopic-label" id="ftopic-label">Worum geht es?</span>
          <div class="tabs" role="group" aria-labelledby="ftopic-label">{topics}</div>
          <input type="hidden" name="thema" value="{esc(C.CONTACT_TOPICS[0])}">
        </div>
        <div class="grid2 grid-1-1 fgrid">
          <label class="field">Name *<input name="name" autocomplete="name" placeholder="Vor- und Nachname" required>{field_error('name')}</label>
          <label class="field">E-Mail *<input type="email" name="email" autocomplete="email" placeholder="name@beispiel.de" required>{field_error('email')}</label>
        </div>
        <label class="field" data-animal-field>Tier-ID <span class="field-hint">optional, z. B. NZ-2026-039</span><input name="tier" placeholder="NZ-2026-"></label>
        <label class="field">Nachricht *<textarea name="msg" rows="6" placeholder="Deine Nachricht an uns" required></textarea>{field_error('msg')}</label>
        <div class="consent-wrap">
          <label class="consent"><input type="checkbox" name="consent" value="1" required><span>Ich bin mit der Verarbeitung meiner Angaben zur Beantwortung meiner Anfrage einverstanden. Mehr dazu in der <a href="{u('datenschutz/')}">Datenschutzerklärung</a>. *</span></label>
          {field_error('consent')}
          <span class="req-note">* Pflichtfelder</span>
        </div>
        <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="fsubmit">
          <button type="submit" class="btn btn-primary btn-arrow">Nachricht senden<span aria-hidden="true">→</span></button>
          <span class="ferr ferr--send" role="alert" data-send-error hidden>{icon('circle-alert', 15, 2)}<span>Die Nachricht konnte leider nicht gesendet werden. Bitte versuch es später noch einmal oder schreib uns direkt an {esc(C.EMAIL)}.</span></span>
        </div>
      </form>
      <div class="fsuccess" data-success hidden tabindex="-1">
        <div class="fsuccess-icon">{icon('check', 28, 1.75)}</div>
        <h2>Danke für deine <strong>Nachricht.</strong></h2>
        <p class="dmax" {dmax(400)}>Wir melden uns schnellstmöglich bei dir.</p>
        <button type="button" class="btn-small btn-small--lg" data-reset>Weitere Nachricht senden</button>
      </div>
    </div>
  </div>
</section>
'''
    return pg, layout(pg, 'Kontakt', 'Kontakt zu Bleeding Edge Corns – Fragen zu Nachzuchten, Projekten oder Haltung.', 'kontakt', body)


def legal_blocks(body):
    out, toc, lst, n = [], [], None, 0
    for line in body.split('\n'):
        if line.startswith('- '):
            if lst is None:
                lst = []
                out.append(lst)
            lst.append(esc(line[2:]))
            continue
        lst = None
        if line.startswith('## '):
            n += 1
            out.append(f'<h2 id="abschnitt-{n}">{esc(line[3:])}</h2>')
            toc.append((f'abschnitt-{n}', line[3:]))
        elif line.startswith('> '):
            out.append(f'<p class="lnote">{esc(line[2:])}</p>')
        elif '|' in line:
            out.append('<div class="laddr">' + ''.join(f'<span>{esc(x)}</span>' for x in line.split('|')) + '</div>')
        elif line.strip():
            out.append(f'<p>{esc(line)}</p>')
    html_ = ''.join(x if isinstance(x, str) else '<ul class="dash-list dash-list--legal">' + ''.join(f'<li><span aria-hidden="true">—</span>{i}</li>' for i in x) + '</ul>' for x in out)
    return html_, toc


def page_legal(key, doc):
    pg = Page(f'{key}/index.html', 1)
    blocks, toc = legal_blocks(doc['body'])
    toc_html = ''.join(f'<a href="#{i}">{esc(t)}</a>' for i, t in toc)
    body = f'''
<section class="legal-sec" data-screen-label="{esc(doc['title'])}">
  <div class="wrap legal-stack">
    <div class="legal-head" {reveal(0)}>
      {eyebrow('Rechtliches')}
      <h1 class="h1-60"><strong>{esc(doc['title'])}</strong></h1>
    </div>
    <div class="legal-grid">
      <nav class="toc" aria-label="Inhalt" data-toc>{eyebrow('Inhalt', 'mb12')}{toc_html}</nav>
      <div class="legal-text dmax" {dmax(720)} {reveal(100)}>{blocks}<p class="stand">{esc(doc['stand'])}</p></div>
    </div>
  </div>
</section>
'''
    return pg, layout(pg, doc['title'], f'{doc["title"]} – {SITE_NAME}', key, body)


# ------------------------------------------------------------------ Build
def main():
    global NOINDEX
    ap = argparse.ArgumentParser(description='Website bauen')
    ap.add_argument('--live', action='store_true', help='ohne noindex (echte Website)')
    ap.add_argument('--import', dest='imp', metavar='CSV', help='MorphMarket-Export übernehmen')
    args = ap.parse_args()
    NOINDEX = not args.live
    if args.imp:
        import_csv(args.imp)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for d in ('img', 'fonts', 'assets'):
        shutil.copytree(SRC / d, DIST / d)
    shutil.copy(SRC / 'php' / 'senden.php', DIST / 'senden.php.tmp')

    animals = load_animals()
    pages = [page_home(animals), page_projekte(), page_nachzuchten(animals), page_kornnatter(), page_app(), page_kontakt(),
             page_legal('impressum', C.IMPRESSUM), page_legal('datenschutz', C.DATENSCHUTZ)]
    pages += [page_projekt(i) for i in range(len(C.PROJECTS))]
    for pg, out in pages:
        target = DIST / pg.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding='utf-8')
    (DIST / 'senden.php.tmp').rename(DIST / 'kontakt' / 'senden.php')
    robots = 'User-agent: *\nDisallow: /\n' if NOINDEX else 'User-agent: *\nAllow: /\n'
    (DIST / 'robots.txt').write_text(robots, encoding='utf-8')
    mode = 'Teststand (noindex)' if NOINDEX else 'LIVE (indexierbar)'
    print(f'{len(pages)} Seiten, {len(animals)} Nachzuchten, {mode} → {DIST}')


if __name__ == '__main__':
    main()
