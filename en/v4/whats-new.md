---
title: What’s New in Version 4
topic: whats-new
summary: What has changed for someone coming from version 3.6.
---

Version 4 opens the scores you wrote in 3.6, and it keeps the licence and settings you already have. The window looks different, a good many commands have moved, and a score saved by version 4 can no longer be opened by 3.6. This page says what is new, where things have gone, and what to know before you save.

![The version 4 window with a score open: toolbars along the top, rudiments at the left, the note toolbox at the right](images/v4/main-window.png){: width="900" }

## New in version 4

Several of the items below need the Studio Edition, as the productivity features did in 3.6. See [Licensing](topic:licensing).

### Scores and tunes

- **Several tunes in one score.** `Score Properties…` now has two sections, `Score` and `Tunes`. In `Tunes` you add, remove and reorder the tunes in a score. Each tune has its own title, tune type, time signature, tempo and number of parts, and carries its own header where it begins. See [Score Properties](topic:score-properties).
- **A new score in two steps.** `New…` first asks `What kind of tune?`, with its time signature and tempo. The second step takes the title, author and band, and the layout. Repeats, bars per line, clef and the header and footer design are under `Advanced options`. See [Starting a Score](topic:new-score).
- **Headers and footers edited on the page.** Double-click a tune header or a page footer to arrange it. Right-click inside it for `Add Text` and `Add Image`. `Save Header as Design` and `Save Footer as Design` keep a layout for new scores. See [Text and Headers](topic:text-and-headers).
- **Numbered parts.** In `Score Properties…`, under `Numbering`, tick `Parts`. Each part of a tune then carries its number, in a box, at the left of its first line. The count starts again at one for each tune. It needs the Studio Edition.
- **Page margins and binding.** The `Page` pane sets margins as `Small`, `Medium`, `Large` or `Custom`, and can leave room for a binding on the left or top edge. See [Layout and Spacing](topic:layout).

![Score Properties, Tunes section, with three tunes in the score](images/v4/score-properties-tunes.png){: width="752" }

### Instruments

These are for scores made in the `Standard` general layout. A score keeps the general layout it was created with.

- **Several instruments on one system.** In the `Notation` pane, `Add Instrument` adds a `Snare`, `Tenor` or `Bass` to the score. A new score has a line for each on every system. In a score you already have, right-click a line and use `Staff Line` ▸ `Instruments` to put the new instrument on that line or on the whole tune. A bracket joins the lines of a system. `Show Names` writes each instrument's name at the left, and `Join Barlines` runs the barlines through the gap between the lines. `View` ▸ `Instruments` hides or shows each instrument's lines.
- **The tenor on five lines.** A tenor's `Stave` can be `One Line` or `Five Lines`. On five lines it is written in the bass clef, each note at its pitch. Choose before you write: once the instrument has notes, its stave cannot be changed.

See [Instruments and Staves](topic:instruments).

![A system of snare, tenor on five lines and bass, joined by a bracket and named at the left](images/v4/instruments-system.png){: width="819" }

### Spacing

- **Line heights.** `Line Heights` in the `Engraving` pane decides how tall each staff line is drawn. `Legacy` is how your score has always been drawn. `Uniform` makes every line of a tune as tall as its tallest line needs. `Fit Each Line` makes each line as tall as its own marks need. Once a score leaves `Legacy` it cannot go back.
- **Lock a bar against Beautify.** Right-click in a bar and choose `Measure` ▸ `Lock Against Beautify`. Beautify and other automatic spacing then leave that bar as you placed it. You can still edit it. `View` ▸ `Bar Locks` shows a padlock over each locked bar.
- **Barlines that move.** With `Allow barlines to move` ticked in the `Engraving` pane, Beautify places the barlines as well as the notes. It replaces barlines you have placed by hand. It is offered only in the `Standard` layout with the `TraditionalSpacing` spacing policy.
- **A tuplet inside a tuplet is drawn clear of the one around it.** 3.6 could write one, but drew both brackets on the same side of the notes. Version 4 draws the inner tuplet on the opposite side, so the two do not run into each other.
- **Tuplet number size.** `Tuplet Number Size` in the `Engraving` pane draws the number over an irregular group `Large`, `Medium` or `Small`.
- **Hide marks without removing them.** `View` ▸ `Markup` shows or hides `Dynamics`, `Highlight Marks` and `Unison Marks`. The marks stay in the score.

See [Layout and Spacing](topic:layout) and [Rudiments, Rolls and Tuplets](topic:rudiments).

![The same four lines drawn with Legacy, Uniform and Fit Each Line](images/v4/line-heights-compared.png){: width="897" }
![A line of music with a padlock over its third bar](images/v4/bar-locks.png){: width="823" }

### Highlight pens

- **Ten pens instead of six.** The editing toolbar now has ten highlight pens. A score written in 3.6 keeps its own six colours.
- **A pen can stand for a note.** Tenor corps mark each drum with a colour. In the `Highlighters` pane, under `Pens and pitches`, you say which note each pen stands for. A note highlighted with that pen on a tenor line is then played back at that note.

### Playing and recording

`Launch Media Studio…` has gone from the `View` menu. In its place:

- **Quick Play** is a toolbar in the main window, shown with `View` ▸ `Show` ▸ `Quick Play`. It runs a cursor through the music at the tunes' tempos. Right-click in a bar and use `Measure` ▸ `Section` to play or loop that bar, or to mark the bars you want to play.
- **Takes.** The record button on the same toolbar records you playing along with the cursor. The microphone is chosen under `Settings` ▸ `Recording`.
- **Studio.** `File` ▸ `Studio...` is where you assemble your takes, set their levels and write a video.

![Quick Play running: the bar being played is shaded and a cursor moves through it](images/v4/quick-play.png){: width="900" }

### Smaller things

- `Edit` ▸ `Undo` and `Redo` name what they will undo or redo.
- `View` ▸ `Fit Width` sits beside `Actual Size`.
- `File` ▸ `Export` has `Export for Drum Score Editor 3…`. See *Your existing scores* below.

## Where things have gone

The menu bar is now `File`, `Edit`, `View` and `Help`, with `Window` on a Mac. The `Insert` and `Format` menus have gone. Their commands are on the menu you get by right-clicking the thing you want to change.

| In 3.6 | In version 4 |
|---|---|
| `Insert` ▸ `Music Area`, `Text Area`, `Image Area` | Music runs on to new pages by itself. On a page arranged by hand, right-click on empty page: `Insert Music Area`, `Add Text`, `Add Image` |
| `Insert` and `Format` ▸ `Music`: parts, staff lines, 2nd time, point size | Right-click in the music. The commands are grouped as `Score`, `Measure`, `Part` and `Staff Line` |
| `Format` ▸ `Music` ▸ `Beautify` | Right-click in the music, `Score` ▸ `Beautify`. Alt+B still works |
| `Format` ▸ `Text` | Right-click the text |
| `Edit` ▸ `Page` | Double-click a tune header or a page footer |
| `Edit` ▸ `Bar Lines` and `Notes` | `Edit` ▸ `Select Bar Lines` and `Select Notes` |
| `Edit` ▸ `Settings` (Windows and Linux) | `File` ▸ `Settings`. On a Mac it is still in the application menu |
| `View` ▸ `Toolbar`, `Edits Bar`, `Notes Actions`, `Rudiments`, `Status Bar` | `View` ▸ `Show` ▸ `Standard toolbar`, `Editing toolbar`, `Note toolbox`, `Rudiments`, `Status Bar` |
| `View` ▸ `Bar Content Warnings` | `View` ▸ `Bar Audit` |
| `View` ▸ `Launch Media Studio…` | `View` ▸ `Show` ▸ `Quick Play`, and `File` ▸ `Studio...` |
| `View` ▸ `New Rudiment Library…`, `Add Existing Rudiment Library`, `Close Current Rudiment Library` | `Settings` ▸ `Libraries` ▸ `Rudiments`: `New…`, `Add…` and `Remove` |
| Settings tab `General` | Split between `Appearance` and `Files` |
| Settings tabs `Options`, `Layout`, `Format` | `Score`, `Notation`, `Page` and `Engraving`, under `New Score Defaults` |

`Settings` is now grouped as `Licence`, `Appearance`, `Files`, `Libraries`, `Recording`, `Privacy` and `New Score Defaults`. `Score Properties…` shows the same panes as `New Score Defaults`, for the score in front of you. See [Settings](topic:settings), [Score Properties](topic:score-properties) and [Keyboard Shortcuts](topic:shortcuts).

<!-- screenshot: the right-click menu in a music area, with the Score, Measure, Part and Staff Line submenus -->
![The Settings window, with its sections along the top](images/v4/settings-sections.png){: width="900" }

## What is different or not here

- **`Block Select`** has been dropped.
- **`Left Align Selection`** and **`Left Align Selection Stems`** have been dropped.
- **Rudiment libraries** are still here, and they are still `.dsl` files. The panel is shown with `View` ▸ `Show` ▸ `Rudiments`. Which libraries are open is now chosen in `Settings`. See [Rudiments, Rolls and Tuplets](topic:rudiments).
- **Bar note checking** is now called `Bar Audit`. It marks a bar that holds more or less than its time signature allows.

## Your existing scores

**Version 4 opens 3.6 scores.** Open them as you always have.

**Some older multi-page scores open read-only the first time.** When a score ran on to a second page in version 3, the items of its header were copied on to the later pages. Version 4 does not do that, because it makes a header for every tune where the tune begins, so it removes those copies. It tells you what it removed and leaves your original file unchanged. To work on the score, use `Save Score As…` and give it a new name.

**Saving is one way.** Version 4 saves in its own format. Once version 4 has saved a score, 3.6 will not open that file. If you may need a score in 3.6 again, keep a copy of the original before you save over it.

**There is a way back for one score.** `File` ▸ `Export` ▸ `Export for Drum Score Editor 3…` saves a separate copy that 3.6 can open. It lists what the older format cannot hold before it writes anything. The `Export` menu is part of the Studio Edition.

**Version 4 replaces 3.6.** Installing version 4 takes the place of 3.6 on your computer, on Mac, Windows and Linux. It uses the same settings and the same licence, and the same `.DrumScoreEditor` folder in your home folder.

**If you need to go back.** The way back is to reinstall 3.6. Please get in touch before you do, at [alan@drumscore.scot](mailto:alan@drumscore.scot).

See [Files and Older Scores](topic:files) and [Printing and Export](topic:export).
