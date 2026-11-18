---
title: Settings
topic: settings
summary: Every section of the Settings window: the licence, how the application looks, saving, your libraries and music fonts, recording, privacy, and what a new score starts with.
---

`Settings` holds what belongs to the application and to you, not to one score. What belongs to one score is in `File` ▸ `Score Properties…`. See [Score Properties](topic:score-properties).

**The Community Edition shows the `Licence` pane and nothing else.** Every other section on this page is part of the Studio Edition. See [Licensing](topic:licensing).

## Open Settings

- **Windows and Linux:** choose `File` ▸ `Settings`.
- **Mac:** choose `Settings…` in the application menu, or press `Cmd+,`.

In the Studio Edition the sections run along the top. Where a section has more than one pane, the panes are listed down the left.

![The Settings window, with its sections along the top](images/v4/settings-sections.png){: width="900" }

| Section | Panes |
|---|---|
| `Licence` | One pane |
| `Appearance` | `Appearance`, `Language` |
| `Files` | One pane |
| `Libraries` | `Location`, `Rudiments`, `Watermarks`, `Images`, `Music Fonts` |
| `Recording` | `Microphone`, `Takes` |
| `Privacy` | One pane |
| `New Score Defaults` | `Score`, `Notation`, `Engraving`, `Page`, `Music Font`, `Unison`, `Watermark`, `Highlighters` |

### OK and Cancel

Settings are written when you choose `OK`, and `Cancel` leaves them as they were. Three lists are the exception. Changes to your rudiment libraries, watermark pictures and music fonts are made at once, and `Cancel` does not undo them.

After `OK`, the paper, the ink and the theme change straight away. A new language, and some parts of a new theme, need a restart.

## Licence

| Control | What it does |
|---|---|
| `License Holder`, `Email`, `Issue Date` | With a licence installed: whose it is and when it was issued. They cannot be changed here. |
| `License Key` | Without a licence: the box for the key you were sent. |
| `Paste License Key` | Pastes the key from the clipboard into the box. |

Choose `OK` to install the key. A message shows the licensee and asks you to restart. The Studio Edition features appear the next time the application starts. A key that is not a licence shows `Invalid License`.

<!-- screenshot: the Settings window in the Community Edition: no sections along the top, only the Licence pane with an empty License Key box, the Paste License Key button, and OK and Cancel -->

For the rest, see [Licensing](topic:licensing).

![Settings, Licence, with a licence installed: the holder, email and issue date](images/v4/settings-licence.png){: width="700" }

## Appearance

### The Appearance pane

| Control | What it does |
|---|---|
| `macOS is set to` | On a Mac only. Shows which of `Increase contrast`, `VoiceOver` and `Zoom` are on in your system. `Open Accessibility Settings…` opens the system's own window for them. |
| `Choose time signatures with` | `Pictures` are nine small symbols. `Drop-downs` name the two numbers in text, which a screen reader can read and the system can enlarge. `Follow the system` uses drop-downs on a Mac when one of the three settings above is on, and pictures otherwise. It says which it is using now. See [Starting a Score](topic:new-score). |
| `Paper Background` | The paper behind the music on screen: `White`, `Parchment` or `Twill`. |
| `Use Pure Black Ink` | Draws the notation in pure black, on screen, in print and in every export. Use it if your printer makes a poor job of the usual dark grey. |
| `Appearance` | `Follow System` uses your system's own look, light or dark as the system is. `Light` and `Dark` hold it at one of them. `Custom` uses the theme chosen below. |
| `Custom Theme Mode` | With `Custom` only: whether to use your `Light` or your `Dark` theme. |
| `Light Mode Theme`, `Dark Mode Theme` | With `Custom` only: the theme for each mode. Choosing one also switches to that mode. |

<!-- screenshot: Settings showing Appearance ▸ Appearance on a Mac: the Accessibility group with "macOS is set to" and the three "Choose time signatures with" choices, the Paper and ink group, and the Theme group with Custom chosen so the three theme rows are live -->

### The Language pane

| Control | What it does |
|---|---|
| `Auto-detect System Language` | Uses your system's language where the application has it. While ticked, the `Language` row is greyed. |
| `Language` | English, French or German. |

