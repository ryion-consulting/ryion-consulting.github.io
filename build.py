#!/usr/bin/env python3
"""Build every page of the site: python3 build.py

    index.html                       the home page
    <App>/index.html                 each product page            (copy in site/content.py)
    <App>/<page>.html                guides, FAQ, support, privacy (copy in site/pages/<App>/)
    appstore.html                    App Store media, for review on this Mac only

The look is one stylesheet and one small script at the root, almanac.css and
almanac.js, written by hand. Pages are plain static HTML with relative links,
so the site works at any address. The build also makes the JPEG thumbnails
for App Store screenshots (with `sips`), so run it on the Mac after the
screenshots in <App>/AppStore/Screenshots/ change.
"""
import html
import math
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "site"))
from content import APPS, HOME, PRINCIPLES  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
MAIL = "ryionconsulting@gmail.com"
YEAR = 2026
FONTS = ("family=Fraunces:ital,opsz,wght,SOFT@0,9..144,300..700,0..100;1,9..144,300..700,0..100"
         "&family=Instrument+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500")

# The secondary pages of each app, in menu order, and the store names of the apps'
# folders in ~/Documents/App Store Artifacts (see README).
DOC_PAGES = {
    "BillCompass": ["features", "guide", "sync", "faq", "support", "privacy"],
    "WhereaboutsCompass": ["support", "privacy"],
    "CinematicTeleprompter": ["support", "privacy"],
}


def esc(s):
    return html.escape(s, quote=True)


def fill(s, app, here):
    """Resolve {L} (the app's folder) and {A} (its assets) for a page in `here`.

    `here` is "" for the home page and an app's folder name for that app's pages.
    """
    if here == "":
        folder = f"{app['dir']}/"
    elif here == app["dir"]:
        folder = ""
    else:
        folder = f"../{app['dir']}/"
    return s.replace("{L}", folder).replace("{A}", folder + "assets/")


def up(here):
    """The path from a page in `here` back to the root."""
    return "" if here == "" else "../"


def platforms(app, sep=" · "):
    return sep.join(app["platforms"] + ([app["extra"]] if app["extra"] else []))


def head(title, desc, here, icon=None, robots=None):
    r = up(here)
    extra = ""
    if icon:
        extra += f'\n<link rel="icon" href="{icon}">\n<link rel="apple-touch-icon" href="{icon}">'
    if robots:
        extra += f'\n<meta name="robots" content="{robots}">'
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">{extra}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS.replace('&', '&amp;')}&amp;display=swap">
<link rel="stylesheet" href="{r}almanac.css">
<script>document.documentElement.classList.add("js")</script>
</head>
"""


# ───────────────────────────── Shared pieces ─────────────────────────────

def rose():
    """A compass rose drawn in hairlines: a ring of words, a ring of ticks, a 16-point star and a needle."""
    def pt(deg, r):
        a = math.radians(deg)
        return f"{r * math.sin(a):.2f},{-r * math.cos(a):.2f}"

    ticks = "".join(
        f'<line x1="0" y1="{-(160 if d % 30 == 0 else 166 if d % 15 == 0 else 170)}" x2="0" y2="-176" transform="rotate({d})"/>'
        for d in range(0, 360, 3))
    star = ""
    # Half-winds first, then ordinals, then cardinals on top: (first angle, step, length, base radius, base half-angle).
    for first, step, length, inner, spread in ((22.5, 45, 70, 46, 11.25), (45, 90, 96, 36, 22.5), (0, 90, 128, 24, 45)):
        for k in range(int(360 // step)):
            d = first + k * step
            star += (f'<polygon class="dark" points="0,0 {pt(d, length)} {pt(d - spread, inner)}"/>'
                     f'<polygon class="light" points="0,0 {pt(d, length)} {pt(d + spread, inner)}"/>')
    letters = "".join(f'<text class="card" x="{x}" y="{y}">{c}</text>'
                      for c, x, y in (("N", 0, -139), ("E", 146, 7), ("S", 0, 153), ("W", -146, 7)))
    words = "No accounts · No ads · No analytics · Your data stays with you · " * 2
    return f"""<svg class="rose-svg" viewBox="-200 -200 400 400">
  <defs><path id="ring" d="M0,-183 A183,183 0 1,1 -0.01,-183"/></defs>
  <g class="rose-words"><text><textPath href="#ring" textLength="1148">{words.upper()}</textPath></text></g>
  <circle r="176"/><circle r="104"/>
  <g class="rose-ticks">{ticks}</g>
  <g class="rose-star">{star}</g>
  {letters}
  <g class="rose-needle"><polygon class="north" points="0,-118 6,0 -6,0"/><polygon class="south" points="0,118 6,0 -6,0"/></g>
  <circle class="pin" r="5"/>
