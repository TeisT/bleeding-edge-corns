#!/usr/bin/env python3
"""Statischer Build für die Website "Bleeding Edge Corns".

Nur Python-Standardbibliothek. Aufrufe:
  python3 build.py                     Teststand: alle Seiten mit noindex (Suchmaschinen gesperrt)
  python3 build.py --live              echte Website: ohne noindex
  python3 build.py --import <csv>      MorphMarket-Export übernehmen (nur benötigte Spalten) und bauen
  python3 build.py --fotos             Nachzuchten-Fotos von MorphMarket nach src/img/nachzuchten/ laden und bauen
Erzeugt dist/ (komplett statisch, relative Links → läuft in jedem Unterordner).
Inhalte: content.py, Nachzuchten: data/nachzuchten.csv.
"""
import argparse
import csv
import html
import re
import shutil
import struct
from pathlib import Path

import content as C_DE
import content_en as C_EN

C = C_DE      # aktive Sprache, wird in main() umgeschaltet
LANG = 'de'
# Englische Seitenpfade (alles unter /en/). Projekt-Slugs sind schon englisch.
EN_PATHS = {'projekte/': 'projects/', 'nachzuchten/': 'hatchlings/', 'kornnatter/': 'corn-snake/',
            'kontakt/': 'contact/', 'impressum/': 'imprint/', 'datenschutz/': 'privacy/'}


def loc_path(p, lang):
    """Deutscher Seitenpfad (z. B. 'projekte/', 'kornnatter/#ernaehrung') → Pfad in der Sprache."""
    if lang == 'de':
        return p
    for de, en in EN_PATHS.items():
        if p.startswith(de):
            p = en + p[len(de):]
            break
    return 'en/' + p

ROOT = Path(__file__).parent
SRC = ROOT / 'src'
DIST = ROOT / 'dist'
SITE_NAME = C_DE.SITE['name']


# ------------------------------------------------------------------ Helfer
def esc(s):
    return html.escape(s, quote=True)


def md(s, pg=None):
    """Inline-Markdown (Text wird escaped): **fett** → <strong>, [[a b]] → nicht umbrechen,
    [Text](pfad/) → Link (interne Pfade relativ zur Startseite, über pg aufgelöst)."""
    parts = esc(s).split('**')
    out = ''.join(f'<strong>{p}</strong>' if i % 2 else p for i, p in enumerate(parts))
    out = re.sub(r'\[\[(.+?)\]\]', r'<span class="nowrap">\1</span>', out)

    def link(m):
        href = m.group(2)
        if pg and not re.match(r'^(https?:|mailto:|#)', href):
            href = pg.link(href)
        ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
        return f'<a href="{href}"{ext}>{m.group(1)}</a>'
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', link, out)


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
    def __init__(self, path, depth=None):
        self.key = path                     # deutscher Pfad, z. B. 'projekte/index.html'
        self.lang = LANG
        self.path = loc_path(path, LANG)    # Ausgabepfad, z. B. 'en/projects/index.html'
        depth = self.path.count('/')
        self.root = '../' * depth if depth else './'

    def url(self, p):
        """Datei (Bild, CSS, JS) relativ zur Seite – sprachunabhängig."""
        return self.root + p

    def link(self, p):
        """Interne Seite (deutscher Pfad) in der Sprache dieser Seite."""
        return self.root + loc_path(p, self.lang)

    def alt(self, lang):
        """Dieselbe Seite in der anderen Sprache."""
        return self.root + loc_path(self.key[:-len('index.html')], lang)


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