Windows you open after choosing `OK` are in the new language. The menus keep the old one until you restart.

## Files

| Control | What it does |
|---|---|
| `Automatic File Saving` | Saves your changes into the score's own file in the background, about three seconds after you stop working, and at least once a minute while you keep going. A score that has never been saved has no file yet, so save it once yourself. |
| `Tell me when an older score is brought up to date` | When a score ran on to a second page in version 3, the items of its header were copied on to the later pages. Version 4 makes a header for every tune instead, so those copies are always removed when such a score is opened. Ticked, you are told, and the score stays read-only until you save it under a new name. Unticked, it is done silently and the score can be saved over its own file. See [Files and Older Scores](topic:files). |

## Libraries

### Location

| Control | What it does |
|---|---|
| `Library location` | The library folder. `Change…` chooses another. |

The library folder holds the pictures scores refer to, your watermarks, your rudiment libraries, and your header and footer designs. Put it somewhere that is backed up, or on a shared or cloud drive. When you change it and choose `OK`, you are asked whether to move what is in the old folder. Anything that could not be moved, or whose name is already taken in the new folder, is listed and left where it was.

![Settings, Libraries, Location: the library folder and its Change… button](images/v4/settings-library-location.png){: width="700" }

### Rudiments

The list shows the rudiment libraries that are open. A library whose file has gone is marked `missing`.

| Button | What it does |
|---|---|
| `New…` | Asks for a name and makes an empty library in your library folder. |
| `Add…` | Opens a `.dsl` library file you already have. |
| `Remove` | Takes the library off the list. The file is not deleted. |
| `Properties` | Changes the library's title. |
| `Move up`, `Move down` | Change the order of the libraries. |
| `Copy to Library Folder…` | Copies libraries kept elsewhere into your library folder. The originals stay where they are. |

For using a library, see [Rudiments, Rolls and Tuplets](topic:rudiments).

![Settings, Libraries, Rudiments: two libraries listed, with the buttons at the right](images/v4/settings-libraries.png){: width="700" }

### Watermarks

| Button | What it does |
|---|---|
| `Add…` | Brings in a PNG or JPEG file and asks what to call it. |
| `Remove` | Deletes the selected picture from the library, after asking. |
| `Rename…` | Gives the selected picture a new name. |

Which picture new scores use is chosen under `New Score Defaults` ▸ `Watermark`. For putting a watermark on a score, see [Text and Headers](topic:text-and-headers).

### Images

| Control | What it does |
|---|---|
| `Keep score images in the library, not inside the score file` | Ticked, a score refers to its pictures in your library folder and does not carry them. |

The score is smaller, but it opens without its pictures on a computer that does not have your library. To send one to somebody, use `File` ▸ `Export` ▸ `Export as Portable .ds…`, which is on the menu only while this box is ticked. See [Printing and Export](topic:export).

### Music Fonts

See *Music fonts* below.

## Recording

A take is a recording of you playing along with a score. Takes are assembled into a video in `File` ▸ `Studio...`.

### Microphone

| Control | What it does |
|---|---|
| `Microphone` | The input to record with. `Whatever the system hands over` uses your system's own choice. |
| `Record at` | The format: 44.1 kHz or 48.0 kHz, stereo or mono, 16-bit. |
| `Right now` | Shows what a recording would use at this moment. It says so if the microphone you chose is not connected. |
| `Count in` | `No count-in`, `One bar` or `Two bars`. The clicks are recorded with the take, and the Studio takes them off the front. |
| `While recording, play` | `Nothing`, `A click on each beat`, `The snare line` or `The whole score`. Use headphones, or whatever is played is in the take as well. `The snare line` is for recording a tenor or a bass against. |

### Takes

| Control | What it does |
|---|---|
| `Takes are kept in` | Shows the folder in use. |
| `Take folder` | `Change…` chooses a folder of your own. |
| `Keep takes with my library` | Keeps takes in your library folder instead. |
| `Kept so far` | Shows how many takes are kept and how much room they use. |
| `Remove old takes` | `Never`, `Older than 7 days`, `Older than a month` or `Older than a year`. Older takes go to the Trash each time the application starts. The newest take is never removed. |

Recordings are large, around a gigabyte an hour, so they are kept on this computer unless you choose otherwise.