</svg>"""


def footer(here):
    r = up(here)

    def link(app, page):
        return fill("{L}" + page, app, here)

    apps = "".join(f'<li><a href="{link(a, "")}">{a["name"]}</a></li>' for a in APPS)
    priv = "".join(f'<li><a href="{link(a, "privacy.html")}">{a["name"]}</a></li>' for a in APPS)
    supp = "".join(f'<li><a href="{link(a, "support.html")}">{a["name"]}</a></li>' for a in APPS)
    return f"""<footer class="foot">
  <div class="foot-top">
    <p class="foot-line">Small apps that <em>keep to themselves.</em></p>
    <nav aria-label="Footer">
      <div><h3>The apps</h3><ul>{apps}</ul></div>
      <div><h3>Privacy policies</h3><ul>{priv}</ul></div>
      <div><h3>Support</h3><ul>{supp}</ul></div>
      <div><h3>Contact</h3><ul><li><a href="mailto:{MAIL}">{MAIL}</a></li></ul></div>
    </nav>
  </div>
  <p class="foot-mark" aria-hidden="true">Ryion</p>
  <p class="foot-base"><span>© {YEAR} Ryion</span><a class="review-link" href="{r}appstore.html" hidden>App Store media (this Mac only)</a></p>
</footer>
<script src="{r}almanac.js" defer></script>
</body>
</html>
"""


def app_nav(app, here, page):
    """The app's own menu. Same-page anchors point at the product page from its other pages."""
    links = ""
    for text, href in app["nav"]:
        target = fill(href, app, here)
        if target.startswith("#") and page != "index":
            target = "index.html" + target
        current = ' aria-current="page"' if target == f"{page}.html" else ""
        links += f'<a href="{target}"{current}>{text}</a>'
    return links


def masthead(app, here, page):
    r = up(here)
    icon = fill("{A}icon.png", app, here)
    return f"""<a class="skip" href="#main">Skip to the content</a>
<header class="mast">
  <a class="wordmark" href="{r}index.html">Ryion</a>
  <a class="crumb" href="index.html"><img src="{icon}" width="256" height="256" alt="">{app['name']}</a>
  <nav aria-label="{app['name']}">{app_nav(app, here, page)}</nav>
</header>
"""


def app_foot(app, here, page):
    links = ""
    for text, href in app["foot"]:
        target = fill(href, app, here)
        if target.startswith("#") and page != "index":
            target = "index.html" + target
        links += f'<a href="{target}">{text}</a>'
    return f'<div class="app-foot"><span>{app["footline"]}</span><nav aria-label="{app["name"]} pages">{links}</nav></div>\n'


def others(app, here):
    cards = ""
    for o in APPS:
        if o is app:
            continue
        cards += (f'<a class="other hue-{o["hue"]}" href="{fill("{L}index.html", o, here)}">'
                  f'<img src="{fill("{A}icon.png", o, here)}" width="256" height="256" alt="" loading="lazy">'
                  f'<span><small>{o["no"]}</small><b>{o["name"]}</b><em>{o["blurb"]}</em></span><i aria-hidden="true">→</i></a>')
    return f'<section class="others"><h2>Also from Ryion</h2><div class="others-grid">{cards}</div></section>\n'


