---
title: Score Properties
topic: score-properties
summary: Every setting that belongs to one score and is saved in its file, pane by pane, and the tunes the score holds.
draft: true
---

`Score Properties` holds everything that belongs to the score in front of you: its name, how it is drawn, the paper it is on and the tunes in it. This page lists every setting in the window. Where another page explains a setting fully, the line here is short and links to it.

## Open the window

Choose `File` ▸ `Score Properties…`, or the `Properties` button on the toolbar. There is no key for it.

The window has two sections, chosen at the top:

- `Score` has a list of panes down its left side: `Score`, `Notation`, `Engraving`, `Page`, `Music Font`, `Unison`, `Watermark` and `Highlighters`.
- `Tunes` lists the tunes in the score, with a form for the one selected.

Nothing changes in the score until you choose `OK`. `Cancel` leaves the score exactly as it was, including any tunes you added or removed in the window. The one exception is the list that shows measurements in `mm` or `inches`: it is the application's own setting and changes at once.

Everything `OK` applies is one step to undo. If you also added, removed or reordered tunes, that is a second step of its own.

## A score carries its own settings

Every setting here is written into the score's file. When a score is made, it takes a copy of `Settings` ▸ `New Score Defaults`. After that the two are separate: changing `New Score Defaults` does not change a score you have already made, and changing a score does not change your defaults.

The panes are the same panes as `New Score Defaults`, for this score instead of the next one. The `Score` pane here, `Page Arranged By Hand` and the `Tunes` section are this window's own. See [Settings](topic:settings).

## Score pane

| Setting | What it does |
|---|---|
| `Score title` | The name of the whole score. It matters when the score holds more than one tune. Each tune's own title is under `Tunes`. |
| `Band` | The band the score is for. The footer shows it. |
| `Version` | A version label of your own. It is printed where a header or footer uses `%version`. |
| `Pages`, `Lines`, `Parts` | Page, line and part numbers. Studio Edition. See [Text and Headers](topic:text-and-headers). |
| `Font`, `Choose…`, `Font Size` | The font for numbers, instrument names and stroke counts. `Choose…` also sets its style. See [Text and Headers](topic:text-and-headers). |
| `Rolls` | What is written at each roll: `None`, `Stroke Count`, or `Roll Breakdown`, which marks the buzzes and taps under the notes. |
| `Filename` | The file's name, as printed where a header or footer uses `%filename`. |

![Score Properties, Score pane: the Identity, Numbering, Text and File groups](images/v4/score-properties-score.png){: width="700" }

## Notation pane

In the Community Edition every row of this pane is shown but cannot be changed.

| Setting | What it does |
|---|---|
| `General Layout` | `DrumScoreEditor` or `Standard`. Shown only: it is fixed when the score is made. See [Starting a Score](topic:new-score). |
| `Bars per line` | How many bars a line gets when a part is added later. It does not re-rule lines already there. |
| `Inline Time Signature` | Shown only: fixed when the score is made. |
| `Use Repeats in Parts` | Has no effect on this score. Use `New parts with repeat dots` under `Tunes`. |
| The instrument rows | One row for each instrument: type, name, stave, `Hands`, clef, and buttons to move or remove it. See [Instruments and Staves](topic:instruments). |
| `Add Instrument` | Adds a row. `Standard` layout only. |
| `Show Names` | Writes instrument names at the left of the lines: `Off`, `First System of a Tune` or `Every System`. |
| `Clef on every line` | Draws the clef on every line, not only the first. `Standard` layout only, and only where an instrument has a clef. Always ticked when there is more than one instrument. |

![Score Properties, Notation pane: three instruments listed, with Add Instrument and Show Names below](images/v4/score-properties-instruments.png){: width="814" }

## Engraving pane

**Spacing.** See [Layout and Spacing](topic:layout).

| Setting | What it does |
|---|---|
| `Spacing Policy` | How a bar shares its width among its notes. Changing it does not re-space what is written. The next Beautify does. |
| `Allow barlines to move` | Beautify places the barlines as well as the notes. `Standard` layout with `TraditionalSpacing` only, otherwise greyed and unticked. Studio Edition. |
| `Beautify tuplets as they are made` | Making a tuplet re-spaces its bar. Greyed and unticked as the row above is. Studio Edition. |
| `Proportional Spacing` | Where the caret goes after each note you type. See [Entering Notes](topic:entering-notes). |
| `Roughs before the barline` | Draws a ruff on the first note of a bar before the barline, where there is room. Studio Edition. See [Rudiments, Rolls and Tuplets](topic:rudiments). |

**Accents and roll ties.** See [Rudiments, Rolls and Tuplets](topic:rudiments).

| Setting | What it does |
|---|---|
| `Align All Accents` | Lifts left-hand accents so that every accent in a bar sits on one row. |
| `Roll Ties Below Accents` | Pulls a roll's tie down over the note-heads, under any accent. |

