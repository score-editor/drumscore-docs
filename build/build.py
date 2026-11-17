#!/usr/bin/env python3
"""Build the Drum Score Editor help site from the Markdown in the language folders.

    build/build.py [--out site] [--release] [--offline]

What it writes, under the output folder (served as https://support.drumscore.scot/docs/):

    v4/<lang>/<topic>/index.html      a page, for every language that has written it
    v4/<lang>/index.html              the overview topic
    go/v4/<lang>/<topic>/index.html   the address the application opens: a redirect to the page
                                      in that language, or to the English page when it is not
                                      translated yet
    assets/, images/                  the stylesheet and the pictures
    topics.json                       the topic ids, for anything that wants to check itself

The application names TOPICS, never pages (see topics.json). So a page may be renamed, split or
moved between releases and every copy of the application already installed still arrives.

--release refuses to build while any English page is still marked `draft: true`.
--offline writes links that name index.html, so the pages open from a folder with no web server.

The build stops, saying why, when: a topic has no English page; a page names a topic that is not
in topics.json; two pages claim one topic; a link to another page or a picture goes nowhere.
"""
import argparse
import html
import json
import pathlib
import re
import shutil
import sys

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = "v4"
LANGUAGES = {"en": "English", "fr": "Français", "de": "Deutsch"}
FALLBACK = "en"
# The few words the frame around a page says, per language.
WORDS = {
    "en": {"guide": "User Guide", "product": "Drum Score Editor 4", "draft": "This page is still being written.",
           "previous": "Previous", "next": "Next", "moved": "Opening the help page.", "go": "Go to the page",
           "contents": "Contents"},
    "fr": {"guide": "Guide de l’utilisateur", "product": "Drum Score Editor 4", "draft": "Cette page est en cours de rédaction.",
           "previous": "Précédent", "next": "Suivant", "moved": "Ouverture de la page d’aide.", "go": "Aller à la page",
           "contents": "Sommaire"},
    "de": {"guide": "Benutzerhandbuch", "product": "Drum Score Editor 4", "draft": "Diese Seite wird noch geschrieben.",
           "previous": "Zurück", "next": "Weiter", "moved": "Die Hilfeseite wird geöffnet.", "go": "Zur Seite",
           "contents": "Inhalt"},
}
OVERVIEW = "overview"


class Refused(Exception):
    pass


def read_page(path):
    """A page is `---`, `key: value` lines, `---`, then Markdown."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise Refused(f"{path.relative_to(ROOT)}: no front matter (--- title/topic/summary ---)")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise Refused(f"{path.relative_to(ROOT)}: front matter line without a colon: {line!r}")
        meta[key.strip()] = value.strip()
    for needed in ("title", "topic"):
        if not meta.get(needed):
            raise Refused(f"{path.relative_to(ROOT)}: front matter has no {needed}")
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta, m.group(2)


def load(topics):
    """pages[lang][topic] = (meta, markdown, path)"""
    pages = {}
    for lang in LANGUAGES:
        found = {}
        folder = ROOT / lang / VERSION
        for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
            meta, body = read_page(path)
            topic = meta["topic"]
            if topic not in topics:
                raise Refused(f"{path.relative_to(ROOT)}: topic {topic!r} is not in topics.json")
            if topic in found:
                raise Refused(f"{path.relative_to(ROOT)}: topic {topic!r} is already claimed by "
                              f"{found[topic][2].relative_to(ROOT)}")
            found[topic] = (meta, body, path)
        pages[lang] = found
    missing = [t for t in topics if t not in pages[FALLBACK]]
    if missing:
        raise Refused(f"no English page for: {', '.join(missing)}")
    return pages


def page_dir(lang, topic):
    """Where a topic's page lives, relative to the site root."""
    return f"{VERSION}/{lang}" if topic == OVERVIEW else f"{VERSION}/{lang}/{topic}"


def relative(from_dir, to_dir, offline):
    """A link from one folder of the site to another, never absolute: the site is served under
    /docs/ today and may be opened from a folder tomorrow."""
    a, b = (from_dir.split("/") if from_dir else []), to_dir.split("/")
    while a and b and a[0] == b[0]:
        a, b = a[1:], b[1:]
    link = "/".join([".."] * len(a) + b)
    link = (link + "/") if link else "./"
    return link + ("index.html" if offline else "")


LINK = re.compile(r'(href|src)="([^"]+)"')


def rewrite_links(body_html, lang, topic, pages, source, offline, site_images):
    """In a page, `topic:new-score` links to that topic in this language (English if it is not
    translated), and `images/x.png` to the picture. Anything else that is not a full address or an
    anchor is refused: a relative link that happens to work is one that breaks when a page moves."""
    here = page_dir(lang, topic)

    def fix(m):
        attr, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if target.startswith("topic:"):
            name, _, anchor = target[len("topic:"):].partition("#")
            if name not in pages[FALLBACK]:
                raise Refused(f"{source.relative_to(ROOT)}: link to unknown topic {name!r}")
            to_lang = lang if name in pages[lang] else FALLBACK
            link = relative(here, page_dir(to_lang, name), offline)
            return f'{attr}="{link}{"#" + anchor if anchor else ""}"'
        if target.startswith("images/"):
            if not (ROOT / target).is_file():
                raise Refused(f"{source.relative_to(ROOT)}: picture {target!r} does not exist")
            site_images.add(target)
            up = "/".join([".."] * len(here.split("/")))
            return f'{attr}="{up}/{target}"'
        raise Refused(f"{source.relative_to(ROOT)}: link {target!r} is neither topic:<id>, images/<file>, "
                      f"an anchor nor a full address")

    return LINK.sub(fix, body_html)