# ───────────────────────────── Product page sections ─────────────────────────────

def fields(items, app, here):
    return '<dl class="fields">' + "".join(f"<div><dt>{dt}</dt><dd>{fill(dd, app, here)}</dd></div>" for dt, dd in items) + "</dl>"


def section(app, here, n, s):
    kind = s["kind"]
    sid = f' id="{s["id"]}"' if s.get("id") else ""
    title = f'<h2>{s["title"]}</h2>' if s.get("title") else ""
    lead = f'<p class="lead">{s["lead"]}</p>' if s.get("lead") else ""
    after = f'<p class="after">{fill(s["after"], app, here)}</p>' if s.get("after") else ""
    label = f'<p class="sec-label"><span class="sec-no">{n:02d}</span>{s["label"]}</p>'
    head_ = f'<header class="sec-head" data-reveal>{label}{title}{lead}</header>'
    body = ""

    if kind == "three":
        lis = "".join(f"<li data-reveal><b>{b}</b><span>{t}</span></li>" for b, t in s["items"])
        body = f'<ol class="three">{lis}</ol>{after}'
    elif kind == "features":
        lis = ""
        for b, t, href in s["items"]:
            inner = f"<b>{b}</b><span>{t}</span>"
            if href:
                inner = f'<a href="{fill(href, app, here)}">{inner}<i aria-hidden="true">→</i></a>'
            lis += f'<li class="card" data-reveal>{inner}</li>'
        body = f'<ul class="defs">{lis}</ul>{after}'
    elif kind == "steps":
        lis = "".join(f"<li>{fill(t, app, here)}</li>" for t in s["items"])
        tip = f'<div class="tip">{s["tip"]}</div>' if s.get("tip") else ""
        fig = ""
        if s.get("figure"):
            src, alt = s["figure"]
            fig = (f'<figure class="steps-fig" data-reveal><div class="phone"><img src="{fill(src, app, here)}" '
                   f'width="600" height="1304" alt="{esc(alt)}" loading="lazy" decoding="async"></div></figure>')
        body = f'<div class="steps-wrap"><div><ol class="steps">{lis}</ol>{tip}</div>{fig}</div>'
    elif kind == "gallery":
        figs = "".join(
            f'<figure class="plate"><div class="phone"><img src="{fill(src, app, here)}" width="600" height="1304" '
            f'alt="{esc(alt)}" loading="lazy" decoding="async"></div><figcaption>{cap}</figcaption></figure>'
            for src, alt, cap in s["items"])
        body = f'<div class="gallery">{figs}</div>'
    elif kind == "fields":
        body = fields(s["items"], app, here)
    elif kind == "list":
        body = '<ul class="notes">' + "".join(f"<li>{t}</li>" for t in s["items"]) + "</ul>"
    elif kind == "prose":
        for tag, val in s["blocks"]:
            body += fields(val, app, here) if tag == "fields" else f"<{tag}>{val}</{tag}>"
        body = f'<div class="prose">{body}</div>'
    elif kind == "spread":
        figs = ""
        shapes = []
        for src, alt, cap, w, h in s["figures"]:
            shape = "desk" if w > h * 1.45 else ("wide" if w > h else "tablet")
            shapes.append(shape)
            figs += (f'<figure class="screen {shape}" data-reveal><img src="{fill(src, app, here)}" width="{w}" height="{h}" '
                     f'alt="{esc(alt)}" loading="lazy" decoding="async"><figcaption>{cap}</figcaption></figure>')
        layout = "n1" if len(shapes) == 1 else ("n2 mixed" if "tablet" in shapes else "n2")
        body = f'{after}<div class="screens {layout}">{figs}</div>'
    elif kind == "pledge":
        ps = "".join(f'<div class="pledge tone-{tone}" data-reveal><span class="stamp">{stamp}</span><p>{fill(t, app, here)}</p></div>'
                     for stamp, t, tone in s["pledges"])
        mid = f'<p class="lead aside">{s["lead"]}</p>' if s.get("lead") else ""
        head_ = f'<header class="sec-head" data-reveal>{label}{title}</header>'
        body = f"{ps}{mid}{after}"
    elif kind == "pricing":
        cols = "".join(f'<div class="col"><b>{t}</b><ul>' + "".join(f"<li>{i}</li>" for i in items) + "</ul></div>"
                       for t, items in s["cols"])
        body = (f'<div class="pledge tone-hue" data-reveal><span class="stamp">{s["stamp"]}</span><p>{s["text"]}</p></div>'
                f'<div class="locks">{cols}</div>{after}')
    elif kind == "faq":
        body = '<div class="faq">' + "".join(
            f'<details><summary>{q}</summary><div class="answer"><p>{fill(a, app, here)}</p></div></details>'
            for q, a in s["items"]) + "</div>"

    return f'<section class="sec kind-{kind}"{sid}>\n{head_}\n<div class="sec-body">{body}</div>\n</section>\n'


