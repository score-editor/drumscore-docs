---
title: Printing and Export
topic: export
summary: Printing a score, and saving it as a PDF, a picture or a MusicXML file for somebody who does not have Drum Score Editor.
---

A score leaves Drum Score Editor on paper, as a PDF, as a picture of one page, or as a MusicXML file for another notation program. Printing is in both editions. The `Export` menu is part of the Studio Edition.

An export is a copy. It does not save the score, and it does not change the score's own file.

## Print a score

1. Choose `File` ▸ `Print…`, or press `Cmd+P` on a Mac or `Ctrl+P` on Windows and Linux. The `Print` button on the toolbar does the same.
2. Your system's own print window opens, set to print every page. Choose the printer, and the pages if you do not want them all.
3. Choose to print.

The job is named after the score, so you can pick it out in the printer's queue.

If the computer has no printer, Drum Score Editor says so and prints nothing.

## Make a PDF to send to the band

1. Choose the `Export PDF` button on the toolbar. `File` ▸ `Export as PDF…` does the same in the Community Edition, and `File` ▸ `Export` ▸ `Export as PDF…` in the Studio Edition.
2. Choose where to put the file. The name offered is the tune's title, such as "The Young MacGregor.pdf".
3. Choose to save.

The PDF holds every page of the score. You can carry on working while it is written. Nothing is shown when it finishes. A message appears only if the file could not be written.

## What is printed and exported

Print, PDF and the three picture formats draw the page the way the screen does, so the page that comes out is the page you see. A few things on screen are there to help you write. They are never printed or exported:

- the marks of `View` ▸ `Bar Audit`;
- the marks of `View` ▸ `Bar Locks`;
- the selection and the caret;
- the `Paper background`. `Parchment` and `Twill` are for the screen. Paper, PDFs and pictures are always white.

Two choices on the `View` menu do carry through:

- **`View` ▸ `Markup`.** Dynamics, highlight marks or unison marks that you have hidden are left out. See [Rudiments, Rolls and Tuplets](topic:rudiments).
- **`View` ▸ `Instruments`.** With some instruments hidden, you get the part on screen, flowed on to its own pages. This is how you print a snare part from a full score. See [Instruments and Staves](topic:instruments).

MusicXML is different. It always writes the whole score, every instrument and every mark, whatever is hidden.

## Paper

The paper size, orientation and margins are the score's own. They are set in the `Page` pane of `File` ▸ `Score Properties…`. See [Layout and Spacing](topic:layout).

`File` ▸ `Page Setup…` is another way to set the paper. It opens your system's page window. The paper size and orientation you choose there become the score's, and the score is laid out again to suit.

The page is printed at its own size, from the corner of the sheet, with the margins the score gives it. Drum Score Editor does not shrink or stretch the page to fit other paper, and does not add the printer's margins to the score's. So put paper of the score's size in the printer, or change the score's paper first.

Where a score has both portrait and landscape pages, each page of a PDF has its own orientation.

## The Export menu

`File` ▸ `Export` is in the Studio Edition. Each item asks where to put the file and offers a name made from the tune's title.

| Item | What it writes | Good for |
|---|---|---|
| `Export as PDF…` | One file holding every page. | Sending to the band, and printing somewhere else. |
| `Export as JPG…` | One picture of the page on screen. | Messages, and anywhere that takes a photo. |
| `Export as SVG…` | One drawing of the page on screen, which stays sharp at any size. | Web pages, and work that will be scaled or printed large. |
| `Export as PNG…` | One picture of the page on screen. | Documents, slides and web pages. |
| `Export as MusicXML…` | The music itself, for another notation program. | Moving a score to other software. |
| `Export for Drum Score Editor 3…` | A copy that Drum Score Editor 3 can open. It lists what the older format drops before it writes anything. | See [Files and Older Scores](topic:files). |
| `Export as Portable .ds…` | A copy of the score with all its pictures inside it. | Sending a score to somebody when you keep pictures in your library. |

### Pictures: JPG, SVG and PNG

A picture holds one page: the one you are looking at. Scroll to the page you want before you choose the item. When the score has more than one page, the name offered says which, such as "The Young MacGregor Page 2.png". To get every page, export each in turn.