def render(template, lang, topic, topics, pages, offline, site_images):
    meta, body, source = pages[lang][topic]
    words = WORDS[lang]
    md = markdown.Markdown(extensions=["tables", "toc", "attr_list", "admonition", "fenced_code", "sane_lists"])
    body_html = rewrite_links(md.convert(body), lang, topic, pages, source, offline, site_images)
    here = page_dir(lang, topic)
    up = "/".join([".."] * len(here.split("/")))

    def title_of(t):
        m = pages[lang].get(t) or pages[FALLBACK][t]
        return html.escape(m[0]["title"])

    def link_to(t):
        to_lang = lang if t in pages[lang] else FALLBACK
        return relative(here, page_dir(to_lang, t), offline)

    nav = "\n".join(
        "<li" + (' class="here"' if t == topic else "") + f'><a href="{link_to(t)}">{title_of(t)}</a></li>'
        for t in topics)
    at = topics.index(topic)
    step = []
    if at > 0:
        step.append(f'<a class="previous" href="{link_to(topics[at - 1])}">'
                    f'<span>{words["previous"]}</span>{title_of(topics[at - 1])}</a>')
    if at + 1 < len(topics):
        step.append(f'<a class="next" href="{link_to(topics[at + 1])}">'
                    f'<span>{words["next"]}</span>{title_of(topics[at + 1])}</a>')
    languages = " · ".join(
        f'<span class="here">{name}</span>' if code == lang
        else f'<a href="{relative(here, page_dir(code, topic), offline)}" lang="{code}">{name}</a>'
        for code, name in LANGUAGES.items() if topic in pages[code])
    filled = template
    for key, value in {
        "lang": lang, "title": html.escape(meta["title"]), "product": words["product"], "guide": words["guide"],
        "summary": html.escape(meta.get("summary", "")), "assets": f"{up}/assets", "nav": nav,
        "home": link_to(OVERVIEW), "contents": words["contents"],
        "draft": f'<p class="draft">{words["draft"]}</p>' if meta["draft"] else "",
        "body": body_html, "step": "\n".join(step), "languages": languages,
    }.items():
        filled = filled.replace("{{" + key + "}}", value)
    left = re.findall(r"\{\{\w+\}\}", filled.replace(body_html, ""))
    if left:
        raise Refused(f"template has names the build does not fill: {left}")
    return here, filled


REDIRECT = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<meta http-equiv="refresh" content="0; url={to}">
<link rel="canonical" href="{to}">
<meta name="robots" content="noindex">
</head>
<body>
<p>{moved} <a href="{to}">{go}</a>.</p>
</body>
</html>
"""


def build(out, release=False, offline=False):
    topics = json.loads((ROOT / "topics.json").read_text(encoding="utf-8"))["topics"]
    if len(set(topics)) != len(topics) or OVERVIEW not in topics:
        raise Refused("topics.json: the ids must be distinct and include 'overview'")
    pages = load(topics)
    if release:
        drafts = [t for t in topics if pages[FALLBACK][t][0]["draft"]]
        if drafts:
            raise Refused(f"--release: still marked draft in English: {', '.join(drafts)}")
    template = (ROOT / "build" / "page.html").read_text(encoding="utf-8")
    if out.exists():
        shutil.rmtree(out)
    site_images = set()
    written = 0
    for lang in LANGUAGES:
        for topic in topics:
            if topic in pages[lang]:
                here, page = render(template, lang, topic, topics, pages, offline, site_images)
                (out / here).mkdir(parents=True, exist_ok=True)
                (out / here / "index.html").write_text(page, encoding="utf-8")
                written += 1
            # the address the application opens, in every language whether translated or not
            to_lang = lang if topic in pages[lang] else FALLBACK
            go = f"go/{VERSION}/{lang}/{topic}"
            (out / go).mkdir(parents=True, exist_ok=True)
            (out / go / "index.html").write_text(REDIRECT.format(
                lang=to_lang, title=html.escape(pages[to_lang][topic][0]["title"]),
                to=relative(go, page_dir(to_lang, topic), offline),
                moved=WORDS[to_lang]["moved"], go=WORDS[to_lang]["go"]), encoding="utf-8")
    shutil.copytree(ROOT / "build" / "assets", out / "assets")
    for picture in sorted(site_images):
        (out / picture).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / picture, out / picture)
    (out / "topics.json").write_text(json.dumps({"version": VERSION, "topics": topics}, indent=1) + "\n",
                                     encoding="utf-8")
    # the folder's own front door goes to the English overview
    (out / "index.html").write_text(REDIRECT.format(
        lang=FALLBACK, title=WORDS[FALLBACK]["guide"], to=relative("", page_dir(FALLBACK, OVERVIEW), offline),
        moved=WORDS[FALLBACK]["moved"], go=WORDS[FALLBACK]["go"]), encoding="utf-8")
    counts = ", ".join(f"{lang} {len(pages[lang])}" for lang in LANGUAGES)
    drafts = sum(1 for t in topics if pages[FALLBACK][t][0]["draft"])
    print(f"built {written} pages ({counts}) and {len(topics) * len(LANGUAGES)} topic addresses into {out}; "
          f"{drafts} of {len(topics)} English pages are drafts")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=str(ROOT / "site"))
    ap.add_argument("--release", action="store_true")
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    try:
        build(pathlib.Path(args.out), args.release, args.offline)
    except Refused as why:
        print(f"refused: {why}", file=sys.stderr)
        sys.exit(1)
