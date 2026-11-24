# DrumScore Editor Documentation

Official documentation and help content for DrumScore Editor - the music notation application for pipe band drumming.

## About

This repository contains user-facing documentation, tutorials, and help content for DrumScore Editor (DSE). Documentation will be available in multiple languages to serve our international pipe band community.

## Status

The user guide for **Drum Score Editor 4** is being written in `en/v4/`. English is the commitment
for the 4.0 release; French and German follow. The guide for 3.6 and earlier is the older site at
[docs.drumscore.scot](https://docs.drumscore.scot/index.html), whose source is
[alanwhite/docnext](https://github.com/alanwhite/docnext).

## How the guide is put together

- **A page is a topic.** `topics.json` lists the topic ids in reading order. Each page in
  `<language>/v4/` starts with a few lines saying which topic it is:

  ```
  ---
  title: Starting a Score
  topic: new-score
  summary: Making a new score: its type, time signature, tempo and layout.
  draft: true
  ---
  ```

- **The application opens topics, not pages.** Help in the application goes to
  `https://support.drumscore.scot/docs/go/<its version>/<language>/<topic>/`, which sends the
  reader on to the page for that version, in English where the page is not translated yet. So a file here can be renamed or a
  page reorganised without breaking any copy of the application already installed. A topic id,
  once released, is never removed or given a new meaning.
- **Links inside a page** are written `[Settings](topic:settings)` for another page and
  `![The New Score window](images/new-score.png)` for a picture. A file to download, such as an example score, is kept under
  `examples/` and linked as `[the score](examples/v4/name.ds)`. Anything else that is not a full
  web address is refused by the build.
- **A translation** is the same file name in `fr/v4/` or `de/v4/` with the same `topic`. Pages not
  yet translated fall back to English by themselves.

## One guide per version

The site holds a copy of the guide for each released version of the application, with a version
menu at the top of every page, and a copy for the version being prepared. `versions.json` says
which they are.

- **`main` is the version being prepared** (`next` in `versions.json`). It is published at
  `/docs/next/`, marked as not released, left out of the version menu and hidden from search
  engines. Write the pages for a release here before the software goes out.
- **A released version's pages are on its branch**, `release/4.0.0`. They can still change: a
  known issue found after release is a pull request to that branch.
- **Somebody who types the address, or follows an old link to `/docs/v4/…`, gets the latest.**
  Help in the application opens the pages for the version that is running. Version 4.0.0 was made
  before this and asks for `go/v4/`, which is pinned to the 4.0.0 pages for good.

To release the guide with the software, say for 4.0.1:

1. `git push origin main:release/4.0.1`
2. In `versions.json` on `main`, add `{"version": "4.0.1", "branch": "release/4.0.1"}` to the end
   of `released` and set `next` to the version after it.
3. Build with `--release` and publish.

A fix that belongs to several versions is made on each branch that needs it.

## Building it

```
python3 -m venv .venv && .venv/bin/pip install -r build/requirements.txt
.venv/bin/python build/build.py            # writes site/
.venv/bin/python build/build.py --offline  # links that open from a folder, no web server
.venv/bin/python build/build.py --release  # refuses while an English page of a released version is a draft
```

The build needs Python, one library and git (a released version is read from its branch, so
`git fetch` first), and nothing else. It stops, saying why, if a topic has no
English page, a page names an unknown topic, or a link or picture goes nowhere.

## Contributing

We welcome two types of contributions:

### 📝 Documentation Contributions

Help us create and improve user documentation! You can contribute directly to this repository.

- Fix typos and errors
- Improve explanations and add examples
- Translate documentation to other languages
- Add screenshots and diagrams

**Get started:** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. No legal agreements required for documentation contributions.

### 💻 Code Contributions

Interested in contributing to DrumScore Editor's source code?

The main application code is in a private repository. Before gaining access, you'll need to review and sign our Contributor License Agreement (CLA).

**Get started:** 
1. Read [CONTRIBUTING_TO_CODE.md](CONTRIBUTING_TO_CODE.md) for the process
2. Review the [CLA](CLA.md) to understand the terms
3. Contact alan@drumscore.scot to begin the process

## Questions?

- **Documentation**: Open an issue or email alan@drumscore.scot
- **Code contributions**: alan@drumscore.scot
- **General support**: Visit [drumscore.scot](https://drumscore.scot)

## License

See [LICENSE](LICENSE.md) for terms of use.

---

**DrumScore Editor** - Music notation software for pipe band drummers