## Privacy

| Control | What it does |
|---|---|
| `Share anonymous usage data` | Ticked, the application sends anonymous data about which features are used. Ticked as installed. |
| `Check for Updates` | Ticked, the application looks for a newer version in the background and tells you when there is one. Ticked as installed. `Help` ▸ `Check for Updates…` looks at once. |

## New Score Defaults

The eight panes here are the same panes as `File` ▸ `Score Properties…`.

**These settings are copied into a score when it is made.** Changing them later does not change any score you already have. Each score keeps its own copy, which you change in `Score Properties…`. The New Score window starts from them too. See [Starting a Score](topic:new-score).

Each control is described in [Score Properties](topic:score-properties). Only these are found here, or work differently here:

| Pane | Control | What it does here |
|---|---|---|
| `Score` | `Author`, `Band` | The names a new score starts with. |
| `Score` | `Header design for new scores`, `Footer design for new scores` | Which of your saved designs a new score is made with. `Built-in` is the plain one. The rows appear once you have saved a design. See [Text and Headers](topic:text-and-headers). |
| `Score` | `Reset all options to default values` | Puts the new-score defaults on all eight panes back to those the application came with. `Author` and `Band` become `Author Name` and `Band`. Your instruments and design choices are left alone. Nothing is written until `OK`. |
| `Notation` | `General Layout:`, `Inline Time Signature` | Can be changed here. In a score they are fixed when it is made. |
| `Notation` | `Anacrusis (%):` | The anacrusis the New Score window offers, as a percentage of the line. Empty means none. |
| `Notation` | The instruments | What each new score is written for. See [Instruments and Staves](topic:instruments). |
| `Engraving` | `Distribute Staff Lines Evenly` | Can always be ticked here. In a score it needs one page and one tune. |
| `Watermark` | `Set as Default` | Makes the selected library picture the one new scores use. It is marked `(default)`. |
| `Watermark` | `New scores reference the default watermark instead of embedding it (smaller files)` | Ticked, a new score names the default picture and does not carry a copy of it. |
| `Watermark` | `Manage Watermarks on This System…` | Goes to `Libraries` ▸ `Watermarks`. |
| `Highlighters` | `Reset pens to defaults` | Puts the ten colours and the notes they stand for back to those the application came with. The rest of your defaults are left alone. |

The title, version and file name of a score, its `Rolls` setting, `Tunes` and `Page Arranged By Hand` are in `Score Properties…` only. There is no default tempo or number of parts: the New Score window asks for those each time.

![Settings, New Score Defaults, Score pane: credits, text, numbering, and the header and footer designs](images/v4/settings-new-score-defaults.png){: width="700" }

## Music fonts

Notation is drawn either with the application's built-in shapes or from a SMuFL music font. Music fonts are part of the Studio Edition. The Community Edition draws every score with the built-in shapes.

**Installing fonts** is done in `Libraries` ▸ `Music Fonts`. Bravura comes with the application.

| Button | What it does |
|---|---|
| `Add Font…` | Asks for the font's `.otf` file, then for its metadata `.json` file. Both are needed. Copies of the two files are kept in the `fonts` folder inside your `.DrumScoreEditor` folder, and the font is listed under the name of its `.otf` file. |
| `Remove Font` | Removes the selected font and deletes its copies, after asking. Bravura cannot be removed. |

**Choosing a font** is done with `Use Music Font`, in the `Music Font` pane. In `New Score Defaults` it is for new scores, and in `Score Properties…` for the score in front of you. `Built-in` is the application's own shapes. Choose a font by name and the other settings on the pane apply.

<!-- screenshot: Settings showing Libraries ▸ Music Fonts: the list with Bravura and one added font selected, and the Add Font… and Remove Font buttons at the right -->

## Where settings are kept

Your settings are kept by your system, for your user account. Version 4 uses the same settings as 3.6.

The `.DrumScoreEditor` folder in your home folder holds your files:

- your library, until you choose another folder in `Libraries` ▸ `Location`;
- your takes, in `takes`, until you choose another folder;
- the music fonts you have added, in `fonts`.

`Help` ▸ `Show Log Folder` shows where the application keeps the log it writes each time it starts. Send that file when you report a problem.
