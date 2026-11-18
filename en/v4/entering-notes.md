---
title: Entering Notes
topic: entering-notes
summary: Writing notes and rests at the caret, then selecting, moving, copying, beaming and deleting them.
---

Notes go in at the caret, the flashing mark that shows where the next note will be written. One key press, or one click on a button, writes a note of the value and hand you want, and the caret moves on by the room that note takes in its bar. This page takes you from an empty ruled score to a line of notes, and shows how to change what you have written.

## Write your first bar

This fills a bar of 2/4 with four quavers, right hand first.

1. Make a new score in 2/4 with no anacrusis. See [Starting a Score](topic:new-score). The caret is at the start of the first bar. If it is not flashing, click just after the first barline.
2. Press `Shift+F`. A right-hand quaver is written and the caret moves a quarter of the way along the bar.
3. Press `F`. A left-hand quaver is written.
4. Press `Shift+F`, then `F` again.

The bar is full, and the caret is now in the next bar, ready for you to carry on.

If you would rather use the pointer, click the buttons in the note toolbox instead of pressing keys. They do the same thing.

![A new 2/4 march with four quavers in its first bar and the caret at the start of the second](images/v4/first-bar-written.png){: width="900" }

## The caret

The caret is a thin upright bar with a short stroke across its top and bottom. It flashes while the score has the keyboard. If you cannot see it, click in the music.

When a score opens, the caret is at the start of the first bar.

| To move the caret | Do this |
|---|---|
| To a place in the music | Click there |
| A little left or right | `Left` or `Right` |
| To the line above or below | `Up` or `Down` |
| To the start of the next bar | `Space` |
| To the next or the previous bar | `Tab` or `Shift+Tab` |

Clicking between notes moves the caret and selects nothing. Clicking on a note selects that note as well.

The caret cannot go into the clef or the time signature at the start of a line, or past the end of the line.

### With several instruments on a system

The caret stands on one instrument's line at a time, and it is only as tall as that line. What you type is written on that line. `Down` moves from one line of a system to the line below it, and from the last line to the first line of the next system. `Up` does the reverse. Clicking on a line puts the caret on it.