# ───────────────────────────── Pages ─────────────────────────────

def home():
    here = ""
    index = "".join(
        f'<li><a href="#{a["slug"]}"><span>{a["no"]}</span><b>{a["name"]}</b><i>{platforms(a)}</i></a></li>' for a in APPS)
    entries = ""
    for a in APPS:
        facts = "".join(f"<li><b>{b}</b><span>{t}</span></li>" for b, t in a["facts"])
        (s1, _), (s2, _) = a["hero"]
        page = fill("{L}index.html", a, here)
        entries += f"""<article class="entry hue-{a['hue']}" id="{a['slug']}">
  <div class="entry-text" data-reveal>
    <p class="entry-no"><span>N°</span>{a['no']}</p>
    <h2><a href="{page}">{a['name']}</a></h2>
    <p class="blurb">{a['blurb']}</p>
    <ul class="facts">{facts}</ul>
    <p class="entry-foot"><a class="more" href="{page}">Read about {a['name']} <i aria-hidden="true">→</i></a><span class="meta">{platforms(a)}</span></p>
  </div>
  <a class="entry-art" href="{page}" tabindex="-1" aria-hidden="true">
    <span class="art-no">{a['no']}</span>
    <img class="icon" src="{fill('{A}icon.png', a, here)}" width="256" height="256" alt="">
    <span class="phone p1"><img src="{fill(s1, a, here)}" width="600" height="1304" alt="" loading="lazy" decoding="async"></span>
    <span class="phone p2"><img src="{fill(s2, a, here)}" width="600" height="1304" alt="" loading="lazy" decoding="async"></span>
  </a>
</article>
"""
    ledger = "".join(f'<div data-reveal><dt>{k}</dt><dd>{v}</dd></div>' for k, v in PRINCIPLES)
    return head(HOME["title"], HOME["desc"], here) + f"""<body class="home">
<a class="skip" href="#apps">Skip to the apps</a>
<header class="mast">
  <a class="wordmark" href="index.html">Ryion</a>
  <nav aria-label="Main"><a href="#apps">The apps</a><a href="#rules">House rules</a><a href="mailto:{MAIL}">Contact</a></nav>
</header>

<section class="hero">
  <div class="hero-text">
    <p class="eyebrow">Apps for iPhone, iPad and Mac</p>
    <h1>{HOME['h1'][0]} <em>{HOME['h1'][1]}.</em></h1>
    <p class="lead">{HOME['lead']}</p>
  </div>
  <div class="rose" aria-hidden="true">{rose()}</div>
  <ol class="index" aria-label="The apps">{index}</ol>
</section>

<main id="apps">
{entries}</main>

<section class="rules" id="rules">
  <header data-reveal>
    <p class="eyebrow">House rules</p>
    <h2>The same rules, <em>in every app.</em></h2>
  </header>
  <dl class="rules-ledger">{ledger}</dl>
</section>

""" + footer(here)


