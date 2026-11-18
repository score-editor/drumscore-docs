---
title: Instruments and Staves
topic: instruments
summary: Writing snare, tenor and bass together on one system, and writing a tenor at pitch on a five-line stave.
draft: true
---

A score can be written for more than one instrument. Each instrument has a line of its own, the lines of a system are joined by a bracket, and you can show, print or export any of them by themselves. A tenor can be written on one line, as a snare is, or at pitch on a five-line stave.

## Which scores can have this

Only a score in the `Standard` general layout can have a second instrument or a five-line stave. A score keeps the general layout it was created with, so a score in the `DrumScoreEditor` layout cannot gain either. Its one instrument can still be changed to a `Tenor` or a `Bass`. The general layout is chosen when the score is made: see [Starting a Score](topic:new-score).

Adding instruments, and choosing which are on a line or shown, needs the Studio Edition. See [Licensing](topic:licensing).

## Add a tenor and a bass to a score

This starts from a snare score in the `Standard` layout.

1. Choose `File` ▸ `Score Properties…` and open the `Notation` pane.
2. Under `Instruments`, choose `Add Instrument`. A second row appears, set to `Tenor`.
3. In the tenor's row, choose its stave: `One Line` or `Five Lines`. Choose now. Once the tenor has notes its stave cannot be changed.
4. Choose `Add Instrument` again. The third row is set to `Bass`.
5. Type the name you want for each instrument, then choose `OK`.
6. Right-click in the music and choose `Staff Line` ▸ `Instruments` ▸ `Whole Tune` ▸ `Tenor`.
7. Do the same for `Bass`. The menu is now called `System`, because the line you click holds two instruments.

Steps 6 and 7 are needed because the table only says which instruments the score has. The `Instruments` menu puts one on the lines. Every system of the tune now has three lines, the new ones empty and ready to write on.

<!-- screenshot: Score Properties, Notation pane, of a Standard-layout score: the Instruments group with three rows (Snare; Tenor with Stave set to Five Lines; Bass with its Hands tick box), the Add Instrument button, and Show Names set to First System of a Tune -->

### For every new score

The same table is in `Settings` ▸ `New Score Defaults` ▸ `Notation`. What you list there is what each new score is written for, and a new score has a line for every instrument on every system from the start. A tune you add to a score later is written for that score's own instruments.

## The instrument table

Each row is one instrument. The order of the rows is the order the lines are drawn in, top to bottom. The controls have no headings: rest the pointer on one to see what it is.

| In a row | What it sets |
|---|---|
| Type | `Snare`, `Tenor` or `Bass`. |
| Name | What the instrument is called on the page and in the menus. A new row is named for its type in small letters, so type it as you want it printed. |
| Stave | `One Line` or `Five Lines`. Tenor rows only. |
| `Hands` | Bass rows only. See *The bass without hands* below. |
| Clef | `None`, `Unpitched`, `Treble` or `Bass`. A new tenor or bass starts in the bass clef, a snare in the unpitched clef. |
| ▲ and ▼ | Move the instrument up or down the system. |
| − | Removes the instrument. In `Score Properties…` this also removes everything written for it. |

What the table will not let you do:

- **Add a second instrument outside the `Standard` layout.** `Add Instrument` is greyed, and says "More than one instrument is offered in the Standard format".
- **Choose `Five Lines` outside the `Standard` layout.**
- **Change the stave of an instrument that has notes.** A note on one line and a note on five are written differently, and one is never turned into the other. A tenor on five lines that has notes keeps its type as well.
- **Choose the clef of a tenor on five lines.** It is always the bass clef.
- **Remove the last instrument.**
- **Untick `Clef on every line`** while the score has more than one instrument. Each line has to say which instrument it is.

## How a system is drawn

A system has one line for each instrument written on it. A bracket at the left joins them.

| Setting | Where | What it does |
|---|---|---|
| `Show Names` | `Notation` pane | Writes each instrument's name at the left of its line, before the bracket. `Off`, `First System of a Tune` or `Every System`. `First System of a Tune` also names any system whose instruments are not those of the system before it. |
| `Space Between Instruments` | `Engraving` pane | The clear space between the lines of one system. It follows `Space Between Lines` until you type a value of its own. |
| `Join Barlines` | Right-click a system, `System` ▸ `Join Barlines` | Ticked, the barlines run through the gaps between the lines. They stop short of any words or figures in the gap. It is set for one system at a time. |