![A system of snare, tenor and bass with the caret on the tenor's line](images/v4/caret-on-one-line.png){: width="819" }

See [Instruments and Staves](topic:instruments).

## The note toolbox

The note toolbox is the column of buttons at the right of the window. Show or hide it with `View` ▸ `Show` ▸ `Note toolbox`. It has two tabs, `Notes` and `Tenor`.

The `Notes` tab has three columns: left-hand notes, right-hand notes and rests. Each column runs from the semibreve at the top to the demisemiquaver at the bottom, so a row is one note value three ways. Rest the pointer on a button to see its name, such as `Right quaver`.

Clicking a button writes that note or rest at the caret. There is no separate step of choosing a value and then placing it.

Below the notes are five barline buttons and a `Time signature` button. The barline buttons work only while `Edit` ▸ `Select Bar Lines` is ticked. The `Time signature` button is for the bar the caret is in.

The `Tenor` tab holds the tenor flourishes. See [Instruments and Staves](topic:instruments).

![The note toolbox, Notes tab: left-hand notes, right-hand notes and rests, then the barline buttons and the time signature button](images/v4/note-toolbox-notes.png){: width="168" }

## Notes and rests from the keyboard

Each note value has a letter. The letter alone writes a left-hand note. With `Shift` it writes a right-hand note. With `Ctrl` it writes a rest.

| Value | Left hand | Right hand | Rest |
|---|---|---|---|
| Semibreve | `A` | `Shift+A` | `Ctrl+A` (Mac only) |
| Minim | `S` | `Shift+S` | `Ctrl+S` (Mac only) |
| Crotchet | `D` | `Shift+D` | `Ctrl+D` |
| Quaver | `F` | `Shift+F` | `Ctrl+F` |
| Semiquaver | `G` | `Shift+G` | `Ctrl+G` |
| Demisemiquaver | `H` | `Shift+H` | `Ctrl+H` |

On a Mac the rest keys use the `Control` key, not `Cmd`. On Windows and Linux, `Ctrl+A` is `Select All` and `Ctrl+S` is `Save`, so use the toolbox buttons for a semibreve or minim rest.

A right-hand note is drawn above the staff line and a left-hand note below it.

### Changing the hand

Select the notes and press `Shift+K`, or right-click the selection and choose `Note` ▸ `Swap Hands`.

You can also change one note's hand with the pointer. Click the note to select it, then drag its note-head straight up for the right hand or down for the left.

### Dotted notes

A dot is added to a note that is already written. Select the note or rest and press `.`, or right-click it and choose `Note` ▸ `Dot`. Do the same again to take the dot off. `Shift+.` gives a double dot.

With an even number of notes selected, and no rests among them, the `.` key works on the notes in pairs. The first note of each pair takes the dot and the second is halved, so two quavers become a dotted quaver and a semiquaver, and the bar still adds up. The `-` key does the opposite: the second note takes the dot and the first is halved. The dot and cut buttons on the editing toolbar do the same as the two keys.

### Longer and shorter

To change the value of notes you have written, select them and press `Shift+M` to make them one step longer, or `Shift+N` one step shorter. The same commands are on the right-click menu as `Note` ▸ `Increase Duration` and `Decrease Duration`.

## Where a note lands

A note is written exactly where the caret is. The notes already in the bar are not moved to make room.

After each note or rest the caret moves on by that note's share of the bar. A crotchet in 2/4 moves it half a bar, a quaver a quarter of a bar. Type a bar straight through and it comes out evenly spaced.

This is the `Proportional Spacing` setting, in the `Engraving` pane of `File` ▸ `Score Properties…`. With it unticked, the caret moves only just past the note you drew, and you space the bar yourself.

A note typed straight after `Tab` or `Space` lands with its stem on the barline. Beautify moves it clear.

To even out the spacing of music that is already written, use Beautify. See [Layout and Spacing](topic:layout).

### At the end of a bar and of a line

When a bar is full, the caret has reached the next bar and the next note goes into that bar. Nothing stops you putting too many notes in a bar. The Bar Audit marks it if you do.

The caret does not run on to the next line by itself. If the caret is past the last bar of the line, a note key writes nothing and the caret stays where it is. Press `Tab` to go to the first bar of the next line.

## Selecting

Selected notes are shown with a shaded band over them.

| To select | Do this |
|---|---|
| One note or rest | Click it |
| A run of notes | Drag across them, or click at one end and `Shift`-click at the other |
| One more note at a time | `Shift+Left` or `Shift+Right` |
| Everything in the music area the caret is in | `Edit` ▸ `Select All`, or `Cmd+A` on a Mac, `Ctrl+A` on Windows and Linux |
| A whole bar | Double-click in it |
| A whole part | Click a third time |
| Nothing | `Esc`, or press an arrow key |

![A line of music with four notes selected under a shaded band](images/v4/notes-selected.png){: width="823" }

### Notes or bar lines

The `Edit` menu has two ticks, `Select Notes` and `Select Bar Lines`. They decide what clicking and dragging can pick up. A score starts with `Select Notes` ticked and `Select Bar Lines` unticked, so dragging across a barline selects the notes either side and leaves the barline alone. Tick `Select Bar Lines` when you want to select, change or delete a barline. One of the two is always ticked.

### Bars and parts

From the keyboard, `Cmd+Up` on a Mac or `Ctrl+Up` on Windows and Linux widens the selection one step: from notes to their bar, and from a bar to its part. With nothing selected it selects the bar the caret is in. `Cmd+Down` or `Ctrl+Down` steps back in.

With a bar selected, `Tab` and `Shift+Tab` move to the next and the previous bar. `Shift+Right` and `Shift+Left` take in more bars or fewer, and so does a `Shift`-click in another bar.

Note keys do not write while a bar or a part is selected. The first key press lets the selection go. Right-click a selected bar or part for the commands that act on it. See [Layout and Spacing](topic:layout).

## Moving, copying and deleting

### Move

Drag a selection to move it. You can drag it along its line, onto another line, or onto another instrument's line of the same system.

To move a selection a very small distance, nudge it. Use the `Nudge left` and `Nudge right` buttons on the editing toolbar, or these keys:

| | Nudge left | Nudge right |
|---|---|---|
| Mac | `Option+Shift+Left` | `Option+Shift+Right` |
| Windows | `Ctrl+Shift+Left` | `Ctrl+Shift+Right` |
| Linux | `Alt+Shift+Left` | `Alt+Shift+Right` |

### Copy, cut and paste

| Command | Mac | Windows and Linux |
|---|---|---|
| `Cut` | `Cmd+X` | `Ctrl+X` |
| `Copy` | `Cmd+C` | `Ctrl+C` |
| `Paste` | `Cmd+V` | `Ctrl+V` |

The three commands are also on the `Edit` menu, on the standard toolbar and on the right-click menu.

`Paste` puts the notes in at the caret. If notes are selected, the pasted notes replace them. What you paste comes out selected, so you can nudge it or drag it straight away. You can paste the same notes as many times as you like, and into another open score.

To paste somewhere other than the caret, right-click in the music at that place and choose `Paste`.

If the line runs out before the pasted notes do, the status bar tells you how many did not fit. They are still on the clipboard.

To copy by dragging, hold `Option` on a Mac, or `Ctrl` on Windows and Linux, while you drag the selection. A copy is left behind.

### Type over a selection

If notes are selected when you write a note or a rest, the selected notes are deleted and the new one is written at the caret. One undo puts everything back.

### Delete

Select what you want to remove and press `Delete` or `Backspace`.

With nothing selected, `Backspace` works back from the caret a step at a time. The first press moves the caret to just after the note before it. The second selects that note. The third deletes it.

Deleting a barline joins the two bars it separated. Their notes stay where they are.

## Undo and redo

| Command | Mac | Windows | Linux |
|---|---|---|---|
| `Undo` | `Cmd+Z` | `Ctrl+Z` | `Ctrl+Z` |
| `Redo` | `Cmd+Shift+Z` | `Ctrl+Y` | `Ctrl+Shift+Z` |

Both are on the `Edit` menu and the standard toolbar. The menu names what it will undo, such as `Undo Insert note`. A drag counts as one step, however far you moved the notes.

## Beams

A beam joins a note to the note before it.

**Automatically.** With `Auto-join note tails as beams` ticked, notes that fall in the same beat are joined for you, and beaming by hand has no effect. The setting is under `Beams` in the `Engraving` pane of `File` ▸ `Score Properties…`. Automatic beaming needs the Studio Edition. In the Community Edition notes are beamed by hand.

**By hand.** Select the notes and press `L`, or right-click them and choose `Group` ▸ `Beam`. The beam button on the editing toolbar does the same. Every selected note except the first is joined to the note before it. With one note selected, that note is joined to the note before it. Do the same again to break the beams.

`Shift+L`, or `Group` ▸ `Single Beam Only`, draws a single beam at the join however short the notes are.

**Which way a short beam points.** Where automatic beaming decides a note needs a short beam of its own, it draws it back from the stem. To have it flow forward from the stem instead, right-click the note and choose `Note` ▸ `Force Cut Forward`.

![Four semiquavers as written, each with its own tails, and joined by a beam after pressing L](images/v4/beams-by-hand.png){: width="482" }

## A tenor on five lines

On a tenor's five-line stave a note is written at a pitch, and hands are not shown. The stave itself is described in [Instruments and Staves](topic:instruments).

When the caret is on a five-line stave it has a short mark across it at the pitch the next note will take, and the `Notes` tab of the toolbox changes. It then shows one column of notes, one of rests, and seven pitch buttons with the highest at the top.

| To | Do this |
|---|---|
| Set the pitch for the next note | Click at that height on the stave, press `W` to go up or `Q` to go down, or click a pitch button |
| Write a note at that pitch | Press a note key, or click a note button. `Shift` makes no difference here |
| Move a selected note up or down | `Shift+W` or `Shift+Q`. With one note selected, you can also drag its note-head |
| Add a note to make a chord | Select the note, set the pitch with `W` and `Q`, then press `E`. Or select the note and click a pitch button |
| Take a note out of a chord | The same again at that pitch, or right-click the note-head and choose `Remove This Pitch` |

Right-clicking a selected note also offers `Add Pitch`, with a list of the pitches it does not have. Holding `Alt` (`Option` on a Mac) and clicking at a height on the stave adds a note-head there to the selected note, or removes the one that is there. A note always keeps at least one pitch.

![The caret on a tenor's five-line stave, and the toolbox showing notes, rests and the seven pitch buttons](images/v4/caret-on-a-tenor-stave.png){: width="900" }

## The Bar Audit

The Bar Audit marks any bar that does not add up to its time signature. It draws a zig-zag under the bar: blue under a bar that holds too little, red under a bar that holds too much. Rest the pointer on the mark to read what is wrong.

An empty bar is not marked. Neither is an anacrusis, nor the short bar at the end of the part that completes it.

The marks are there to help you write. They are not printed or exported. Turn them off or on with `View` ▸ `Bar Audit`.

![A line with one bar holding too little, marked in blue, and one holding too much, marked in red](images/v4/bar-audit.png){: width="791" }

## What next

Grace notes, rolls, accents, dynamics, tuplets, ties and unisons are all added to notes you have already written. See [Rudiments, Rolls and Tuplets](topic:rudiments).

For every key the editor answers to, see [Keyboard Shortcuts](topic:shortcuts).