def product(a):
    here = a["dir"]
    (s1, a1), (s2, a2) = a["hero"]
    ctas = "".join(f'<a class="btn{" solid" if i == 0 else ""}" href="{fill(h, a, here)}">{t}</a>' for i, (t, h) in enumerate(a["ctas"]))
    sections = "".join(section(a, here, i, s) for i, s in enumerate(a["sections"], 1))
    return head(a["title"], a["desc"], here, icon="assets/icon.png") + f"""<body class="app hue-{a['hue']}">
{masthead(a, here, "index")}
<section class="app-hero">
  <div class="app-hero-text">
    <p class="eyebrow"><span>N° {a['no']}</span>{platforms(a)}</p>
    <h1>{a['h1']}</h1>
    <p class="lead">{a['tagline']}</p>
    <div class="ctas">{ctas}</div>
    <p class="note">Coming to the App Store</p>
  </div>
  <div class="app-hero-art">
    <span class="art-no" aria-hidden="true">{a['no']}</span>
    <img class="icon" src="assets/icon.png" width="256" height="256" alt="{esc(a['icon_alt'])}">
    <figure class="phone p1"><img src="{fill(s1, a, here)}" width="600" height="1304" alt="{esc(a1)}" decoding="async"></figure>
    <figure class="phone p2"><img src="{fill(s2, a, here)}" width="600" height="1304" alt="{esc(a2)}" decoding="async"></figure>
  </div>
</section>

<main id="main">
{sections}</main>

{others(a, here)}{app_foot(a, here, "index")}""" + footer(here)


def doc(a, page):
    """A guide, FAQ, support or privacy page: its fragment in the app's masthead and footer."""
    here = a["dir"]
    src = open(os.path.join(ROOT, "site", "pages", a["dir"], f"{page}.html"), encoding="utf-8").read()
    title = re.search(r"<!-- title: (.*?) -->", src).group(1)
    desc = re.search(r"<!-- description: (.*?) -->", src)
    body = re.sub(r"<!-- (title|description): .*? -->\n", "", src)
    return head(title, desc.group(1) if desc else a["desc"], here, icon="assets/icon.png") + f"""<body class="app doc-page page-{page} hue-{a['hue']}">
{masthead(a, here, page)}
<main id="main" class="doc">
{body}</main>

{others(a, here)}{app_foot(a, here, page)}""" + footer(here)


# ───────────────────────────── App Store media (local review) ─────────────────────────────

DEVICES = [("iPhone-6.9", "iPhone 6.9″", "iphone"), ("iPad-13", "iPad 13″", "ipad"), ("Mac", "Mac", "mac")]
STORE_NAME = {"BillCompass": "Bill Compass", "WhereaboutsCompass": "Whereabouts Compass", "CinematicTeleprompter": "Cinematic Teleprompter"}
PREVIEWS = {"iPhone-6.9": ("iPhone-6.9.mp4", 886, 1920), "iPad-13": ("iPad-13.mp4", 1200, 1600)}


def png_size(path):
    with open(path, "rb") as f:
        head_ = f.read(24)
    return int.from_bytes(head_[16:20], "big"), int.from_bytes(head_[20:24], "big")


def thumbnail(png, jpg, width):
    """A JPEG of `png`, `width` pixels wide, made again whenever the PNG is newer."""
    if os.path.exists(jpg) and os.path.getmtime(jpg) >= os.path.getmtime(png):
        return
    subprocess.run(["sips", "--resampleWidth", str(width), "-s", "format", "jpeg", "-s", "formatOptions", "80",
                    png, "--out", jpg], check=True, capture_output=True)


