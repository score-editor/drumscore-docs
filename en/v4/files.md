---
title: Files and Older Scores
topic: files
summary: Opening, saving and sharing scores, and what happens to scores written in 3.6 and earlier.
---

A score is one `.ds` file. This page covers opening and saving, what version 4 does with the scores you already have, and how to send a score to somebody else.

## The short answers

**Will version 4 open my old scores?** Yes. It opens scores written by 3.6 and by the versions before it. Open them as you always have.

**Does opening one change my file?** No. Nothing is written until the score is saved. Read *Automatic File Saving* below, though, because in the Studio Edition a save follows your first change by a few seconds.

**Can 3.6 open a score once version 4 has saved it?** No. Version 4 saves in its own format, and 3.6 will not open that file. If you may need a score in 3.6 again, make a copy of the file before you change it in version 4.

**Can I go back to 3.6?** Version 4 replaces 3.6 on your computer. The way back is to reinstall 3.6. Please get in touch before you do, at [alan@drumscore.scot](mailto:alan@drumscore.scot).

**Is there a backup or a history of my saves?** No. A save replaces the file. Keep your own copies of scores that matter.

## The score file

A `.ds` file holds the whole score: the music, the score's own settings, and its headers and footers. One file can hold several tunes. See [Score Properties](topic:score-properties).

Pictures are saved inside the file too, unless you have ticked `Keep score images in the library, not inside the score file`. See [Text and Headers](topic:text-and-headers) and *Sending a score to somebody* below.

Scores live wherever you save them. There is no special folder for them.

## Open a score

Choose `File` ▸ `Open…`, or press `Cmd+O` on a Mac or `Ctrl+O` on Windows and Linux. The `Open` button on the toolbar does the same. You can also double-click a `.ds` file. On a Mac and on Windows it opens in the window you already have. On Linux it starts another copy of the application.

Each score opens in its own tab. `Ctrl+Tab` moves to the next tab and `Ctrl+Shift+Tab` to the one before.

**`File` ▸ `Open Recent`** lists the last ten scores you opened or saved, newest first, each with its whole path. The first nine have keys: `Cmd+1` to `Cmd+9` on a Mac, `Alt+1` to `Alt+9` on Windows. A file that has since been moved or deleted stays on the list.

**The same score twice.** Drum Score Editor does not check whether a score is already open. Open it again and you have two tabs on one file, and whichever you save last is what the file holds.

<!-- screenshot: the tab strip with three scores open: one plain ("City Pipe Band Medley"), one with a star before its name ("*The Young MacGregor"), one with a padlock before its name -->

### What the tab tells you

The tab shows the score's name, which is its tune's title and not the file's name.

| Mark | Meaning |
|---|---|
| `*` before the name | The score has changes that are not saved. |
| A padlock before the name | The score is read-only. See *Read-only scores* below. |

The status bar says the same in words: `Saved`, `Unsaved changes`, or `No score` when nothing is open. The title bar shows which file the score in front came from, or `Untitled` for a score with no file yet.

### When a score will not open

A box titled `Could not open`, followed by the file's name, says why:

- **"No such score"** and the path. The file is not where it was. This is what you see when you choose a moved or deleted file from `Open Recent`.
- **"Not a readable score file"**. The file is damaged, or is not a Drum Score Editor score.
- **"This score needs a newer version of Drum Score Editor"**. Update the application.

In the Community Edition, a score that uses Studio Edition instruments is not opened either. See [Instruments and Staves](topic:instruments).

## Save a score

| Command | What it does |
|---|---|
| `File` ▸ `Save` | Writes the score to its file. `Cmd+S` on a Mac, `Ctrl+S` on Windows and Linux, or the `Save` button on the toolbar. For a score with no file yet it asks where to put it. |
| `File` ▸ `Save Score As…` | Asks for a new name and place. The score in the tab is that new file from then on. The `Save As` button on the toolbar does the same. |
| `File` ▸ `Save All` | Saves every open score that has a file. It skips new scores that have never been saved, and read-only scores, without asking. |

A new score is offered its tune's title as a name, such as "The Young MacGregor.ds". If you leave `.ds` off the name, it is added.

If a save fails, a `Save Error` box says the score could not be written, and why when it can. The `Save Score As…` window then opens so you can put the score somewhere else. This is what happens when the file is one your system will not let you change.

### Closing with unsaved changes

Close a score with `File` ▸ `Close` (`Cmd+W` on a Mac, `Ctrl+W` on Windows and Linux), the close button on its tab, or a middle-click on the tab. `File` ▸ `Close All` closes every score.

A score with unsaved changes asks first: "Do you want to save the changes to The Young MacGregor?" Choose `Save`, `Don't Save` or `Cancel`. If you choose `Save` and then cancel the file window, the score stays open.

Quitting asks the same about one unsaved score. With several, it says how many and offers `Review Changes…`, which asks about each in turn, `Discard Changes`, which quits and saves none, and `Cancel`.