Names are drawn in the same font as the line numbers. With line numbers on, every instrument's line has a number of its own, because the numbers count lines and not systems.

A 1st or 2nd time bracket, and words written on a barline or over a bar, are drawn on the top line of the system only.

<!-- screenshot: one system of The Young MacGregor with Snare, Tenor (five lines, bass clef, two sharps) and Bass lines: bracket at the left, names shown before the bracket, barlines joined through the gaps, line numbers on -->

### Leaving an instrument off a line

Not every system needs every instrument. Right-click a system and choose `System` ▸ `Instruments`, then untick an instrument to take its line off that system. The items under `Whole Tune` do the same for every system of the tune. Taking a line off removes what was written on it; `Undo` puts it back. A system always keeps at least one line.

A line or a part that you insert is given the same instruments as the one beside it.

Right-click menus cannot be pictured here.

## Showing only some instruments

`View` ▸ `Instruments` has a tick for each instrument in the score. Untick one to hide its lines. The systems close up and the pages are flowed again, so a snare part can be taken from a full score.

While any instrument is hidden:

- a bar across the top says which are showing, and "Editing is paused while instruments are hidden". Choose `Show All` to edit again;
- printing, and export to PDF and to a picture, give the pages as you see them;
- the score itself is not changed. Saving keeps every instrument.

<!-- screenshot: the same score with only the snare shown: the banner "Showing Snare. Editing is paused while instruments are hidden." and its Show All button above the page -->

## Writing on a system

The caret stands on one instrument's line, and what you type goes on that line. See [Entering Notes](topic:entering-notes) for moving it between lines.

To move notes to another instrument, select them and drag them onto that instrument's line of the same system. A tenor flourish can be dragged to another line the same way. Barlines belong to the whole system and stay where they are.

A five-line stave takes only notes written at a pitch, and a one-line staff takes only notes without one. So notes cannot be dragged or pasted between a five-line tenor and a snare, a bass or a one-line tenor. Rests can.

## The tenor on five lines

A tenor set to `Five Lines` is written in the bass clef with a key signature of two sharps, F and C. It has seven notes and no others:

| | Lowest | | | | | | Highest |
|---|---|---|---|---|---|---|---|
| Note | B | C♯ | D | E | F♯ | G | A |

They run from the second line of the stave up to the top line, so there are no ledger lines and no accidentals. Hands are not shown. Every stem points down, and flourishes are drawn higher so that they clear the stave.

Writing at a pitch, chords, and moving a note-head up or down are described in [Entering Notes](topic:entering-notes), under *A tenor on five lines*. Flourishes are on the `Tenor` tab of the note toolbox: see [Rudiments, Rolls and Tuplets](topic:rudiments).

<!-- screenshot: two bars of a five-line tenor stave: bass clef, two sharps, single notes on several pitches, one two-note chord, and a flourish drawn above the stave -->

## The bass without hands

A bass part is often written for its rhythm alone. Untick `Hands` in a bass row and every note of that instrument is written on the line, with the line through the middle of the note-head, instead of above or below it.

- Whatever way you enter a note on that line, it is written without a hand.
- Notes already on the line are rewritten the same way.
- If you tick `Hands` again, every note on the line becomes a right-hand note, and you set the left hands again yourself.

## Pens for a one-line tenor

On one line, tenor corps mark each drum with a highlight pen. In the `Highlighters` pane, under `Pens and pitches`, choose the note and octave each pen stands for. A note on a tenor line highlighted with that pen is then played back at that note. Pens mean nothing to a five-line stave, where the note-head gives the pitch.

## Playing and exporting

Quick Play plays every instrument's line together. A five-line tenor sounds the pitches written, chords included.

MusicXML export writes one part for each instrument, in the order of the table. A five-line tenor is written at its pitches, in the bass clef with two sharps. See [Printing and Export](topic:export).
