"""Build projectcutover.com from the copy in content.py and the pieces in a pieces folder.

    python3 _build/build.py                      # the site, into the repo root, with the pieces in _build/pieces/
    python3 _build/build.py --out DIR --pieces DIR  # a preview somewhere else, e.g. with a held piece in it

Jekyll skips folders that start with an underscore, so nothing in _build/ is served.
A component links from the map only when its piece is in the pieces folder."""
import argparse, html, re, shutil, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import content as C  # noqa: E402
from mdlite import convert, inline  # noqa: E402

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,400..800&family=JetBrains+Mono:wght@500;700&display=swap">')
THEME_EARLY = ("<script>try{var t=localStorage.getItem('pc-theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>")
SCRIPT = '''<script>
(function(){var r=document.documentElement,b=document.getElementById('theme');if(!b)return;
function dark(){return r.getAttribute('data-theme')!=='light'}
function label(){b.textContent=dark()?'Light':'Dark';b.setAttribute('aria-label',dark()?'Switch to the light theme':'Switch to the dark theme')}
b.addEventListener('click',function(){var n=dark()?'light':'dark';r.setAttribute('data-theme',n);try{localStorage.setItem('pc-theme',n)}catch(e){}label()});label();})();
</script>'''


def esc(s):
    return html.escape(s, quote=True)