<!-- screenshot: the unsaved-changes question for "The Young MacGregor" with its three buttons Save, Don't Save and Cancel -->

### Automatic File Saving

In the Studio Edition, `Automatic File Saving` saves your changes into the score's own file in the background. It is on unless you have turned it off. It writes about three seconds after you stop working, and at least once a minute while you keep going. The setting is in `Settings` ▸ `Files`. See [Settings](topic:settings).

- It writes over the score's file, as `Save` does. There is no separate copy.
- A score that has never been saved has no file, so it is not saved this way. Save it once yourself.
- **It applies to a 3.6 score as well.** Open one, change a note, and a few seconds later the file is in version 4's format. Copy the file first if you want to keep it for 3.6, or untick the setting.
- If it cannot write, an `Auto-Save Error` box tells you to save your work yourself.

The Community Edition saves only when you choose `Save`.

## Read-only scores

A read-only score has a padlock on its tab. It cannot be edited, and `Save` will not write over its file. To work on it, choose `File` ▸ `Save Score As…` and give it a new name. The padlock goes and the new file is an ordinary score. The file you opened is left as it was.

A score opens read-only for one of two reasons:

- **It is an older multi-page score that has been brought up to date.** See the next section.
- **It was saved by a newer release of version 4 than the one you have.** The status bar says `Written by a newer version`. Saving over it would drop whatever the newer release added, so update the application instead if you can.

## Scores from 3.6 and earlier

Version 4 reads an older score and brings it up to date as it opens. The file itself is not touched until the score is saved. It is then written in version 4's format, and 3.6 will not open it again.

**One change you are told about.** Earlier versions copied the title, author and footer from the first page on to every page after it. A score can now hold several tunes, each with its own header where it begins, so a copy of page one's title no longer belongs on a later page. Version 4 removes those copies and brings the music up into the space.

When that happens, a window titled `This score has changed shape` lists what was removed, and the score opens read-only. Your original file still holds everything. Save the score under a new name to carry on.

<!-- screenshot: the "This score has changed shape" window for an older two-page score, showing the list of removed captions and the tick box "Do not show this again - update older scores silently from now on" -->

The window has a tick box, `Do not show this again - update older scores silently from now on`. Tick it and older scores are still brought up to date, but without the window, and they open ready to edit and to save over their own files. The same choice is `Tell me when an older score is brought up to date`, in `Settings` ▸ `Files`, where you can turn the warning back on. See [Settings](topic:settings).

A score with no such copies opens ready to edit, with nothing to tell you.

If you built a multi-page score to stand in for several tunes, or you are unsure what to do with one, send the original file to [support@drumscore.scot](mailto:support@drumscore.scot) and it can be converted for you.

### In the Studio Edition: a copy for 3.6

`File` ▸ `Export` ▸ `Export for Drum Score Editor 3…` writes a separate copy that 3.6 can open, and lists what the older format cannot hold before it writes anything. See [Printing and Export](topic:export).

## Bring music in from MusicXML

`File` ▸ `Import` ▸ `Import MusicXML…` is part of the Studio Edition. It reads a `.musicxml` or `.xml` file into a new score.

- The score opens in a new tab with no file of its own. Save it as a `.ds` when you are ready. The MusicXML file is not changed, and is not added to `Open Recent`.
- The title, composer, tune type, time signature and tempo come from the file. The paper, fonts and band name come from your `New Score Defaults`, as they do for a new score.
- The score is made in the `Standard` general layout.

If the file cannot be read, a `Could not import` box says "This file could not be read as MusicXML." Nothing is opened.

For writing MusicXML, see [Printing and Export](topic:export).

## Sending a score to somebody

Send the `.ds` file. Three things to check first:

- **Their version.** A score saved by version 4 needs version 4 to open it.
- **Pictures.** If you keep pictures in your library and not in the score, the file alone arrives without them. Send a copy made with `File` ▸ `Export` ▸ `Export as Portable .ds…` instead. See [Printing and Export](topic:export).
- **Their edition.** The Community Edition does not open a score with more than one instrument on a system, or a tenor on a five-line stave. See [Instruments and Staves](topic:instruments).

For somebody who does not have Drum Score Editor, send a PDF. See [Printing and Export](topic:export).

## Where things are kept

Your scores are where you saved them. Everything else is kept for you:

- **Settings** are kept by your system, for your user account. Version 4 uses the same settings and the same licence as 3.6.
- **The `.DrumScoreEditor` folder** in your home folder holds your library, your takes and the music fonts you have added, until you choose other places for them. See [Settings](topic:settings).
- **The log.** `Help` ▸ `Show Log Folder` opens the folder that holds the log the application writes each time it starts, and shows its path. Send that file when you report a problem.

See also [What’s New in Version 4](topic:whats-new) and [Licensing](topic:licensing).
