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
  `https://support.drumscore.scot/docs/go/v4/<language>/<topic>/`, which sends the reader on to
  the page, in English where the page is not translated yet. So a file here can be renamed or a
  page reorganised without breaking any copy of the application already installed. A topic id,
  once released, is never removed or given a new meaning.
- **Links inside a page** are written `[Settings](topic:settings)` for another page and
  `![The New Score window](images/new-score.png)` for a picture. Anything else that is not a full
  web address is refused by the build.
- **A translation** is the same file name in `fr/v4/` or `de/v4/` with the same `topic`. Pages not
  yet translated fall back to English by themselves.

## Building it

```
python3 -m venv .venv && .venv/bin/pip install -r build/requirements.txt
.venv/bin/python build/build.py            # writes site/
.venv/bin/python build/build.py --offline  # links that open from a folder, no web server
.venv/bin/python build/build.py --release  # refuses while any English page is still a draft
```

The build needs Python and one library, and nothing else. It stops, saying why, if a topic has no
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