**Irregular groups.** See [Rudiments, Rolls and Tuplets](topic:rudiments).

| Setting | What it does |
|---|---|
| `Expand Irregular Time Signatures` | Writes an irregular time signature as its groups, such as 2+3 over 8, instead of 5 over 8. |
| `Irregular Groups Below Notes` | Puts a tuplet's number under the beams in a squared-off bracket. |
| `Draw Ties For Irregular Groups` | Draws the slur or bracket over a tuplet. Unticked, only the number is drawn. |
| `Tuplet Number Size` | `Large`, `Medium` or `Small`. |

**Beams.** See [Entering Notes](topic:entering-notes).

| Setting | What it does |
|---|---|
| `Auto-join note tails as beams` | Beams the notes of a beat for you. Studio Edition. |
| `Beams at Subdivision of Beat` | How many beams carry on across a subdivision of the beat. `Single` keeps one, `Progressive` one fewer, `Continue` all of them. Studio Edition. |

**Staff lines down the page.** See [Layout and Spacing](topic:layout).

| Setting | What it does |
|---|---|
| `Distribute Staff Lines Evenly` | Spreads the lines over the height of the page. Only for a score of one page and one tune, and the score then stays that way. |
| `Line Heights` | `Legacy`, `Uniform` or `Fit Each Line`. Once a score leaves `Legacy`, `Legacy` is no longer offered. Studio Edition. |
| `Staff Line Gap Factor` | In `Legacy` only. Adds or takes away space between lines, as a percentage of a line's height. Greyed while lines are distributed evenly. |
| `Space Between Lines` | Outside `Legacy`. The clear space between one line's marks and the next. Greyed while lines are distributed evenly. |
| `Space Between Instruments` | Outside `Legacy`. The same, within one system. Empty the box and it follows `Space Between Lines`. Greyed while lines are distributed evenly. Studio Edition. |

![Score Properties, Engraving pane: the Spacing group and the start of those below it](images/v4/score-properties-engraving.png){: width="619" }

## Page pane

See [Layout and Spacing](topic:layout) for all of these.

| Setting | What it does |
|---|---|
| `Paper size` | `A4`, `A3`, `Letter` or `Legal`. A score on some other size shows `Custom` and keeps it. |
| `Default orientation` | `Portrait` or `Landscape`. A tune can be turned the other way under `Tunes`. |
| `Size` | The margins: `Small`, `Medium`, `Large` or `Custom`. |
| `Values` | `Left`, `Top`, `Right` and `Bottom`, to type in when `Size` is `Custom`, with the list for `mm` or `inches`. |
| `Binding` | `Off`, `Left edge` or `Top edge`, and a `Width`: extra room kept clear on that edge. |
| `Mirror margins on facing pages` | The binding room changes sides on alternate pages. |
| `Page Arranged By Hand` | The page is never re-flowed. It can be ticked only while the score has one page and one tune. |

![Score Properties, Page pane, with custom margins and binding on the left edge](images/v4/score-properties-page.png){: width="800" }

## Music Font pane

This pane is part of the Studio Edition. The Community Edition does not show it. Every setting below `Use Music Font` is greyed while that is `Built-in`.

| Setting | What it does |
|---|---|
| `Use Music Font` | `Built-in` draws the music with the application's own shapes. Choose a font and the music is drawn from it. |
| `Music Font Size` | The size of the music, as a figure of your own. |
| `Use Font Default Stem Length` | Takes the length of a stem from the font. |
| `Stem Length (staff lines)` | Your own stem length. Untick the row above to type it. |
| `Bar height (staff lines)` | `5` or `3`: full-height barlines or short ones. |
| `Thinner Secondary Beams` | Draws the secondary beams thinner, leaving one at full thickness. |
| `Dynamics Relative Size` | Dynamics at `100%`, `75%`, `50%` or `25%` of the music's size. |
| `Use Z Through Stem For Rolls` | Draws a buzz roll as a Z through the stem instead of slashes. |
| `Bracket Part Barlines` | Puts bracket ends on the barlines that open and close each part. |

<!-- screenshot: Score Properties, Music Font pane, with Use Music Font set to a music font (not Built-in) so every row is live: Music font, Stems and Notation groups all visible. Width about 800. -->

## Unison pane

See [Rudiments, Rolls and Tuplets](topic:rudiments) for marking unison.

| Setting | What it does |
|---|---|
| `Unison bracket weight` | `None`, `Regular`, `Medium` or `Heavy`. `None` draws no bracket. Studio Edition. |
| `Draw unison bracket dashed` | Draws the bracket as a dashed line. |
| `Put a u inside the unison bracket` | A small u just inside the start of each bracket. Greyed when there is no bracket. Studio Edition. |
| `Use colour to highlight unison` | Colours the unison notes. The three rows below are greyed without it. |
| `% Weight of unison highlight` | How strong the colour is. Studio Edition. |
| `Use thinner unison highlighter` | Draws the colour as a thinner band. Studio Edition. |
| `Colour to highlight unison`, `Change ..` | The colour. The label shows it at the weight you chose. |