def store_media():
    """Every App Store screenshot, as thumbnails linking to the full PNGs, and the App Preview
    videos from _artifacts (git-ignored, so they exist only on this Mac)."""
    blocks, toc = "", ""
    for a in APPS:
        base = os.path.join(ROOT, a["dir"], "AppStore", "Screenshots")
        if not os.path.isdir(base):
            continue
        thumbs_dir = os.path.join(ROOT, a["dir"], "assets", "store")
        os.makedirs(thumbs_dir, exist_ok=True)
        wanted = set()
        rows = ""
        for folder, label, prefix in DEVICES:
            d = os.path.join(base, folder)
            if not os.path.isdir(d):
                continue
            files = sorted(f for f in os.listdir(d) if f.endswith(".png"))
            if not files:
                continue
            w, h = png_size(os.path.join(d, files[0]))
            orient = "portrait" if h > w else "landscape"
            tw = 480 if prefix == "iphone" else (600 if orient == "portrait" else 800)
            figs = ""
            if folder in PREVIEWS:
                name, vw, vh = PREVIEWS[folder]
                src = f"_artifacts/{STORE_NAME[a['dir']].replace(' ', '%20')}/App%20Previews/{name}"
                figs += (f'<figure class="clip"><video controls playsinline preload="metadata" width="{vw}" height="{vh}" src="{src}#t=3" '
                         f'onerror="this.closest(\'figure\').remove()"></video><figcaption>App Preview</figcaption></figure>')
            for f in files:
                png = os.path.join(d, f)
                jpg_name = f"{prefix}-{f[:-4]}.jpg"
                wanted.add(jpg_name)
                thumbnail(png, os.path.join(thumbs_dir, jpg_name), tw)
                pw, ph = png_size(png)
                nice = re.sub(r"^\d+-", "", f[:-4]).replace("-", " ").capitalize()
                rel = f"{a['dir']}/AppStore/Screenshots/{folder}/{f}"
                figs += (f'<figure><a href="{rel}"><img src="{a["dir"]}/assets/store/{jpg_name}" width="{tw}" height="{round(tw * ph / pw)}" '
                         f'loading="lazy" alt="{esc(a["name"])} on {label}: {esc(nice)}"></a>'
                         f'<figcaption><b>{f[:2]}</b> {esc(nice)}</figcaption></figure>')
            rows += (f'<div class="media-row {orient} dev-{prefix}"><h3>{label}<small>{len(files)} screenshots · {pw} × {ph} PNG</small></h3>'
                     f'<div class="strip" tabindex="0">{figs}</div></div>')
        # Thumbnails of screenshots that no longer exist.
        for old in os.listdir(thumbs_dir):
            if old.endswith(".jpg") and old not in wanted:
                os.remove(os.path.join(thumbs_dir, old))
        toc += f'<li><a href="#store-{a["slug"]}">{a["name"]}</a></li>'
        blocks += (f'<article class="media hue-{a["hue"]}" id="store-{a["slug"]}"><h2><img src="{a["dir"]}/assets/icon.png" alt="">{a["name"]}</h2>{rows}</article>\n')
    here = ""
    return head("App Store media — Ryion", "App Store screenshots and previews, for review.", here, robots="noindex") + f"""<body class="store-page">
<a class="skip" href="#main">Skip to the content</a>
<header class="mast">
  <a class="wordmark" href="index.html">Ryion</a>
  <nav aria-label="Apps"><ul class="store-toc">{toc}</ul></nav>
</header>
<main id="main" class="store">
  <header class="store-head">
    <p class="eyebrow">For review on this Mac</p>
    <h1>App Store <em>media</em></h1>
    <p class="lead">Every screenshot as it goes to App Store Connect. Tap one for the full-size PNG. The App Preview videos live outside the repository and play only from the local preview server.</p>
    <p class="store-off" hidden>This page is meant for the local preview server (<code>python3 serve.py</code>), where the App Preview videos can play.</p>
  </header>
{blocks}</main>
""" + footer(here)


def write(rel, text):
    with open(os.path.join(ROOT, rel), "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


if __name__ == "__main__":
    write("index.html", home())
    for app in APPS:
        write(f"{app['dir']}/index.html", product(app))
        for page in DOC_PAGES[app["dir"]]:
            write(f"{app['dir']}/{page}.html", doc(app, page))
    write("appstore.html", store_media())
