#!/usr/bin/env python3
"""Build the Drum Score Editor help site from the Markdown in the language folders.

    build/build.py [--out site] [--release] [--offline]

The site holds one copy of the guide for each released version of the application, and one for the
version being prepared. versions.json says which they are:

    released   the versions in people's hands, oldest first, each with the branch its pages are
               kept on (release/4.0.0). The last one is the latest.
    next       the version being prepared. Its pages are the files in this checkout.
    pinned     the addresses older copies of the application open, and the version each one
               goes to for good (v4 is what 4.0.0 asks for).

What it writes, under the output folder (served as https://support.drumscore.scot/docs/):

    <version>/<lang>/<topic>/index.html     a page, for every language that has written it
    <version>/<lang>/index.html             the overview topic
    <version>/images/, <version>/examples/  that version's pictures and files
    next/...                                the same for the version being prepared: marked as not
                                            released, left out of the version menu, hidden from
                                            search engines
    go/<version>/<lang>/<topic>/index.html  the address the application opens: a redirect to the
                                            page for ITS version in that language, or to the English
                                            page when it is not translated yet. The version being
                                            prepared has one too, going to next/, so a build of the
                                            application made before its release arrives somewhere.
    go/v4/...                               what 4.0.0 opens: pinned, see above
    go/next/...                             what a development build opens
    v4/<lang>/<topic>/index.html            the address the guide had before it kept versions: a
                                            redirect to the latest
    assets/                                 the stylesheet
    topics.json, versions.json              the latest topic ids and the versions, for anything
                                            that wants to check itself

The application names TOPICS, never pages (see topics.json). So a page may be renamed, split or
moved between releases and every copy of the application already installed still arrives.

--release refuses to build while any English page of a RELEASED version is still marked
`draft: true`. The version being prepared may have drafts: that is what preparing it is.
--offline writes links that name index.html, so the pages open from a folder with no web server.

The build stops, saying why, when: a topic has no English page; a page names a topic that is not
in topics.json; two pages claim one topic; a link to another page or a picture goes nowhere; a
released version's branch cannot be found.
"""
import argparse
import html
import json
import pathlib
import re
import io
import shutil
import subprocess
import sys
import tarfile
import tempfile

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = "v4"  # the folder a language keeps its pages in, on every branch
BEFORE_VERSIONS = "v4"  # the address the guide had before it kept versions
NEXT = "next"
BASE = "https://support.drumscore.scot/docs/"
LANGUAGES = {"en": "English", "fr": "Français", "de": "Deutsch"}
FALLBACK = "en"
# The few words the frame around a page says, per language.
WORDS = {
    "en": {"guide": "User Guide", "product": "Drum Score Editor 4", "draft": "This page is still being written.",
           "previous": "Previous", "next": "Next", "moved": "Opening the help page.", "go": "Go to the page",
           "contents": "Contents",
           "version": "Version {v}", "latest": "latest", "unreleased": "not yet released",
           "older": "This is the guide for version {v}.", "newer": "The latest version is {latest}.",
           "coming": "This is the guide for version {v}, which has not been released yet.",
           "current": "The guide for the released version is {latest}."},
    "fr": {"guide": "Guide de l’utilisateur", "product": "Drum Score Editor 4", "draft": "Cette page est en cours de rédaction.",
           "previous": "Précédent", "next": "Suivant", "moved": "Ouverture de la page d’aide.", "go": "Aller à la page",
           "contents": "Sommaire",
           "version": "Version {v}", "latest": "la plus récente", "unreleased": "pas encore publiée",
           "older": "Ceci est le guide de la version {v}.", "newer": "La version la plus récente est la {latest}.",
           "coming": "Ceci est le guide de la version {v}, qui n’est pas encore publiée.",
           "current": "Le guide de la version publiée est celui de la {latest}."},
    "de": {"guide": "Benutzerhandbuch", "product": "Drum Score Editor 4", "draft": "Diese Seite wird noch geschrieben.",
           "previous": "Zurück", "next": "Weiter", "moved": "Die Hilfeseite wird geöffnet.", "go": "Zur Seite",
           "contents": "Inhalt",
           "version": "Version {v}", "latest": "aktuell", "unreleased": "noch nicht veröffentlicht",
           "older": "Dies ist das Handbuch für Version {v}.", "newer": "Die aktuelle Version ist {latest}.",
           "coming": "Dies ist das Handbuch für Version {v}, die noch nicht veröffentlicht ist.",
           "current": "Das Handbuch der veröffentlichten Version ist {latest}."},
}
OVERVIEW = "overview"


class Refused(Exception):
    pass