def image_size(path):
    """(Breite, Höhe) aus JPEG, PNG oder WebP lesen – ohne Zusatzbibliothek."""
    data = path.read_bytes()
    if data[:8] == b'\x89PNG\r\n\x1a\n':
        return struct.unpack('>II', data[16:24])
    if data[:4] == b'RIFF' and data[8:12] == b'WEBP':
        kind = data[12:16]
        if kind == b'VP8X':
            return (int.from_bytes(data[24:27], 'little') + 1, int.from_bytes(data[27:30], 'little') + 1)
        if kind == b'VP8L':
            v = int.from_bytes(data[21:25], 'little')
            return ((v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1)
        if kind == b'VP8 ':
            w, h = struct.unpack('<HH', data[26:30])
            return (w & 0x3FFF, h & 0x3FFF)
    if data[:2] == b'\xff\xd8':
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                h, w = struct.unpack('>HH', data[i + 5:i + 9])
                return (w, h)
            if marker in (0xD8, 0x01) or 0xD0 <= marker <= 0xD7:
                i += 2
                continue
            i += 2 + struct.unpack('>H', data[i + 2:i + 4])[0]
    raise SystemExit(f'Bildgröße nicht lesbar (nur JPG, PNG, WebP): {path}')


def load_gallery():
    """Galerie Startseite aus data/galerie.csv (Datei;Bildunterschrift;Kategorie)."""
    path = ROOT / 'data' / 'galerie.csv'
    text = path.read_text(encoding='utf-8-sig')
    delim = ';' if text.split('\n', 1)[0].count(';') >= text.split('\n', 1)[0].count(',') else ','
    out = []
    for n, r in enumerate(csv.reader(text.splitlines(), delimiter=delim)):
        if n == 0 or not r or not r[0].strip():
            continue  # Kopfzeile / Leerzeile
        r = [x.strip() for x in r] + ['', '']
        f, label, cat = r[0], r[1], r[2]
        img = SRC / 'img' / 'galerie' / f
        if not img.exists():
            raise SystemExit(f'data/galerie.csv, Zeile {n + 1}: Foto "{f}" fehlt in src/img/galerie/')
        w, h = image_size(img)
        cats = [c.strip() for c in cat.split(',') if c.strip()]  # mehrere Kategorien durch Komma getrennt
        out.append((f, w, h, label, cats))
    return out


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
        A = C.ANIMAL_SLIDER
        sex_label, sex_icon = {'female': (A['female'], '♀'), 'male': (A['male'], '♂')}.get(sex, (A['unknown'], ''))
        photos = r.get('Photo_Urls', '').split()
        local = NZ_IMG / f'{aid}.jpg'
        out.append({'id': aid, 'title': title, 'sex': sex_label, 'sex_icon': sex_icon,
                    'remote': photos[0] if photos else '',
                    'photo': f'img/nachzuchten/{aid}.jpg' if local.exists() else '',
                    'url': r.get('Mm_Url**', '').strip() or C.MORPHMARKET_SHOP})
    return out


NZ_IMG = SRC / 'img' / 'nachzuchten'


def fetch_photos(animals):
    """Erstes Foto jeder Nachzucht lokal ablegen (src/img/nachzuchten/<ID>.jpg), auf macOS mit sips auf 1200 px verkleinert."""
    import subprocess
    import urllib.request
    NZ_IMG.mkdir(parents=True, exist_ok=True)
    sips = shutil.which('sips')
    for a in animals:
        if not a['remote']:
            print(f'  {a["id"]}: kein Foto im Export')
            continue
        target = NZ_IMG / f'{a["id"]}.jpg'
        if target.exists():
            print(f'  {a["id"]}: schon vorhanden')
            continue
        req = urllib.request.Request(a['remote'], headers={'User-Agent': 'bleeding-edge-corns-build'})
        with urllib.request.urlopen(req, timeout=60) as resp:
            target.write_bytes(resp.read())
        if sips:
            subprocess.run([sips, '-Z', '1200', '-s', 'format', 'jpeg', '-s', 'formatOptions', '82', str(target)],
                           check=True, capture_output=True)
        print(f'  {a["id"]}: geladen ({target.stat().st_size // 1024} KB)')
    # Fotos von Tieren, die nicht mehr angeboten werden, aufräumen
    keep = {f'{a["id"]}.jpg' for a in animals}
    for f in NZ_IMG.glob('*.jpg'):
        if f.name not in keep:
            f.unlink()
            print(f'  {f.name}: entfernt (nicht mehr im Export)')


# ------------------------------------------------------------------ Bausteine
def mm_logo(pg, dark=False):
    f = ' mm-logo--dark' if dark else ''
    return f'<img class="mm-logo{f}" src="{pg.url("img/morphmarket-logo-white.svg")}" alt="{esc(C.SITE["mm_logo_alt"])}" width="56" height="21">'


def mm_button(pg, label=None, cls='btn btn-primary', dark_logo=False):
    label = label or C.SITE['mm_button']
    return (f'<a class="{cls} btn-mm" href="{C.MORPHMARKET_SHOP}" target="_blank" rel="noopener">{esc(label)} '
            f'<span class="nudge" aria-hidden="true">→</span> {mm_logo(pg, dark_logo)}</a>')


def lang_links(pg):
    out = []
    for lang in ('de', 'en'):
        cur = ' aria-current="true"' if lang == pg.lang else ''
        out.append(f'<a href="{pg.alt(lang)}" hreflang="{lang}" lang="{lang}"{cur}>{lang.upper()}</a>')
    return ''.join(out)


def header(pg, active):
    proj_sub = ''.join(f'<a class="subnav-link" href="{pg.link("projekte/" + p["slug"] + "/")}">{esc(p["title"])}</a>' for p in C.PROJECTS)
    items = []
    for key, label, href in C.NAV:
        cur = ' is-active' if key == active else ''
        aria = ' aria-current="page"' if key == active and active != 'projekte-detail' else ''
        if key == 'projekte':
            cur = ' is-active' if active in ('projekte', 'projekte-detail') else ''
            items.append(f'<div class="nav-item has-sub"><a class="nav-link{cur}" href="{pg.link(href)}" aria-haspopup="true"{aria}>{label}'
                         f'<span class="chev">{icon("chevron-right", 14, 1.75)}</span></a>'
                         f'<div class="subnav">{proj_sub}</div></div>')
        else:
            items.append(f'<div class="nav-item"><a class="nav-link{cur}" href="{pg.link(href)}"{aria}>{label}</a></div>')

    m_items = []
    for key, label, href in C.NAV:
        m_items.append(f'<a class="mnav-link" href="{pg.link(href)}">{label}<span aria-hidden="true">→</span></a>')
        if key == 'projekte':
            m_items.append('<div class="mnav-sub">' + ''.join(
                f'<a href="{pg.link("projekte/" + p["slug"] + "/")}">{esc(p["title"])}</a>' for p in C.PROJECTS) + '</div>')
    socials = ''.join(f'<a class="msocial" href="{u}" aria-label="{l}">{icon(i, 18)}</a>' for i, l, u in C.SOCIALS)

    S = C.SITE
    return f'''<header class="site-header">
  <div class="wrap header-bar">
    <a class="logo" href="{pg.link('')}" aria-label="{esc(S['home_label'])}"><img src="{pg.url('img/logo.png')}" alt="{esc(S['logo_alt'])}" width="560" height="400"></a>
    <nav class="main-nav" aria-label="{esc(S['nav_main'])}">{''.join(items)}</nav>
    <div class="header-right">
      <div class="lang" role="group" aria-label="{esc(S['lang_label'])}">{lang_links(pg)}</div>
      {mm_button(pg, cls='header-cta')}
      <button type="button" class="burger" aria-label="{esc(S['menu'])}" data-label-close="{esc(S['menu_close'])}" aria-expanded="false" aria-controls="mobile-menu">{icon('menu', 26, 1.5, 'i-menu')}{icon('x', 26, 1.5, 'i-close')}</button>
    </div>
  </div>
  <div class="mobile-menu" id="mobile-menu" hidden>
    <div class="wrap mobile-menu-inner">
      <nav class="mnav" aria-label="{esc(S['nav_mobile'])}">{''.join(m_items)}</nav>
      {mm_button(pg, cls='mmenu-cta')}
      <div class="msocials">{socials}</div>
    </div>
  </div>
</header>'''


def footer(pg):
    socials = ''.join(f'<a class="fsocial" href="{u}" aria-label="{l}">{icon(i, 18)}</a>' for i, l, u in C.SOCIALS)
    nav = ''.join(f'<a href="{pg.link(h)}">{l}</a>' for _, l, h in C.NAV)
    S = C.SITE
    return f'''<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="footer-logo" href="{pg.link('')}" aria-label="{esc(S['home_label'])}"><img src="{pg.url('img/logo.png')}" alt="{esc(S['logo_alt'])}" width="118" height="84"></a>
        <p>{md(S['footer_text'], pg)}</p>
        <div class="fsocials">{socials}</div>
      </div>
      <nav class="footer-nav" aria-label="{esc(S['nav_footer'])}">{nav}</nav>
    </div>
    <div class="footer-bottom">
      <span>{esc(S['copyright'])}</span>
      <div><a href="{pg.link('impressum/')}">{esc(S['impressum'])}</a><a href="{pg.link('datenschutz/')}">{esc(S['datenschutz'])}</a></div>
    </div>
  </div>
</footer>
<div class="mm-dock">{mm_button(pg, cls='mm-dock-btn')}</div>'''


def contact_teaser(pg, heading, bg='gray'):
    T = C.CONTACT_TEASER
    return f'''<section class="cta-section bg-{bg}" data-screen-label="Kontakt">
  <div class="wrap cta-inner" {reveal(0)}>
    {eyebrow(T['eyebrow'])}
    <h2 class="h2">{md(heading, pg)}</h2>
    <p class="cta-text dmax" {dmax(520)}>{md(T['text'], pg)}</p>
    <a class="btn btn-primary cta-btn" href="{pg.link('kontakt/')}">{esc(T['button'])}</a>
  </div>
</section>'''


def slider_arrows(theme):
    return (f'<div class="slider-arrows">'
            f'<button type="button" class="arrow arrow--{theme}" data-prev aria-label="{esc(C.SITE["prev"])}">{icon("arrow-left", 20)}</button>'
            f'<button type="button" class="arrow arrow--{theme}" data-next aria-label="{esc(C.SITE["next"])}">{icon("arrow-right", 20)}</button></div>')


def slider_bar(theme, label):
    return (f'<div class="sbar sbar--{theme}" data-bar role="scrollbar" aria-label="{label}" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0">'
            f'<div class="sbar-track"><div class="sbar-thumb"></div></div></div>')


def animals_slider(pg, animals, theme):
    """Nachzuchten-Slider. theme 'light' (Startseite, #f7f7f7) oder 'dark' (Nachzuchten-Seite)."""
    T = C.ANIMAL_SLIDER
    cards = []
    for a in animals:
        sx = f'<span class="sex-icon" aria-hidden="true">{a["sex_icon"]}</span>' if a['sex_icon'] else '<span class="sex-icon" aria-hidden="true"></span>'
        cards.append(f'''<a class="acard" href="{esc(a["url"])}" target="_blank" rel="noopener">
          <div class="acard-img">{f'<img src="{esc(pg.url(a["photo"]) if a["photo"] else a["remote"])}" alt="{esc(a["title"])}" loading="lazy" width="600" height="750">' if a["photo"] or a["remote"] else ''}</div>
          <div class="acard-body">
            <span class="acard-id">{esc(a["id"])}</span>
            <div class="acard-title">{esc(a["title"])}</div>
            <div class="acard-sex">{sx}{esc(a["sex"])}</div>
            <div class="acard-foot"><span class="link-arrow">{esc(T['card_link'])}<span aria-hidden="true">→</span></span></div>
          </div>
        </a>''')
    cards.append(f'''<a class="acard-all" href="{C.MORPHMARKET_SHOP}" target="_blank" rel="noopener">
        <div class="acard-all-eyebrow">{esc(T['all_eyebrow'])}</div>
        <div class="acard-all-mid">
          <div class="acard-all-title">{md(T['all_title'])}</div>
          <div class="acard-all-text">{md(T['all_text'])}</div>
        </div>
        <span class="acard-all-pill">{esc(T['all_pill'])} <span class="nudge" aria-hidden="true">→</span></span>
      </a>''')
    btn_cls = 'btn btn-primary' if theme == 'light' else 'btn btn-light'
    return f'''<section class="nz-slider nz-slider--{theme}" data-screen-label="Nachzuchten" data-slider>
  <div class="slider-stack">
    <div class="wrap slider-head">
      <h2 class="h2-slider dmax" {dmax(720)}>{md(T['heading'], pg)}</h2>
      {slider_arrows('light' if theme == 'light' else 'dark')}
    </div>
    <div class="track" data-track>{''.join(cards)}</div>
    <div class="wrap slider-foot">
      {mm_button(pg, T['all_button'], btn_cls, dark_logo=(theme == 'dark'))}
      {slider_bar('light' if theme == 'light' else 'dark', esc(T['bar_label']))}
    </div>
  </div>
</section>'''


def cells(items, padfirst=False, dark=False):
    """Vertrauensleiste / Ablauf: Icon, Titel, Text, Trennlinien zwischen den Spalten."""
    cls = 'cells' + (' cells--padfirst' if padfirst else '')
    out = [f'<div class="cell" {reveal(i * 80)}>{icon(ic, 26)}<div class="cell-title">{esc(t)}</div><div class="cell-text">{esc(d)}</div></div>'
           for i, (ic, t, d) in enumerate(items)]
    return f'<div class="{cls}">{"".join(out)}</div>'


def long_text(body, pg=None):
    """Mini-Markdown (Kornnatter-Themen)."""
    out, lst = [], None
    for line in body.split('\n'):
        if line.startswith('- '):
            if lst is None:
                lst = []
                out.append(lst)
            lst.append(md(line[2:], pg))
            continue
        lst = None
        if line.startswith('#### '):
            out.append(f'<h4>{esc(line[5:])}</h4>')
        elif line.startswith('## '):
            out.append(f'<h3>{esc(line[3:])}</h3>')
        elif line.startswith('> '):
            out.append(f'<p class="note">{md(line[2:], pg)}</p>')
        elif line.strip():
            out.append(f'<p>{md(line, pg)}</p>')
    return ''.join(x if isinstance(x, str) else '<ul class="dlist">' + ''.join(f'<li>{i}</li>' for i in x) + '</ul>' for x in out)


def app_demo(kind):
    """Animierte Mini-App im Kachel-Phone, 1:1 nach den App-Screens (CSS .dm-* in style.css, Maße in pt/16 = em).
    Texte stehen in content.py unter APP_DEMO."""
    D = C.APP_DEMO
    sysi = ('<svg class="dm-sys" viewBox="0 0 70 13" fill="#fff"><rect x="0" y="8" width="3" height="4" rx=".8"/><rect x="4.5" y="6" width="3" height="6" rx=".8"/>'
            '<rect x="9" y="3.5" width="3" height="8.5" rx=".8"/><rect x="13.5" y="1" width="3" height="11" rx=".8"/>'
            '<path d="M29.5 12 22.6 5.1a9.8 9.8 0 0 1 13.8 0Z"/><rect x="43.5" y="1" width="22" height="11" rx="3.3" fill="none" stroke="#fff" stroke-opacity=".45"/>'
            '<rect x="45.5" y="3" width="15" height="7" rx="1.8"/><rect x="66.6" y="4.6" width="1.5" height="3.8" rx=".7" fill-opacity=".45"/></svg>')
    def top(eb, h1, extra=''):
        return (f'<div class="dm-top"><div class="dm-status"><b>9:41</b><i class="dm-island"></i>{sysi}</div>'
                f'<div class="dm-r1"><i class="dm-wm"></i><span class="dm-btns"><i>{icon("cn-qr", 14, 2)}</i><i>{icon("cn-gear", 16, 2)}</i></span></div>'
                f'<p class="dm-eb">{eb}</p><p class="dm-h1">{h1}</p>{extra}</div>')
    def ring(lbl, c, p, cls=''):
        return f'<span class="dm-ring{cls}" style="--c:{c};--p:{p}%"><b>{lbl}</b></span>'
    def row(name, sex, morph, rg, cls=''):
        return (f'<div class="dm-an{cls}"><i class="dm-th"></i><span class="dm-tx"><b>{name}<em>{sex}</em></b><small>{morph}</small></span>{rg}</div>')
    def sec(t, c):
        return f'<div class="dm-sec"><b>{t}</b><span>{c}</span></div>'
    if kind == 'swipe':
        fed = ring('14', '#cfa9ad', 100, ' dm-q1') + f'<span class="dm-ring dm-q2" style="--c:#4b9b5c;--p:100%"><b>{icon("cn-mouse", 14, 2.2)}</b></span>'
        shd = ring('5', '#e9a73a', 100, ' dm-q1') + f'<span class="dm-ring dm-q2" style="--c:#4467a8;--p:100%"><b>{icon("cn-eye", 14, 2.2)}</b></span>'
        body = (f'<div class="dm-stats"><div class="dm-st dm-st--due"><small>{D["due"]}</small><b>3</b><span>{D["feedings"]}</span></div>'
                f'<div class="dm-st"><small>{D["pause"]}</small><b>1</b><span>{D["shed"]}</span></div><div class="dm-st"><small>{D["hatch"]}</small><b>11</b><span>{D["days"]}</span></div></div>'
                + sec(D['incubator'], D['clutches'])
                + f'<div class="dm-card dm-inc"><p><b>G-26-02</b><span>{D["day"]}</span></p><p class="dm-pair">Cornflakes × Tortilla</p><i class="dm-prog"><i></i></i><small>{D["hatch_eta"]}</small></div>'
                + sec(D['feed_today'], D['animals_3'])
                + f'<div class="dm-hint"><span>← {D["feeding"]}</span><span>{D["long_press"]}</span><span>{D["in_shed"]} →</span></div>'
                + '<div class="dm-card dm-list">'
                + f'<div class="dm-sr"><span class="dm-act dm-act--feed">{icon("cn-mouse", 16, 2)}{D["feeding"]}</span>{row("Cornflakes", "0.1", "Shatter", fed, " dm-sw dm-sw--l")}<i class="dm-finger dm-finger--l"></i></div>'
                + f'<div class="dm-sr"><span class="dm-act dm-act--shed">{icon("cn-eye", 16, 2)}{D["in_shed"]}</span>{row("N-26-12", "0.0.1", "Palmetto", shd, " dm-sw dm-sw--r")}<i class="dm-finger dm-finger--r"></i></div>'
                + row('Polenta', '1.0', 'Hypo Bloodred', ring('7', '#e9a73a', 72))
                + '</div>')
        return f'<div class="dm dm-swipe" aria-hidden="true">{top(D["date"], D["greeting"])}<div class="dm-body">{body}</div></div>'
    if kind == 'menu':
        tools = ('<div class="dm-search">' + '<svg viewBox="0 0 24 24" fill="none" stroke="#b9b6c6" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>'
                 f'<span>{D["search"]}</span></div><div class="dm-chips"><i class="on">{D["all"]}</i><i>1.0</i><i>0.1</i><i>0.0.1</i><i>{D["due"]}</i></div>')
        rows = (f'<div class="dm-press">{row("Cornflakes", "0.1", "Shatter", ring("14", "#cfa9ad", 100))}<i class="dm-finger dm-finger--p"></i></div>'
                + row('N-26-12', '0.0.1', 'Palmetto', ring('5', '#e9a73a', 100))
                + row('Polenta', '1.0', 'Hypo Bloodred', ring('7', '#e9a73a', 72))
                + row('Tortilla', '0.1', 'Amel', ring('3', '#4b9b5c', 40))
                + row('Taco', '1.0', 'Tessera', ring('4', '#4b9b5c', 30))
                + row('Nacho', '0.1', 'Charcoal', ring('6', '#4b9b5c', 15)))
        body = (f'<div class="dm-vt"><i class="on">{icon("cn-rows", 14, 2)}</i><i>{icon("cn-grid", 14, 2)}</i></div>'
                f'<div class="dm-card dm-list">{rows}</div>')
        kinds = [('cn-shed', 'shed'), ('cn-mouse', 'ok'), ('cn-eye', 'shed'), ('cn-scale', 'neu'), ('cn-cam', 'neu'),
                 ('cn-lineage', 'neu'), ('cn-qr', 'neu'), ('cn-pair', 'pair'), ('cn-calculator', 'neu')]
        sheet = ''.join(f'<li class="dm-it{" dm-it--hi" if n == "cn-pair" else ""}"><i class="dm-dot dm-dot--{c}">{icon(n, 16, 2)}</i>{t}</li>'
                        for (n, c), t in zip(kinds, D['menu']))
        return (f'<div class="dm dm-menu" aria-hidden="true">{top(D["animals_24"], D["collection"], tools)}<div class="dm-body">{body}</div>'
                f'<i class="dm-scrim"></i><div class="dm-sheet"><i class="dm-grab"></i><b class="dm-sh">Shatter</b><ul>{sheet}</ul><i class="dm-finger dm-finger--s"></i></div></div>')
    if kind == 'calc':
        x = icon('cn-x', 10, 2.6)
        par = (f'<div class="dm-card dm-pc"><p class="dm-pr"><em>1.0</em><b>{D["sire"]}</b><u>{D["from_collection"]}</u></p><p class="dm-pn">Tessera</p><small>het Cinder</small></div>'
               f'<div class="dm-card dm-pc"><p class="dm-pr"><em>0.1</em><b>{D["dam"]}</b><u>{D["from_collection"]}</u></p>'
               '<p class="dm-pn"><span class="dm-n1">Cinder</span><span class="dm-n2">Cinder Sunkissed</span></p>'
               f'<div class="dm-in">{D["genes_hint"]}</div>'
               f'<div class="dm-gc"><i>Cinder{x}</i><i class="dm-new">Sunkissed{x}</i></div></div>')
        res = [('Cinder', '', 'het Sunkissed'), ('Cinder Tessera', 'Cinder + Tessera', 'het Sunkissed'),
               ('Normal', '', 'het Cinder · het Sunkissed'), ('Tessera', '', 'het Cinder · het Sunkissed')]
        rows = ''.join(f'<div class="dm-res" style="--i:{i}"><span class="dm-pct"><b>{D["pct"]}</b><small>1/4</small></span>'
                       f'<span class="dm-tx"><b>{a}</b>{f"<small>{s}</small>" if s else ""}<small class="dk">{h}</small><i class="dm-bar"><i></i></i></span><em>{D["count"]}</em></div>'
                       for i, (a, s, h) in enumerate(res))
        body = (f'<div class="dm-scroll">{par}' + sec(D['offspring'], D['phenotypes'])
                + f'<div class="dm-cl"><span>{D["clutch_size"]}</span><span class="dm-step"><i>–</i><b>12</b><i>+</i></span></div>'
                + f'<div class="dm-card dm-rs">{rows}</div></div>')
        return f'<div class="dm dm-calc" aria-hidden="true">{top(D["genetics"], D["calculator"])}<div class="dm-body">{body}</div></div>'
    return ''

def phone(slot_img, cls='phone'):
    """Smartphone-Mockup. slot_img: ein Bildpfad oder eine Liste (dann wechseln die Screens automatisch)."""
    imgs = slot_img if isinstance(slot_img, list) else ([slot_img] if slot_img else [])
    on = ' class="on"'
    tags = ''.join(f'<img src="{s}" alt="" loading="lazy"{on if i == 0 else ""}>' for i, s in enumerate(imgs))
    slides = ' data-slides' if len(imgs) > 1 else ''
    dots = ('<div class="phone-dots" aria-hidden="true">' + ''.join(f'<i{on if i == 0 else ""}></i>' for i in range(len(imgs))) + '</div>') if len(imgs) > 1 else ''
    notch = '' if imgs else '<div class="phone-notch"></div>'
    return f'<div class="phone-wrap"><div class="{cls}"{slides}><div class="phone-screen">{tags}{notch}</div></div>{dots}</div>'


# ------------------------------------------------------------------ Layout
NOINDEX = True  # wird mit --live abgeschaltet


def layout(pg, title, description, active, body):
    full_title = f'{SITE_NAME} – {title}'
    robots = '\n<meta name="robots" content="noindex, nofollow">' if NOINDEX else ''
    return f'''<!DOCTYPE html>
<html lang="{pg.lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(description)}">{robots}
<link rel="alternate" hreflang="de" href="{pg.alt('de')}">
<link rel="alternate" hreflang="en" href="{pg.alt('en')}">
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
def page_home(animals, gallery):
    pg = Page('index.html', 0)
    u = pg.url
    T = C.HOME
    proj_cards = ''.join(f'''<a class="pcard" href="{pg.link('projekte/' + p['slug'] + '/')}" {reveal(i * 100)}>
        <div class="pcard-img"><img src="{u(p['img_start'])}" alt="{esc(p['title'])}" loading="lazy" width="606" height="758"></div>
        <div class="pcard-body">
          <h3>{esc(p['title'])}</h3>
          <p>{esc(p['teaser'])}</p>
          <span class="link-arrow">{esc(T['projects_link'])}<span aria-hidden="true">→</span></span>
        </div>
      </a>''' for i, p in enumerate(C.PROJECTS))

    used = []
    for g in gallery:
        for c in g[4]:
            if c not in used:
                used.append(c)
    cats = [c for c in C.GALLERY_CATS if c in used] + [c for c in used if c not in C.GALLERY_CATS]
    tabs = f'<button type="button" role="tab" class="tab" aria-selected="true" data-filter="*">{esc(C.GALLERY_ALL)}</button>' + ''.join(
        f'<button type="button" role="tab" class="tab" aria-selected="false" data-filter="{esc(c)}">{esc(C.GALLERY_LABELS.get(c, c))}</button>' for c in cats)
    figs = ''.join(f'''<figure class="gfig" data-cats="{esc('|'.join(cats))}">
          <div class="gimg" style="aspect-ratio:{w} / {h}"><img src="{u('img/galerie/' + f)}" alt="{esc(label)}" loading="lazy" width="{w}" height="{h}"></div>
          <figcaption><span class="gcap-label">{md(label, pg)}</span></figcaption>
        </figure>''' for f, w, h, label, cats in gallery)

    app_points = ''.join(f'''<div class="apoint" {reveal(120 + i * 80)}>{icon(ic, 26)}<div><div class="apoint-title">{esc(t)}</div><div class="apoint-text">{esc(d)}</div></div></div>'''
                         for i, (ic, t, d) in enumerate(C.APP_POINTS))
    shot = u(C.APP_SCREENSHOT_HOME) if C.APP_SCREENSHOT_HOME else ''
    about_paras = ''.join(f'<p class="body-18">{md(t, pg)}</p>' for t in T['about_paras'])

    body = f'''
<section class="hero" data-screen-label="Hero">
  <picture>
    <source media="(max-width: 639.98px)" srcset="{u('img/hero-mobil.jpg')} 1x, {u('img/hero-mobil-2x.jpg')} 2x">
    <source media="(max-width: 1023.98px)" srcset="{u('img/hero-tablet.jpg')} 1x, {u('img/hero-tablet-2x.jpg')} 2x">
    <img class="hero-img" src="{u('img/hero-desktop-wide.jpg')}" srcset="{u('img/hero-desktop-wide.jpg')} 1x, {u('img/hero-desktop-wide-2x.jpg')} 2x" alt="{esc(T['hero_img_alt'])}" fetchpriority="high">
  </picture>
  <div class="wrap hero-wrap">
    <div class="hero-text">
      <div class="hero-eyebrow" {reveal(0)} aria-label="{esc(T['hero_eyebrow_label'])}"><span>{esc(T['hero_eyebrow_before'])}</span>{icon('heart', 14, 1.75)}<span>{esc(T['hero_eyebrow_after'])}</span></div>
      <h1 class="h1 hero-h1" {reveal(80)}>{md(T['hero_h1'], pg)}</h1>
      <p class="hero-p" {reveal(160)}>{md(T['hero_text'], pg)}</p>
      <div class="hero-btns" {reveal(240)}>
        <a class="btn btn-primary" href="{pg.link('nachzuchten/')}">{esc(T['hero_button_1'])}</a>
        <a class="btn btn-secondary" href="{pg.link('projekte/')}">{esc(T['hero_button_2'])}</a>
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
      {eyebrow(T['projects_eyebrow'], 'mb18')}
      <h2 class="h2">{md(T['projects_h2'], pg)}</h2>
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
          {eyebrow(T['gallery_eyebrow'], 'mb18')}
          <h2 class="h2">{md(T['gallery_h2'], pg)}</h2>
        </div>
        {slider_arrows('light')}
      </div>
      <div class="tabs" role="tablist" aria-label="{esc(T['gallery_filter_label'])}">{tabs}</div>
    </div>
    <div class="track track--gallery" data-track>{figs}</div>
    <div class="wrap slider-foot slider-foot--end">{slider_bar('light', esc(T['gallery_bar_label']))}</div>
  </div>
</section>

<section class="sec bg-gray" data-screen-label="Über uns">
  <div class="wrap grid2 grid-1-1 about">
    <div class="about-img" {reveal(0)}><img src="{u('img/ueber-uns.jpg')}" alt="{esc(T['about_img_alt'])}" loading="lazy" width="1000" height="1000"></div>
    <div class="about-text dmax" {dmax(500)} {reveal(120)}>
      {eyebrow(T['about_eyebrow'])}
      <h2 class="h2">{md(T['about_h2'], pg)}</h2>
      <p class="lead-20">{md(T['about_lead'], pg)}</p>
      {about_paras}
      <a class="about-link" href="{pg.link('kontakt/')}">{esc(T['about_link'])}</a>
    </div>
  </div>
</section>

<section class="sec bg-black app-teaser" data-screen-label="App">
  <div class="wrap grid2 grid-1-115">
    <div class="app-phone-wrap" {reveal(0)}>{phone(shot, 'phone phone--home')}</div>
    <div class="app-teaser-text">
      <div {reveal(80)}>
        {eyebrow(T['app_eyebrow'], 'mb18')}
        <h2 class="h2">{md(T['app_h2'], pg)}</h2>
        <p class="app-free">{md(T['app_free'], pg)}</p>
      </div>
      <div class="apoints">{app_points}</div>
      <a class="link-arrow link-arrow--white" href="{pg.link('app/')}" {reveal(200)}>{esc(T['app_link'])}<span aria-hidden="true">→</span></a>
    </div>
  </div>
</section>

{contact_teaser(pg, T['contact_h2'])}
'''
    return pg, layout(pg, T['title'], T['description'], 'home', body)


def page_projekte():
    pg = Page('projekte/index.html', 1)
    u = pg.url
    T = C.PROJEKTE
    arts = []
    for i, p in enumerate(C.PROJECTS):
        dark = i == 1
        paras = ''.join(f'<p class="body-17">{md(t, pg)}</p>' for t in p['list_paras'])
        genes = ''.join(f'<span class="gene">{esc(g)}</span>' for g in p['genes'])
        btn = 'btn-light' if dark else 'btn-primary'
        arts.append(f'''<article id="projekt-{i + 1}" class="zz{' zz--dark' if dark else ''}{' zz--flip' if i % 2 else ''}">
      <div class="zz-img ratio-45" {reveal(0)}><img src="{u(p['img_list'])}" alt="{esc(p['title'])}" loading="lazy" width="872" height="1090"></div>
      <div class="zz-text dmax" {dmax(500)} {reveal(120)}>
        {eyebrow(f"{T['project_label']} {i + 1}", 'mbm12')}
        <h2 class="h2-zz">{md(p['title_md'], pg)}</h2>
        <p class="lead-18">{md(p['list_lead'], pg)}</p>
        {paras}
        <div class="genes-block">{eyebrow(T['genes_label'])}<div class="genes">{genes}</div></div>
        <div class="goal">{eyebrow(p['goal_label'])}<div class="goal-text">{md(p['goal'], pg)}</div></div>
        <a class="btn {btn} btn-arrow" href="{pg.link('projekte/' + p['slug'] + '/')}">{esc(T['button'])}<span aria-hidden="true">→</span></a>
      </div>
    </article>''')
    body = f'''
<section class="intro-dark" data-screen-label="Projekte Intro">
  <div class="wrap grid2 grid-12-1 align-end gap-96">
    <div class="intro-left" {reveal(0)}>
      {eyebrow(T['eyebrow'])}
      <h1 class="h1">{md(T['h1'], pg)}</h1>
    </div>
    <p class="body-18 c-e2" {reveal(100)}>{md(T['intro'], pg)}</p>
  </div>
</section>

<section class="sec clip-x" data-screen-label="Projekte Zickzack">
  <div class="wrap zz-list">{''.join(arts)}</div>
</section>

{contact_teaser(pg, T['contact_h2'])}
'''
    return pg, layout(pg, T['title'], T['description'], 'projekte', body)


def page_projekt(idx):
    p = C.PROJECTS[idx]
    pg = Page(f'projekte/{p["slug"]}/index.html', 2)
    u = pg.url
    T = C.PROJEKT_DETAIL
    label = C.PROJEKTE['project_label']
    blocks = ''.join(f'<h2 class="h2-24">{md(t[3:], pg)}</h2>' if t.startswith('## ') else f'<p class="body-17 lh18">{md(t, pg)}</p>' for t in p['detail_body'])
    lead = f'<p class="lead-20">{md(p["detail_lead"], pg)}</p>' if p['detail_lead'] else ''
    figs = ''.join(f'''<figure class="gfig">
          <div class="gimg gimg--dark" style="aspect-ratio:{w} / 900"><img src="{u('img/galerie/' + f)}" alt="{esc(cap or p['title'])}" loading="lazy" width="{w}" height="900"></div>
          <figcaption class="gcap-dark">{esc(cap or p['title'])}</figcaption>
        </figure>''' for f, w, cap in p['gallery'])

    def link(i, d):
        q = C.PROJECTS[i]
        lab = f'← {label} {i + 1}' if d == 'prev' else f'{label} {i + 1} →'
        return f'<a class="pnav-link pnav-link--{d}" href="{pg.link("projekte/" + q["slug"] + "/")}"><span class="eyebrow">{lab}</span><span class="pnav-title">{esc(q["title"])}</span></a>'

    prev = link(idx - 1, 'prev') if idx > 0 else ''
    nxt = link(idx + 1, 'next') if idx < len(C.PROJECTS) - 1 else ''
    body = f'''
<section class="crumb-sec" data-screen-label="Breadcrumb">
  <div class="wrap"><nav class="crumb" aria-label="{esc(T['breadcrumb_label'])}" {reveal(0)}><a href="{pg.link('projekte/')}">{esc(T['breadcrumb'])}</a><span class="crumb-sep">/</span><span aria-current="page">{esc(p['title'])}</span></nav></div>
</section>

<section class="detail-sec" data-screen-label="Projekt Text">
  <div class="wrap grid2 grid-1-125 align-start">
    <div class="sticky-col" {reveal(0)}>
      {eyebrow(f"{label} {idx + 1}")}
      <h1 class="h1-60">{md(p['title_md'], pg)}</h1>
    </div>
    <div class="detail-text dmax" {dmax(620)} {reveal(120)}>{lead}{blocks}</div>
  </div>
</section>

<section class="sec-104 bg-black gallery" data-screen-label="Weitere Fotos" data-slider>
  <div class="slider-stack gallery-stack">
    <div class="wrap slider-head" {reveal(0)}>
      <div>
        {eyebrow(T['gallery_eyebrow'], 'mb18')}
        <h2 class="h2">{md(T['gallery_h2'], pg)}</h2>
      </div>
      {slider_arrows('dark')}
    </div>
    <div class="track track--gallery" data-track>{figs}</div>
    <div class="wrap slider-foot slider-foot--end">{slider_bar('dark', esc(T['gallery_bar_label']))}</div>
  </div>
</section>

<section class="pnav-sec" data-screen-label="Projekt Navigation">
  <div class="wrap pnav">
    <div class="pnav-cell">{prev}</div>
    <a class="btn btn-secondary btn-allproj" href="{pg.link('projekte/')}">{icon('layout-grid', 16)}{esc(T['all_projects'])}</a>
    <div class="pnav-cell pnav-cell--next">{nxt}</div>
  </div>
</section>

{contact_teaser(pg, T['contact_h2'])}
'''
    return pg, layout(pg, p['title'], T['description'].format(title=p['title'], teaser=p['teaser']), 'projekte-detail', body)


def page_nachzuchten(animals):
    pg = Page('nachzuchten/index.html', 1)
    u = pg.url
    T = C.NACHZUCHTEN
    faq = ''.join(f'''<div class="faq-item{' is-open' if i == 0 else ''}">
        <button type="button" class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="faq-{i}" id="faq-q-{i}">{esc(q)}{icon('plus', 22, 1.5, 'i-plus')}{icon('minus', 22, 1.5, 'i-minus')}</button>
        <div class="faq-a" id="faq-{i}" role="region" aria-labelledby="faq-q-{i}"{'' if i == 0 else ' hidden'}><p>{md(a, pg)}</p></div>
      </div>''' for i, (q, a) in enumerate(C.FAQ))
    body = f'''
<section class="nz-intro" data-screen-label="Nachzuchten Intro">
  <div class="wrap grid2 grid-12-1 align-end gap-96">
    <div class="intro-left" {reveal(0)}>
      {eyebrow(T['eyebrow'])}
      <h1 class="h1">{md(T['h1'], pg)}</h1>
    </div>
    <div class="intro-right" {reveal(100)}>
      <p class="body-18">{md(T['intro'], pg)}</p>
      {mm_button(pg, T['button'])}
    </div>
  </div>
</section>

{animals_slider(pg, animals, 'dark')}

<section class="steps" data-screen-label="Ablauf">
  <div class="wrap steps-inner">
    <div class="eyebrow" {reveal(0)}>{esc(T['steps_eyebrow'])}</div>
    {cells(C.STEPS)}
  </div>
</section>

<section class="sec bg-gray" data-screen-label="FAQ">
  <div class="wrap grid2 grid-1-16 align-start gap-96">
    <div class="sticky-col" {reveal(0)}>
      {eyebrow(T['faq_eyebrow'])}
      <h2 class="h2">{md(T['faq_h2'], pg)}</h2>
      <p class="body-16 text-links">{md(T['faq_text'], pg)}</p>
    </div>
    <div class="faq" data-faq {reveal(100)}>{faq}</div>
  </div>
</section>

{contact_teaser(pg, T['contact_h2'], 'white')}
'''
    return pg, layout(pg, T['title'], T['description'], 'nachzuchten', body)


def page_kornnatter():
    pg = Page('kornnatter/index.html', 1)
    u = pg.url
    T = C.KORNNATTER
    stats = ''.join(f'<div class="stat" {reveal(i * 70)}>{icon(ic, 24)}<div class="stat-v">{esc(v)}</div><div class="stat-l">{esc(l)}</div></div>'
                    for i, (ic, v, l) in enumerate(C.STATS))
    topics = []
    for t in C.TOPICS:
        intro = f'<p class="topic-intro">{md(t["intro"], pg)}</p>' if t['intro'] else ''
        fazit = f'<div class="fazit">{eyebrow(T["fazit_label"])}<p>{md(t["fazit"], pg)}</p></div>' if t['fazit'] else ''
        topics.append(f'''<div class="topic" data-topic="{t['id']}" id="{t['id']}">
        <button type="button" class="topic-head" aria-expanded="false" aria-controls="panel-{t['id']}">
          {icon(t['glyph'], 24)}<span class="topic-title">{esc(t['title'])}</span>{icon('plus', 24, 1.5, 'i-plus')}{icon('minus', 24, 1.5, 'i-minus')}
        </button>
        <div class="topic-panel" id="panel-{t['id']}" hidden>
          {intro}{long_text(t['body'], pg)}{fazit}
          <div class="topic-close"><button type="button" class="btn-small" data-close>{esc(T['close_button'])}</button></div>
        </div>
      </div>''')
    body = f'''
<section class="kn-intro" data-screen-label="Kornnatter Intro">
  <div class="wrap grid2 grid-11-1 align-center kn-grid">
    <div class="kn-text">
      <div class="eyebrow" {reveal(0)}>{esc(T['eyebrow'])}</div>
      <h1 class="h1" {reveal(80)}>{md(T['h1'], pg)}</h1>
      <p class="lead-19" {reveal(160)}>{md(T['lead'], pg)}</p>
      <p class="body-17 lh17" {reveal(220)}>{md(T['text'], pg)}</p>
    </div>
    <div class="kn-img ratio-45" {reveal(120)}><img src="{u('img/slots/kornnatter-intro.webp')}" alt="{esc(T['img_alt'])}" width="835" height="1044"></div>
  </div>
</section>

<section class="stats-sec" data-screen-label="Kennzahlen">
  <div class="wrap stats">{stats}</div>
</section>

<section class="sec" data-screen-label="Themen">
  <div class="wrap stack-64">
    <div {reveal(0)}>
      {eyebrow(T['topics_eyebrow'], 'mb18')}
      <h2 class="h2">{md(T['topics_h2'], pg)}</h2>
    </div>
    <div class="topics" data-topics>{''.join(topics)}</div>
  </div>
</section>
'''
    return pg, layout(pg, T['title'], T['description'], 'kornnatter', body)


def app_cta(pg, T):
    """Abschluss der App-Seite: Link zur Cornnector-Seite."""
    if not T.get('cta_h2'):
        return ''
    href = T.get('cta_url') or '#'
    ext = ' target="_blank" rel="noopener"' if href.startswith('http') else ''
    return f'''<section class="cta-section bg-black app-cta" data-screen-label="Cornnector">
  <div class="wrap cta-inner" {reveal(0)}>
    <h2 class="h2">{md(T['cta_h2'], pg)}</h2>
    <p class="cta-text dmax" {dmax(520)}>{md(T['cta_text'], pg)}</p>
    <a class="btn btn-light cta-btn btn-arrow" href="{esc(href)}"{ext}>{esc(T['cta_button'])}</a>
    <p class="app-cta-note">{esc(T['cta_note'])}</p>
  </div>
</section>'''


def page_app():
    pg = Page('app/index.html', 1)
    u = pg.url
    T = C.APP
    phones = []
    def shots(f):
        sc = f['screenshot']
        return [u(x) for x in sc] if isinstance(sc, list) else (u(sc) if sc else '')
    # Intro-Phones: Zucht (Verpaart) links, Hub in der Mitte, Rechner rechts
    intro = [C.APP_FEATURES[1], C.APP_FEATURES[0]] + C.APP_FEATURES[2:]
    for i, f in enumerate(intro):
        sc = shots(f)
        shot = sc[0] if isinstance(sc, list) else sc
        cls = 'app-ph app-ph--mid' if i == 1 else 'app-ph app-ph--side'
        phones.append(f'<div class="{cls}" {reveal(200 + i * 120)}><div class="app-ph-shift">{phone(shot, "phone phone--intro")}</div></div>')
    feats = []
    for i, f in enumerate(C.APP_FEATURES):
        shot = shots(f)
        tile = (f'<div class="phone phone--tile"><div class="phone-screen">{app_demo(f["demo"])}<div class="phone-notch"></div></div></div>'
                if f.get('demo') else phone(shot, 'phone phone--tile'))
        paras = ''.join(f'<p class="body-17">{md(t, pg)}</p>' for t in f['paras'])
        pts = ''.join(f'<li><span aria-hidden="true">—</span>{md(t, pg)}</li>' for t in f['points'])
        feats.append(f'''<article class="zz zz-app{' zz--dark' if i == 1 else ''}{' zz--flip' if i % 2 else ''}">
      <div class="zz-img app-tile" {reveal(0)}>{tile}</div>
      <div class="zz-text app-text" {reveal(120)}>
        <div class="app-icon">{icon(f['icon'], 26)}</div>
        <h2 class="h2-app"><strong>{esc(f['title'])}</strong> – {esc(f['claim'])}</h2>
        <p class="lead-18 lh16">{md(f['lead'], pg)}</p>
        {paras}
        <ul class="dash-list">{pts}</ul>
      </div>
    </article>''')
    body = f'''
<section class="app-intro" data-screen-label="App Intro">
  <div class="wrap app-intro-inner">
    <div class="eyebrow" {reveal(0)}>{esc(T['eyebrow'])}</div>
    <h1 class="h1" {reveal(80)}>{md(T['h1'], pg)}</h1>
    <p class="app-free app-free--intro" {reveal(120)}>{md(T['free'], pg)}</p>
    <p class="body-18 c-e2 dmax" {dmax(560)} {reveal(160)}>{md(T['intro'], pg)}</p>
    <div class="app-phones">{''.join(phones)}</div>
  </div>
</section>

<section class="app-features clip-x" data-screen-label="App Features">
  <div class="wrap zz-list zz-list--app">{''.join(feats)}</div>
</section>

{app_cta(pg, T)}
{contact_teaser(pg, T['contact_h2'])}
'''
    return pg, layout(pg, T['title'], T['description'], 'app', body)


def field_error(name, **msgs):
    """Fehlerzeile unter einem Feld. Die Meldungen stehen als data-Attribute bereit (main.js liest sie)."""
    data = ''.join(f' data-msg-{k.replace("_", "-")}="{esc(v)}"' for k, v in msgs.items())
    return f'<span class="ferr" role="alert" data-err="{name}"{data} hidden>{icon("circle-alert", 15, 2)}<span></span></span>'


def page_kontakt():
    pg = Page('kontakt/index.html', 1)
    u = pg.url
    T = C.KONTAKT
    def info_val(v, h):
        if not h:
            return f'<span class="info-val">{esc(v)}</span>'
        ext = ' target="_blank" rel="noopener"' if h.startswith('http') else ''
        return f'<a class="info-val" href="{esc(h)}"{ext}>{esc(v)}</a>'
    info = ''.join(f'<div class="info-row">{icon(ic, 22)}<div class="info-txt"><span class="eyebrow">{esc(l)}</span>{info_val(v, h)}</div></div>'
                   for ic, l, v, h in C.CONTACT_INFO)
    topics = ''.join(f'<button type="button" class="tab" aria-pressed="{"true" if i == 0 else "false"}" data-topic-btn="{esc(C_DE.CONTACT_TOPICS[i])}">{esc(t)}</button>' for i, t in enumerate(C.CONTACT_TOPICS))
    body = f'''
<section class="kontakt-sec" data-screen-label="Kontakt">
  <div class="wrap grid2 grid-1-115 align-start">
    <div class="kontakt-left">
      <div class="eyebrow" {reveal(0)}>{esc(T['eyebrow'])}</div>
      <h1 class="h1-60" {reveal(80)}>{md(T['h1'], pg)}</h1>
      <p class="body-18 lh165 dmax" {dmax(420)} {reveal(160)}>{md(T['text'], pg)}</p>
      <div class="info" {reveal(220)}>{info}</div>
    </div>

    <div class="form-box" {reveal(120)}>
      <form class="cform" action="{pg.url('kontakt/senden.php')}" method="post" novalidate data-form>
        <div class="ftopic">
          <span class="ftopic-label" id="ftopic-label">{esc(T['topic_label'])}</span>
          <div class="tabs" role="group" aria-labelledby="ftopic-label">{topics}</div>
          <input type="hidden" name="thema" value="{esc(C_DE.CONTACT_TOPICS[0])}"><input type="hidden" name="sprache" value="{pg.lang}">
        </div>
        <div class="grid2 grid-1-1 fgrid">
          <label class="field">{esc(T['name_label'])}<input name="name" autocomplete="name" placeholder="{esc(T['name_placeholder'])}" required>{field_error('name', empty=T['err_name'])}</label>
          <label class="field">{esc(T['email_label'])}<input type="email" name="email" autocomplete="email" placeholder="{esc(T['email_placeholder'])}" required>{field_error('email', empty=T['err_email_empty'], invalid=T['err_email_invalid'])}</label>
        </div>
        <label class="field" data-animal-field>{esc(T['animal_label'])} <span class="field-hint">{esc(T['animal_hint'])}</span><input name="tier" placeholder="{esc(T['animal_placeholder'])}"></label>
        <label class="field">{esc(T['msg_label'])}<textarea name="msg" rows="6" placeholder="{esc(T['msg_placeholder'])}" required></textarea>{field_error('msg', empty=T['err_msg'])}</label>
        <div class="consent-wrap">
          <label class="consent"><input type="checkbox" name="consent" value="1" required><span>{md(T['consent'], pg)}</span></label>
          {field_error('consent', empty=T['err_consent'])}
          <span class="req-note">{esc(T['required_note'])}</span>
        </div>
        <div class="hp" aria-hidden="true"><label>Website<input name="website" tabindex="-1" autocomplete="off"></label></div>
        <div class="fsubmit">
          <button type="submit" class="btn btn-primary btn-arrow">{esc(T['submit'])}<span aria-hidden="true">→</span></button>
          <span class="ferr ferr--send" role="alert" data-send-error hidden>{icon('circle-alert', 15, 2)}<span>{md(T['err_send'].format(email=C.EMAIL), pg)}</span></span>
        </div>
      </form>
      <div class="fsuccess" data-success hidden tabindex="-1">
        <div class="fsuccess-icon">{icon('check', 28, 1.75)}</div>
        <h2>{md(T['success_h2'], pg)}</h2>
        <p class="dmax" {dmax(400)}>{md(T['success_text'], pg)}</p>
        <button type="button" class="btn-small btn-small--lg" data-reset>{esc(T['success_button'])}</button>
      </div>
    </div>
  </div>
</section>
'''
    return pg, layout(pg, T['title'], T['description'], 'kontakt', body)


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
      {eyebrow(C.LEGAL['eyebrow'])}
      <h1 class="h1-60"><strong>{esc(doc['title'])}</strong></h1>
    </div>
    <div class="legal-grid">
      <nav class="toc" aria-label="{esc(C.LEGAL['toc'])}" data-toc>{eyebrow(C.LEGAL['toc'], 'mb12')}{toc_html}</nav>
      <div class="legal-text dmax" {dmax(720)} {reveal(100)}>{blocks}<p class="stand">{esc(doc['stand'])}</p></div>
    </div>
  </div>
</section>
'''
    return pg, layout(pg, doc['title'], f'{doc["title"]} – {SITE_NAME}', key, body)


# ------------------------------------------------------------------ Build
def main():
    global NOINDEX, C, LANG
    ap = argparse.ArgumentParser(description='Website bauen')
    ap.add_argument('--live', action='store_true', help='ohne noindex (echte Website)')
    ap.add_argument('--import', dest='imp', metavar='CSV', help='MorphMarket-Export übernehmen')
    ap.add_argument('--fotos', action='store_true', help='Nachzuchten-Fotos von MorphMarket lokal ablegen')
    args = ap.parse_args()
    NOINDEX = not args.live
    if args.imp:
        import_csv(args.imp)
    if args.imp or args.fotos:
        fetch_photos(load_animals())

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    for d in ('img', 'fonts', 'assets'):
        shutil.copytree(SRC / d, DIST / d)
    shutil.copy(SRC / 'php' / 'senden.php', DIST / 'senden.php.tmp')

    gallery = load_gallery()
    pages = []
    for LANG, C in (('de', C_DE), ('en', C_EN)):
        animals = load_animals()
        missing = [a['id'] for a in animals if not a['photo']]
        if missing and LANG == 'de':
            msg = (f'Kein lokales Foto für {", ".join(missing)} – erst "python3 build.py --fotos" ausführen '
                   '(im Teststand werden solange die MorphMarket-Fotos eingebunden).')
            if args.live:
                raise SystemExit(msg)
            print('Hinweis: ' + msg)
        lang_pages = [page_home(animals, gallery), page_projekte(), page_nachzuchten(animals), page_kornnatter(), page_app(), page_kontakt(),
                      page_legal('impressum', C.IMPRESSUM), page_legal('datenschutz', C.DATENSCHUTZ)]
        lang_pages += [page_projekt(i) for i in range(len(C.PROJECTS))]
        pages += lang_pages
    for pg, out in pages:
        target = DIST / pg.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(out, encoding='utf-8')
    (DIST / 'senden.php.tmp').rename(DIST / 'kontakt' / 'senden.php')
    robots = 'User-agent: *\nDisallow: /\n' if NOINDEX else 'User-agent: *\nAllow: /\n'
    (DIST / 'robots.txt').write_text(robots, encoding='utf-8')
    mode = 'Teststand (noindex)' if NOINDEX else 'LIVE (indexierbar)'
    print(f'{len(pages)} Seiten (DE + EN), {len(animals)} Nachzuchten, {mode} → {DIST}')


if __name__ == '__main__':
    main()