![Score Properties, Unison pane: the Bracket and Colour groups](images/v4/score-properties-unison.png){: width="604" }

## Watermark pane

This pane is part of the Studio Edition. The Community Edition does not show it. See [Text and Headers](topic:text-and-headers).

| Setting | What it does |
|---|---|
| `Watermark` | `None`, `Text` or `Image`. `Image` is offered when the score has a picture or your library holds one. |
| `% Weight of watermark` | How strongly it prints. |
| `Watermark Text`, `Font Size` | The words and their size. `Text` only. |
| `Library` | Your watermark pictures. Click one to use it for this score. Pictures are added and removed in [Settings](topic:settings). |
| `Use this score's own image` | Goes back to the picture the score came with, after you have clicked one in the library. |
| `This score references the watermark image instead of embedding it (smaller file)` | The file stores the picture's name in your library, not the picture. Offered when the score uses a library picture. |

## Highlighters pane

| Setting | What it does |
|---|---|
| `Pens and pitches` | The ten pens. For each: its colour, and the note and octave it stands for on a tenor line. Studio Edition. See [Instruments and Staves](topic:instruments). |
| `Continuous highlights` | Joins a run of highlighted notes into one band. |
| `Reset pens to defaults` | Puts this score's colours and notes back to those a new score is given. |

![Score Properties, Highlighters pane: ten pens, each with a note and an octave](images/v4/score-properties-highlighters.png){: width="704" }

## Tunes

The list at the left holds the score's tunes in the order they are printed. Under it:

| Button | What it does |
|---|---|
| `+` | Adds a tune called `New Tune`, copying the tune type, author, time signature and tempo of the tune selected. Change them in the form before you choose `OK`. |
| `−` | Removes the selected tune and all its music. It does not ask first: `Cancel` keeps the tune, and after `OK`, undo brings it back. A score keeps at least one tune. |
| ▲ and ▼ | Move the tune earlier or later. Its header and music move with it. |

![Score Properties, Tunes section, with three tunes in the score](images/v4/score-properties-tunes.png){: width="752" }

| In the form | What it sets |
|---|---|
| `Title` | The tune's name, shown in its header. |
| `Tune Type` | One of the eight tune types, or type your own. Choosing one sets the time signature and tempo that type starts with. |
| `Author` | Who wrote the tune. |
| `Time Signature` | The two numbers, `Irregular Grouping`, and `Display using Common symbol` or `Display using Cut-Common symbol`. See [Starting a Score](topic:new-score). Changing it changes the time signature drawn. It does not re-bar notes already written. |
| `Beats per Minute` | The tempo. |
| `Number of parts` | How many parts to rule. Shown only for a tune you have just added, and it starts at 2. |
| `Anacrusis` | Shown only: it is set when the tune is made. For a pickup bar on a part, see [Layout and Spacing](topic:layout). |
| `Start on a new page` | The tune begins a fresh page. |
| `Orientation` | `Inherit score default`, `Portrait` or `Landscape`. A tune turned the other way from the page before it starts a new page. |
| `New parts with repeat dots` | Parts added to this tune are written once, with repeat dots. |

The whole `Tunes` section is greyed, with the reason shown at its top, in two cases:

- **The staff lines are distributed evenly.** Such a score holds one tune on one page. This is how a score made in the Community Edition is set.
- **The page is arranged by hand.** An arranged page is never re-flowed, so a second tune would have nowhere to go.

To change the tunes, untick `Distribute Staff Lines Evenly` in the `Engraving` pane, or `Page Arranged By Hand` in the `Page` pane, choose `OK`, and open the window again.

## What cannot be changed

These are shown so that you can see how the score was made. Rest the pointer on one for the reason.

- `General Layout` and `Inline Time Signature`, fixed when the score is made.
- A tune's `Anacrusis`, and the number of parts in a tune that already exists. Parts are added and removed on the score itself.
- The stave of an instrument that has notes: `One Line` or `Five Lines`.
- `Legacy` line heights, once the score has left them.

To change the general layout, make a new score. See [Starting a Score](topic:new-score).

## Community Edition

The Community Edition shows six panes: `Score`, `Notation`, `Engraving`, `Page`, `Unison` and `Highlighters`. `Music Font` and `Watermark` are not listed.

A setting marked Studio Edition above is still shown, so you can see how the score is set, but it needs a licence to change. A greyed one says `Studio edition only. This setting needs a licence.` when you rest the pointer on it. See [Licensing](topic:licensing).