class Edition:
    """The guide for one version of the application.

    label    the folder it is written to: the version, or `next` for the one being prepared
    version  the version of the application it describes
    kind     "latest", "older" or "next"
    root     where its pages, pictures and topics.json are: this checkout for the version being
             prepared, the files of its branch for a released one
    """

    def __init__(self, label, version, kind, root):
        self.label, self.version, self.kind, self.root = label, version, kind, root
        self.topics = json.loads((root / "topics.json").read_text(encoding="utf-8"))["topics"]
        if len(set(self.topics)) != len(self.topics) or OVERVIEW not in self.topics:
            raise Refused(f"{self.named(root / 'topics.json')}: the ids must be distinct and include 'overview'")
        self.pages = load(self)
        self.files = set()

    def named(self, path):
        """A file of this edition, as somebody would look for it."""
        where = path.relative_to(self.root)
        return str(where) if self.kind == "next" else f"{where} (version {self.version})"

    def has(self, lang, topic):
        return topic in self.pages[lang]

    def spoken(self, lang, topic):
        """The language a topic is read in by somebody who asked for `lang`."""
        return lang if self.has(lang, topic) else FALLBACK


def read_page(path, edition):
    """A page is `---`, `key: value` lines, `---`, then Markdown."""
    text = path.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
    if not m:
        raise Refused(f"{edition.named(path)}: no front matter (--- title/topic/summary ---)")
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise Refused(f"{edition.named(path)}: front matter line without a colon: {line!r}")
        meta[key.strip()] = value.strip()
    for needed in ("title", "topic"):
        if not meta.get(needed):
            raise Refused(f"{edition.named(path)}: front matter has no {needed}")
    meta["draft"] = meta.get("draft", "false").lower() == "true"
    return meta, m.group(2)


def load(edition):
    """pages[lang][topic] = (meta, markdown, path)"""
    pages = {}
    for lang in LANGUAGES:
        found = {}
        folder = edition.root / lang / SOURCE
        for path in sorted(folder.glob("*.md")) if folder.is_dir() else []:
            meta, body = read_page(path, edition)
            topic = meta["topic"]
            if topic not in edition.topics:
                raise Refused(f"{edition.named(path)}: topic {topic!r} is not in topics.json")
            if topic in found:
                raise Refused(f"{edition.named(path)}: topic {topic!r} is already claimed by "
                              f"{edition.named(found[topic][2])}")
            found[topic] = (meta, body, path)
        pages[lang] = found
    missing = [t for t in edition.topics if t not in pages[FALLBACK]]
    if missing:
        raise Refused(f"version {edition.version}: no English page for: {', '.join(missing)}")
    return pages


def page_dir(edition, lang, topic):
    """Where a topic's page lives, relative to the site root."""
    return f"{edition.label}/{lang}" if topic == OVERVIEW else f"{edition.label}/{lang}/{topic}"


def same_topic(edition, lang, topic):
    """Where somebody reading `topic` in `lang` lands in another edition: the same topic, or that
    edition's overview when it has no such topic."""
    topic = topic if topic in edition.topics else OVERVIEW
    return page_dir(edition, edition.spoken(lang, topic), topic)


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


def rewrite_links(body_html, edition, lang, topic, source, offline):
    """In a page, `topic:new-score` links to that topic in this language (English if it is not
    translated), `images/x.png` to the picture, and `examples/x.ds` to a file to download. Anything else that is not a full address or an
    anchor is refused: a relative link that happens to work is one that breaks when a page moves."""
    here = page_dir(edition, lang, topic)
    pages = edition.pages

    def fix(m):
        attr, target = m.group(1), m.group(2)
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return m.group(0)
        if target.startswith("topic:"):
            name, _, anchor = target[len("topic:"):].partition("#")
            if name not in pages[FALLBACK]:
                raise Refused(f"{edition.named(source)}: link to unknown topic {name!r}")
            link = relative(here, page_dir(edition, edition.spoken(lang, name), name), offline)
            return f'{attr}="{link}{"#" + anchor if anchor else ""}"'
        if target.startswith(("images/", "examples/")):
            if not (edition.root / target).is_file():
                raise Refused(f"{edition.named(source)}: file {target!r} does not exist")
            edition.files.add(target)
            # a version's pictures are its own: they are redrawn when the application changes
            up = "/".join([".."] * (len(here.split("/")) - 1))
            return f'{attr}="{up}/{target}"'
        raise Refused(f"{edition.named(source)}: link {target!r} is neither topic:<id>, images/<file>, examples/<file>, "
                      f"an anchor nor a full address")

    return LINK.sub(fix, body_html)