def slugify(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


FRQZ = ('<svg class="frqz-mark" viewBox="0 0 18 18" width="14" height="14" aria-hidden="true">'
        '<rect x="0" y="3" width="3" height="12" fill="currentColor"/><rect x="7" y="0" width="3" height="18" fill="currentColor"/>'
        '<rect x="11" y="5" width="3" height="8" fill="currentColor"/><rect x="14" y="7" width="3" height="4" fill="currentColor"/></svg>')


def chrome(current, title, desc, body, path, image='/assets/iris-480.png'):
    nav = ''.join(f'<a href="{href}"{" aria-current=page" if key == current else ""}>{esc(name)}</a>'
                  for key, name, href in C.NAV)
    canonical = f'https://projectcutover.com{path}'
    f = C.FOOT
    foot = f'''<footer class="foot"><div class="wrap"><div class="cols">
<div><div class="lock"><img class="iris" src="/assets/iris-64.png" alt="" width="40" height="40"><div><b>Project Cutover</b></div></div>
<div class="credit">{FRQZ}<span>{esc(f["credit"])}</span></div></div>
<div><div class="label">{esc(f["read_h"])}</div><ul>{"".join(f'<li><a href="{h}">{esc(n)}</a></li>' for n, h in f["read"])}</ul></div>
<div><div class="label">{esc(f["contact_h"])}</div><ul>{"".join(f'<li><a href="{h}">{esc(n)}</a></li>' for n, h in f["contact"])}</ul></div>
</div><div class="bottom">{esc(f["copyright"])}</div></div></footer>'''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://projectcutover.com{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/assets/iris-64.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/iris-192.png">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{THEME_EARLY}
</head>
<body>
<a class="skip" href="#main">{esc(C.SKIP)}</a>
<header class="top"><div class="wrap">
<a class="brand" href="/"><img class="iris" src="/assets/iris-64.png" alt="" width="30" height="30"><span>Project Cutover</span></a>
<nav class="nav" aria-label="Site">{nav}<a class="btn sm" href="/newsletter/">{esc(C.SUBSCRIBE)}</a></nav>
<button class="toggle" id="theme" type="button">Light</button>
</div></header>
<main id="main">
{body}
</main>
{foot}
{SCRIPT}
</body>
</html>
'''


# ---------------------------------------------------------------- the map
def comp_name(c, written):
    if c['slug'] in written:
        return f'<a href="/delivery/{c["slug"]}/">{esc(c["name"])}</a>'
    return f'<span>{esc(c["name"])}</span>'


def comp_list(comps, written):
    return '<ul class="comps">' + ''.join(f'<li>{comp_name(c, written)}</li>' for c in comps) + '</ul>'


def layer(name):
    return next(l for l in C.LAYERS if l['name'] == name)


def home_layers(written):
    rows = ''.join(f'<div class="layer"><h3>{esc(l["name"])}</h3><div><p>{esc(l["short"])}</p>{comp_list(l["comps"], written)}</div></div>'
                   for l in C.LAYERS)
    return f'<div class="layers">{rows}</div>'


def map_drawing(written):
    def phase(n):
        l = layer(n)
        return f'<div class="phase"><span class="label">{esc(n)}</span>{comp_list(l["comps"], written)}</div>'
    pj = layer('Project')
    phases = ''.join(phase(n) for n in ('Plan', 'Run', 'Cutover', 'Handover'))
    inner_pj = f'<div class="nest"><span class="label">Project</span>{comp_list(pj["comps"], written)}<div class="phases">{phases}</div></div>'
    pg = layer('Program')
    inner_pg = f'<div class="nest"><span class="label">Program</span>{comp_list(pg["comps"], written)}{inner_pj}</div>'
    pf = layer('Portfolio')
    outer = f'<div class="nest"><span class="label">Portfolio</span>{comp_list(pf["comps"], written)}{inner_pg}</div>'
    return f'<div class="map" role="group" aria-label="{esc(C.DELIVERY["map_label"])}">{outer}</div>'


# ---------------------------------------------------------------- pages
def btn(label_href, ghost=False):
    label, href = label_href
    return f'<a class="btn{" ghost" if ghost else ""}" href="{href}">{esc(label)}</a>'


def home(written):
    h = C.HOME
    first = btn(h['first'], ghost=True) if h['first'][1].split('/')[-2] in written else ''
    body = f'''<section class="wrap hero">
<div><h1 class="disp">{esc(h["headline"])}</h1><p class="stand">{inline(h["stand"])}</p>
<div class="ctas">{btn((h["cta"], h["cta_href"]))}{first}</div></div>
<img class="iris" src="/assets/iris-480.png" alt="" width="280" height="280">
</section>
<section class="sec band s-map"><div class="wrap">
<h2 class="h2">{esc(h["layers_h"])}</h2>{f'<p class="stand" style="margin-top:12px">{inline(h["layers_p"])}</p>' if h["layers_p"] else ""}
{home_layers(written)}
<p style="margin:24px 0 0"><a href="/delivery/">{esc(h["layers_link"])}</a></p>
</div></section>
<section class="sec s-who"><div class="wrap">
<h2 class="h2">{esc(h["who_h"])}</h2><p class="stand" style="margin:12px 0 16px">{inline(h["who_p"])}</p>
<a href="{h["who_link"][1]}">{esc(h["who_link"][0])}</a>
</div></section>
{signup_band()}'''
    return chrome('home', h['title'], h['desc'], body, '/')


def signup_band():
    n = C.SIGNUP
    return f'''<section class="sec band s-sign"><div class="wrap signup">
<div><h2 class="h2">{esc(n["h"])}</h2><p class="stand" style="margin:12px 0 0">{inline(n["p"])}</p></div>
<a class="btn" href="{C.SUBSTACK}">{esc(n["btn"])}</a></div></section>'''


def delivery(written):
    d = C.DELIVERY
    toc = ''.join(f'<a href="#{slugify(l["name"])}">{esc(l["name"])}</a>' for l in C.LAYERS)
    secs = ''
    for l in C.LAYERS:
        comps = ''
        for c in l['comps']:
            title = (f'<a href="/delivery/{c["slug"]}/">{esc(c["name"])}</a>' if c['slug'] in written else esc(c['name']))
            comps += (f'<div class="comp" id="{c["slug"]}"><div></div><div><h3>{title}</h3><p>{inline(c["what"])}</p>'
                      f'<p class="q">{esc(c["q"])}</p><p class="aka"><b>{esc(d["aka_label"])}</b> {esc(c["aka"])}</p></div></div>')
        secs += (f'<section class="lsec" id="{slugify(l["name"])}"><header><h2>{esc(l["name"])}</h2><p>{inline(l["long"])}</p></header>{comps}</section>')
    body = f'''<section class="wrap" style="padding-block:72px 0">
<h1 class="h1">{esc(d["h1"])}</h1><p class="stand" style="margin-top:20px"><strong style="color:var(--ink)">{esc(d["sub"])}</strong> {inline(d["stand"])}</p>
{map_drawing(written)}
<nav class="toc" aria-label="{esc(d["toc_label"])}">{toc}</nav>
</section>
<div class="wrap" style="padding-bottom:96px">{secs}</div>
{signup_band()}'''
    return chrome('delivery', d['title'], d['desc'], body, '/delivery/')


def watch(written):
    w = C.WATCH
    rows = ''
    for e in w['episodes']:
        rows += (f'<article class="ep"><div class="thumb"><img src="/assets/iris-64.png" alt="" width="28" height="28"><div class="t">{esc(e["title"])}</div></div>'
                 f'<div class="body"><h3><a href="{e["url"]}">{esc(e["title"])}</a></h3><p style="margin:0">{e["minutes"]} min · {esc(e["component"])} · '
                 f'<a href="{e["piece"]}">Read the piece</a></p></div></article>')
    grid = f'<div class="grid2" style="margin-top:40px">{rows}</div>' if rows else ''
    head = f'<div><h1 class="h1">{esc(w["h1"])}</h1><p class="stand" style="margin-top:20px">{inline(w["stand"])}</p></div>'
    plate = ('<div class="plate" aria-hidden="true"><img class="iris" src="/assets/iris-192.png" alt="" width="88" height="88">'
             '<span class="label" style="color:var(--ink)">Project Cutover</span></div>')
    top = head if rows else f'<div class="vhead">{head}{plate}</div>'
    body = f'<section class="wrap page">{top}{grid}</section>\n{signup_band()}'
    return chrome('watch', w['title'], w['desc'], body, '/watch/')


def simple(key, page, path):
    b = page.get('button')
    body = f'''<section class="wrap" style="padding-block:72px 120px">
<h1 class="h1">{esc(page["h1"])}</h1>
<div class="prose" style="margin-top:28px">{convert(page["body"])}</div>
{f'<p style="margin-top:28px">{btn(b)}</p>' if b else ''}
</section>'''
    return chrome(key, page['title'], page['desc'], body, path)


def about():
    a = C.ABOUT
    intro, *rest = re.split(r'\n## ', a['body'])
    rows = ''
    for r in rest:
        h, _, b = r.partition('\n')
        rows += f'<div class="row"><h2>{esc(h.strip())}</h2><div>{convert(b)}</div></div>'
    body = f'''<section class="wrap page">
<header class="phead"><h1 class="h1">{esc(a["h1"])}</h1><p class="stand">{inline(intro.strip())}</p></header>
<div class="rows">{rows}</div>
<p class="cta">{btn(a["button"])}</p></section>'''
    return chrome('about', a['title'], a['desc'], body, '/about/')


def newsletter():
    n = C.NEWSLETTER
    body = f'''<section class="wrap page">
<h1 class="h1">{esc(n["h1"])}</h1><p class="stand" style="margin:20px 0 32px">{inline(n["body"])}</p>{btn(n["button"])}
</section>'''
    return chrome('newsletter', n['title'], n['desc'], body, '/newsletter/')


def notfound():
    n = C.NOTFOUND
    body = f'''<section class="wrap page nf"><div>
<h1 class="disp">{esc(n["h1"])}</h1><p class="stand" style="margin:24px 0 32px">{inline(n["body"])}</p>{btn(n["button"])}</div>
<img class="iris" src="/assets/iris-480.png" alt="" width="200" height="200"></section>'''
    return chrome('', n['title'], n['desc'], body, '/404.html')


# ---------------------------------------------------------------- a piece
def read_piece(p):
    md = p.read_text()
    meta = {}
    md = re.sub(r'^\s*<!--.*?-->\s*', '', md, flags=re.S)
    m = re.match(r'---\n(.*?)\n---\n', md, flags=re.S)
    if m:
        for line in m.group(1).split('\n'):
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
        md = md[m.end():]
    md = re.sub(r'<!--.*?-->', '', md, flags=re.S).strip()
    return meta, md


def all_comps():
    return [(l, c) for l in C.LAYERS for c in l['comps']]


def link_or_text(c, written):
    return f'<a href="/delivery/{c["slug"]}/">{esc(c["name"])}</a>' if c['slug'] in written else esc(c['name'])


def pn_link(c, written):
    return link_or_text(c, written) if c['slug'] in written else f'<b>{esc(c["name"])}</b>'


def piece(meta, md, written):
    L = C.PIECE
    head, *secs = re.split(r'\n## ', md)
    hl = [l for l in head.strip().split('\n') if l.strip()]
    title = hl[0].lstrip('# ').strip()
    dateline, story = hl[1], hl[2:]
    seq = all_comps()
    idx = next(i for i, (_, c) in enumerate(seq) if c['slug'] == meta['slug'])
    lay, comp = seq[idx]
    by_name = {c['name']: c for _, c in seq}
    nav, body, sources, connects = [], '', '', ''
    for s in secs:
        h, _, b = s.partition('\n')
        h = h.strip()
        if h == 'Connects to':
            draws = [by_name[x.strip()] for x in meta.get('draws_on', '').split(',') if x.strip()]
            feeds = [by_name[x.strip()] for x in meta.get('feeds_into', '').split(',') if x.strip()]
            def lst(cs):
                return '<ul>' + ''.join(f'<li>{link_or_text(c, written)}</li>' for c in cs) + '</ul>'
            connects = (f'<section><h2 id="connects-to">{esc(L["connects_h"])}</h2>{convert(b)}<div class="connects">'
                        f'<div><div class="label">{esc(L["draws_on"])}</div>{lst(draws)}</div>'
                        f'<div><div class="label">{esc(L["feeds_into"])}</div>{lst(feeds)}</div></div></section>')
            nav.append(('connects-to', h))
            continue
        if h == 'Sources':
            sources = f'<section><h2 id="sources">{esc(L["sources_h"])}</h2><div class="sources">{convert(b)}</div></section>'
            nav.append(('sources', h))
            continue
        sid = slugify(h)
        nav.append((sid, h))
        html_b = convert(b.replace('{{TEMPLATE}}', '\n\nTEMPLATEBLOCK\n\n'))
        html_b = html_b.replace('<p>TEMPLATEBLOCK</p>', template_block(meta))
        body += f'<section><h2 id="{sid}">{esc(h)}</h2>{html_b}</section>'
    side = ''.join(f'<a href="#{i}">{esc(h)}</a>' for i, h in nav)
    prev_ = seq[idx - 1][1] if idx > 0 else None
    next_ = seq[idx + 1][1] if idx + 1 < len(seq) else None
    pn = ''
    if prev_:
        pn += f'<span><span class="k">{esc(L["prev"])}</span> {pn_link(prev_, written)}</span>'
    if next_:
        pn += f'<span><span class="k">{esc(L["next"])}</span> {pn_link(next_, written)}</span>'
    cover = (f'<img class="cover" src="{meta["cover"]}" alt="" width="1200" height="630">' if meta.get('cover') else '')
    words = len(re.findall(r'\w+', md))
    minutes = max(1, round(words / 230))
    art = f'''<div class="wrap pg"><aside aria-label="{esc(L["on_page"])}"><div class="label" style="margin-bottom:10px">{esc(L["on_page"])}</div>{side}</aside>
<article>
<div class="crumb"><a href="/delivery/">Delivery</a> / <a href="/delivery/#{slugify(lay["name"])}">{esc(lay["name"])}</a> / {esc(comp["name"])}</div>
<h1 class="h1">{esc(title)}</h1>
<p class="answers">{esc(comp["q"])}</p>
<div class="meta">{esc(L["meta"].format(date=meta.get("published", ""), minutes=minutes))}</div>
{cover}<div class="dateline">{esc(dateline)}</div>
{convert((chr(10)*2).join(story))}
{body}
<div class="close"><p style="margin:0 0 14px;font-weight:600">{esc(L["close_h"])}</p><a class="btn" href="{C.SUBSTACK}">{esc(L["close_btn"])}</a></div>
{connects}
{sources}
<nav class="pn" aria-label="Previous and next">{pn}</nav>
</article></div>'''
    return chrome('delivery', f'{title} · {comp["name"]} · Project Cutover', meta.get('desc', comp['q']), art, f'/delivery/{meta["slug"]}/',
                  meta.get('cover', '/assets/iris-480.png'))


def template_block(meta):
    """meta['templates']: 'Label | blank.xlsx | example.xlsx | note' entries separated by ' ;; '."""
    L = C.PIECE
    shot = f'<a href="{meta["template_shot"]}"><img class="shot" src="{meta["template_shot"]}" alt="{esc(L["dl_alt"])}" width="1500" height="502" loading="lazy"></a>' if meta.get('template_shot') else ''
    files = ''
    for entry in [e for e in meta.get('templates', '').split(';;') if e.strip()]:
        label, blank, example, note = [x.strip() for x in entry.split('|')]
        files += (f'<div class="dlf"><div><b>{esc(label)}</b><p>{inline(note)}</p></div>'
                  f'<div class="go"><a class="btn" href="{blank}" download>{esc(L["dl_btn"].format(label=label))}</a>'
                  f'<a class="ex" href="{example}" download>{esc(L["dl_example"])}</a></div></div>')
    return (f'<div class="dl"><h3 style="font-size:22px;margin:0 0 8px">{esc(meta["template_name"])}</h3>'
            f'<p style="margin:0;color:var(--ink-2)">{inline(meta.get("template_text", ""))}</p>{shot}{files}</div>')


def template_files(meta):
    out = []
    for e in meta.get('templates', '').split(';;'):
        if e.strip():
            parts = [x.strip() for x in e.split('|')]
            out += parts[1:3]
    return out


# ---------------------------------------------------------------- build
def build(out, pieces_dir):
    out.mkdir(parents=True, exist_ok=True)
    pieces = []
    if pieces_dir and pieces_dir.exists():
        for p in sorted(pieces_dir.glob('*.md')):
            meta, md = read_piece(p)
            if meta.get('slug'):
                pieces.append((meta, md, p))
    written = {m['slug'] for m, _, _ in pieces}
    pages = {
        'index.html': home(written),
        'delivery/index.html': delivery(written),
        'about/index.html': about(),
        'newsletter/index.html': newsletter(),
        '404.html': notfound(),
    }
    for meta, md, p in pieces:
        pages[f'delivery/{meta["slug"]}/index.html'] = piece(meta, md, written)
        for href in template_files(meta) + [meta[k] for k in ('template_shot', 'cover') if meta.get(k)]:
            if href:
                src = p.parent / Path(href).name
                if not src.exists():
                    print('missing', src); continue
                dst = out / href.lstrip('/')
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
    if C.SHOW_VIDEOS:
        pages['watch/index.html'] = watch(written)
    for rel, text in pages.items():
        f = out / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    if out != ROOT:
        for name in ('assets', 'CNAME'):
            src = ROOT / name
            if src.is_dir():
                shutil.copytree(src, out / name, dirs_exist_ok=True)
            elif src.exists():
                shutil.copy2(src, out / name)
    print(f'{out}: {len(pages)} pages, written: {sorted(written) or "none"}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', type=Path, default=ROOT)
    ap.add_argument('--pieces', type=Path, default=HERE / 'pieces')
    a = ap.parse_args()
    build(a.out.resolve(), a.pieces.resolve())