None of the three asks any questions. There is no choice of resolution or quality.

- **JPG and PNG** are made at four pixels to the point. An A4 page comes out 2384 pixels wide and 3368 high, which is about 288 dots to the inch.
- **PNG** has a solid white page. It is not transparent.
- **SVG** is the size of the paper, and can be scaled to any size without going soft.

### Portable .ds

This item is on the menu only when `Keep score images in the library, not inside the score file` is ticked in [Settings](topic:settings). A score saved that way refers to its pictures in your library folder, so somebody without your library would not see them. The portable copy puts the pictures back in. The name offered ends in "-portable".

If a picture is no longer in your library, the copy is still written, and you are told how many are missing.

## MusicXML

MusicXML is for other notation programs. It carries the music and not the look of the page.

1. Choose `File` ▸ `Export` ▸ `Export as MusicXML…`.
2. Choose where to put the file. A score with more than one tune asks for a folder instead.
3. The `MusicXML Options` window opens. Check the pitches and the `Export partwise` tick, then choose `OK`.
4. The window shows `MusicXML file saved`. Choose `Done`.

![The MusicXML Options window: a pitch and octave for each hand, for notes and for grace notes](images/v4/musicxml-options.png){: width="289" }

**Why it asks for pitches.** MusicXML writes a note by where it sits on a stave, and a drum score writes it by hand. So you choose a `Pitch` and `Octave` to stand for the `Left hand` and the `Right hand`, for a `Note` and for a `Grace note`. The window opens with D for the left hand and F for the right, in octave 4.

**`Export partwise`.** MusicXML has two ways of arranging the same music. Partwise writes each instrument from start to finish, one after another. Timewise writes bar by bar, with every instrument's music inside each bar. The music is the same either way. Leave `Export partwise` ticked unless the program you are sending the file to asks for timewise: nearly every notation program reads partwise, and some read nothing else. DrumScore Editor's own MusicXML import reads partwise only.

**What is written:**

- notes and rests with their values, dots and tuplets, including a tuplet inside a tuplet;
- grace notes, as small notes before the note they belong to;
- rolls, as tremolo strokes;
- accents and the other articulations, dynamics and hairpins;
- a part for each instrument, in the order of their lines, named as the score names them. See [Instruments and Staves](topic:instruments);
- a tenor on a five-line stave at the pitches written, chords included.

**A score with more than one tune** is written as a folder: one file for each tune, numbered in order, such as "01 The Young MacGregor.musicxml", and one more file that lists them. The window then shows how many files were written.

## How the output looks

**The music font.** A score drawn with a music font prints and exports in that font. A score drawn with the built-in shapes prints and exports in those. The choice is `Use music font`, in the `Music Font` pane, which is part of the Studio Edition.

**The ink.** Notation is normally drawn in a very dark grey. If your printer handles greys badly, tick `Use pure black ink` in [Settings](topic:settings), under `Appearance`: print, PDF and the picture exports are then drawn in pure black, as the screen is.

**Text in PDF and SVG files** is drawn as shapes. The file looks the same on a computer that has none of your fonts. The words in it cannot be selected or searched.

**The Community Edition** draws every score with the built-in shapes, does not show pictures, and puts a faint "Drumscore.scot Community Edition" watermark on each page. What it prints is the same as its screen in this too.

## What needs the Studio Edition

| | Community Edition | Studio Edition |
|---|---|---|
| `File` ▸ `Print…` and the `Print` button | Yes | Yes |
| `File` ▸ `Page Setup…` | Yes | Yes |
| The `Export PDF` button on the toolbar | Yes | Yes |
| `File` ▸ `Export as PDF…` | Yes | In the `Export` menu |
| The `File` ▸ `Export` menu | No | Yes |
| `File` ▸ `Studio…` | No | Yes |

See [Licensing](topic:licensing).

## Video, and bringing music in

`File` ▸ `Studio…` opens the Studio, where you assemble your takes, set their levels and write a video. It is not covered on this page.

In the Studio Edition, `File` ▸ `Import` ▸ `Import MusicXML…` reads a MusicXML file into a new score. See [Files and Older Scores](topic:files).