def render(template, edition, lang, topic, released, offline):
    """`released` is every released edition, oldest first; the last is the latest."""
    topics, pages = edition.topics, edition.pages
    latest = released[-1]
    meta, body, source = pages[lang][topic]
    words = WORDS[lang]
    md = markdown.Markdown(extensions=["tables", "toc", "attr_list", "admonition", "fenced_code", "sane_lists"])
    body_html = rewrite_links(md.convert(body), edition, lang, topic, source, offline)
    here = page_dir(edition, lang, topic)
    up = "/".join([".."] * len(here.split("/")))

    def title_of(t):
        m = pages[lang].get(t) or pages[FALLBACK][t]
        return html.escape(m[0]["title"])

    def link_to(t):
        return relative(here, page_dir(edition, edition.spoken(lang, t), t), offline)

    def link_in(other):
        return relative(here, same_topic(other, lang, topic), offline)

    # THE VERSION MENU: the released versions, newest first. The one being prepared is in it only
    # on its own pages, so nobody finds their way to it from a released one.
    listed = ([edition] if edition.kind == NEXT else []) + list(reversed(released))
    entries = []
    for other in listed:
        tag = (f' <span class="tag">{words["latest"]}</span>' if other is latest
               else f' <span class="tag">{words["unreleased"]}</span>' if other.kind == NEXT else "")
        entries.append(f'<li class="here"><span>{other.version}{tag}</span></li>' if other is edition
                       else f'<li><a href="{link_in(other)}">{other.version}{tag}</a></li>')
    versions = (f'<details class="versions"><summary>{words["version"].format(v=edition.version)}</summary>\n'
                '<ul>\n' + "\n".join(entries) + '\n</ul>\n</details>')
    to_latest = f'<a href="{link_in(latest)}">' + "{sentence}</a>"
    if edition.kind == "older":
        notice = (f'<p class="notice">{words["older"].format(v=edition.version)} '
                  + to_latest.format(sentence=words["newer"].format(latest=latest.version)) + '</p>')
    elif edition.kind == NEXT:
        notice = (f'<p class="notice">{words["coming"].format(v=edition.version)} '
                  + to_latest.format(sentence=words["current"].format(latest=latest.version)) + '</p>')
    else:
        notice = ""
    # ONE ADDRESS PER TOPIC FOR A SEARCH ENGINE: the latest. An older version points at it, and the
    # one being prepared is not to be listed at all.
    if edition.kind == NEXT:
        head = '<meta name="robots" content="noindex">'
    elif offline:
        head = ""
    else:
        head = f'<link rel="canonical" href="{BASE}{same_topic(latest, lang, topic)}/">'

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
        else f'<a href="{relative(here, page_dir(edition, code, topic), offline)}" lang="{code}">{name}</a>'
        for code, name in LANGUAGES.items() if topic in pages[code])
    filled = template
    for key, value in {
        "lang": lang, "title": html.escape(meta["title"]), "product": words["product"], "guide": words["guide"],
        "summary": html.escape(meta.get("summary", "")), "assets": f"{up}/assets", "nav": nav,
        "home": link_to(OVERVIEW), "contents": words["contents"],
        "draft": f'<p class="draft">{words["draft"]}</p>' if meta["draft"] else "",
        "body": body_html, "step": "\n".join(step), "languages": languages,
        "versions": versions, "notice": notice, "head": head,
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


def number(version):
    """4.0.10 comes after 4.0.9."""
    if not re.fullmatch(r"\d+(\.\d+)+", version):
        raise Refused(f"versions.json: {version!r} is not a version number")
    return tuple(int(part) for part in version.split("."))


def files_of(branch, into):
    """Unpack a released version's files. The copy on the server is tried first: that is what the
    site is built from, and a local branch of the same name may be behind it."""
    for ref in (f"origin/{branch}", branch):
        packed = subprocess.run(["git", "-C", str(ROOT), "archive", ref], capture_output=True)
        if packed.returncode == 0:
            with tarfile.open(fileobj=io.BytesIO(packed.stdout)) as tar:
                tar.extractall(into, filter="data")
            return
    raise Refused(f"versions.json: no branch {branch!r} here or on origin (git fetch?)")


def editions(scratch):
    """Every released edition, oldest first, then the one being prepared."""
    said = json.loads((ROOT / "versions.json").read_text(encoding="utf-8"))
    listed = said["released"]
    if not listed:
        raise Refused("versions.json: nothing is released")
    numbers = [number(each["version"]) for each in listed] + [number(said["next"])]
    if numbers != sorted(set(numbers)):
        raise Refused("versions.json: the versions must be distinct and in order, `next` after them all")
    released = []
    for at, each in enumerate(listed):
        root = scratch / each["version"]
        root.mkdir()
        files_of(each["branch"], root)
        released.append(Edition(each["version"], each["version"],
                                "latest" if at == len(listed) - 1 else "older", root))
    by_version = {edition.version: edition for edition in released}
    pinned = {}
    for address, version in said.get("pinned", {}).items():
        if version not in by_version:
            raise Refused(f"versions.json: {address!r} is pinned to {version!r}, which is not released")
        pinned[address] = by_version[version]
    return released, Edition(NEXT, said["next"], NEXT, ROOT), pinned


def redirect(out, at, to_dir, lang, title, offline):
    (out / at).mkdir(parents=True, exist_ok=True)
    (out / at / "index.html").write_text(REDIRECT.format(
        lang=lang, title=html.escape(title), to=relative(at, to_dir, offline),
        moved=WORDS[lang]["moved"], go=WORDS[lang]["go"]), encoding="utf-8")


def build(out, release=False, offline=False):
    with tempfile.TemporaryDirectory() as scratch:
        released, coming, pinned = editions(pathlib.Path(scratch))
        latest = released[-1]
        if release:
            for edition in released:
                drafts = [t for t in edition.topics if edition.pages[FALLBACK][t][0]["draft"]]
                if drafts:
                    raise Refused(f"--release: version {edition.version} is released and still marked "
                                  f"draft in English: {', '.join(drafts)}")
        template = (ROOT / "build" / "page.html").read_text(encoding="utf-8")
        if out.exists():
            shutil.rmtree(out)
        written = 0
        # THE ADDRESSES THE APPLICATION OPENS, and the edition each is answered from: a version's
        # own; the version being prepared, which goes to next/ until it is released; a development
        # build; and the addresses pinned for copies made before the guide kept versions.
        answered = {edition.version: edition for edition in released}
        answered[coming.version] = coming
        answered[NEXT] = coming
        answered.update(pinned)
        for edition in released + [coming]:
            for lang in LANGUAGES:
                for topic in edition.topics:
                    if edition.has(lang, topic):
                        here, page = render(template, edition, lang, topic, released, offline)
                        (out / here).mkdir(parents=True, exist_ok=True)
                        (out / here / "index.html").write_text(page, encoding="utf-8")
                        written += 1
            for file in sorted(edition.files):
                (out / edition.label / file).parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(edition.root / file, out / edition.label / file)
        addresses = 0
        for address, edition in answered.items():
            for lang in LANGUAGES:
                for topic in edition.topics:
                    # in every language, whether translated or not
                    spoken = edition.spoken(lang, topic)
                    redirect(out, f"go/{address}/{lang}/{topic}", page_dir(edition, spoken, topic), spoken,
                             edition.pages[spoken][topic][0]["title"], offline)
                    addresses += 1
        # WHERE THE GUIDE WAS before it kept versions, for bookmarks and links from elsewhere: the
        # latest, whatever that is by then.
        for lang in LANGUAGES:
            for topic in latest.topics:
                spoken = latest.spoken(lang, topic)
                if spoken == lang:
                    was = f"{BEFORE_VERSIONS}/{lang}" if topic == OVERVIEW else f"{BEFORE_VERSIONS}/{lang}/{topic}"
                    redirect(out, was, page_dir(latest, lang, topic), lang,
                             latest.pages[lang][topic][0]["title"], offline)
        shutil.copytree(ROOT / "build" / "assets", out / "assets")
        (out / "topics.json").write_text(
            json.dumps({"version": latest.version, "topics": latest.topics}, indent=1) + "\n", encoding="utf-8")
        (out / "versions.json").write_text(json.dumps({
            "latest": latest.version, "released": [edition.version for edition in released],
            "next": coming.version}, indent=1) + "\n", encoding="utf-8")
        # the folder's own front door goes to the latest English overview
        redirect(out, "", page_dir(latest, FALLBACK, OVERVIEW), FALLBACK, WORDS[FALLBACK]["guide"], offline)
        counts = "; ".join(
            f"{edition.version}{' (next)' if edition.kind == NEXT else ''}: "
            + ", ".join(f"{lang} {len(edition.pages[lang])}" for lang in LANGUAGES)
            for edition in released + [coming])
        drafts = sum(1 for t in coming.topics if coming.pages[FALLBACK][t][0]["draft"])
        print(f"built {written} pages ({counts}) and {addresses} topic addresses into {out}; "
              f"latest is {latest.version}; {drafts} of {len(coming.topics)} English pages of "
              f"{coming.version} are drafts")


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
