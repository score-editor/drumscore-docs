---
title: Layout and Spacing
topic: layout
summary: Spacing notes along a line with Beautify, nudge and squeeze, then line heights, the page, and how the music runs from page to page.
---

This page is about where things sit: notes along a line, lines down the page, and music from one page to the next. Most of it is done for you.

## Tidy a score you have just typed

1. Press `Alt+B` (`Option+B` on a Mac), or right-click in the music and choose `Score` ▸ `Beautify`.
2. Where a bar is still not as you want it, move its notes by hand. See *Move notes by hand* below.
3. Right-click in that bar and choose `Measure` ▸ `Lock Against Beautify`.
4. Beautify again whenever you like. The locked bars stay as you left them.

Beautify needs the Studio Edition. So do the `Measure` and `Part` submenus of the right-click menu. See [Licensing](topic:licensing).

<!-- screenshot: the same line of a 2/4 march before and after Beautify: before, notes bunched at the left of each bar with the first stem on the barline; after, evenly spaced -->

## Beautify

Beautify lays out every note where an engraver would put it. It always works on the whole score, every tune and every page, and it is one step to undo. There is no Beautify for one bar, one line or a selection.

A note typed straight after `Tab` or `Space` lands with its stem on the barline. Beautify moves it clear.

Beautify leaves two things alone:

- **Locked bars.** The status bar says how many, such as `Beautified. 1 locked bar was left alone`, and a padlock shows over each for a few seconds.
- **The barlines**, unless `Allow barlines to move` is ticked.

### Lock a bar

`Measure` ▸ `Lock Against Beautify` is ticked while the bar is locked. Choose it again to unlock. To lock several bars at once, select them and right-click the selection.

Locking moves nothing, and a locked bar can still be edited. Only automatic spacing passes it by: Beautify, making a tuplet, and `Redistribute Staff Content`.

`View` ▸ `Bar Locks` shows a padlock over every locked bar.

### Spacing settings

These are under `Spacing` in the `Engraving` pane of `File` ▸ `Score Properties…`.

| Setting | What it does |
|---|---|
| `Spacing Policy` | How a bar shares its width among its notes. See the next table. |
| `Allow barlines to move` | Beautify places the barlines as well as the notes, so that a note gets the same room wherever it falls on the line. It replaces barlines you have placed by hand. Studio Edition. |
| `Beautify tuplets as they are made` | Making a tuplet re-spaces its bar. See [Rudiments, Rolls and Tuplets](topic:rudiments). |
| `Proportional Spacing` | Where the caret goes after each note you type. See [Entering Notes](topic:entering-notes). |

The middle two are offered only in the `Standard` layout with the `TraditionalSpacing` policy. Otherwise they are greyed and shown unticked.

| `Spacing Policy` | How a bar is spaced |
|---|---|
| `TraditionalSpacing` | A longer note gets more room than a shorter one, but not in strict proportion, as in engraved music. A new Studio Edition score starts with this. |
| `AmortizeAcrossBar` | Room in proportion to each note's length. Room taken by grace notes is shared back across the whole bar. Most older scores were written this way. |
| `AmortizeAcrossBeat` | Each beat gets an equal share of the bar, and the sharing is done within the beat. |
| `RecoverASAP` | In proportion to length. Room taken by grace notes comes back from the notes straight after them. |
| `FlatSpacedInBar` | Every note in the bar gets the same room. |
| `FlatSpacedByBeat` | Every beat gets the same room, and so does every note within a beat. |

Changing the policy does not re-space what is already written. The next Beautify does. The one thing you may see at once on choosing `TraditionalSpacing` is a slight nudge where flams are: it draws a flam's grace note closer in to its main note.

## Move notes by hand

**Nudge.** Select notes and move them a little at a time with `Nudge left` and `Nudge right` on the editing toolbar, or the nudge keys listed in [Entering Notes](topic:entering-notes). A nudge to the left stops at the start of the line.

**Nudge a barline.** Tick `Edit` ▸ `Select Bar Lines`, select the barline and nudge it the same way. A note the barline passes then belongs to the bar on the other side. A barline cannot pass another barline.

**Squeeze.** Select three or more notes on one line. The status bar says `Drag either end of the selection to space these notes.` Drag one end: the other end stays put and the notes between keep their proportions. From the keyboard, `Cmd+Right` on a Mac, or `Ctrl+Right` on Windows and Linux, spaces the run out to the right. `Cmd+Left` or `Ctrl+Left` draws it in. If two notes would collide, nothing moves.

<!-- screenshot: six selected semiquavers shown twice: as typed, and after dragging the right-hand end of the selection so the run is wider and the first note has not moved -->

## Staff lines, bars and parts

Right-click on a staff line. The last submenu is `Staff Line`, or `System` where the line carries more than one instrument.

There is no setting for how far a line is set in from the margin. A line is indented by itself where it needs room at the left, for line numbers, part numbers, instrument names or the bracket.

| `Staff Line` ▸ | What it does |
|---|---|
| `Insert Staff Above`, `Insert Staff Below` | Adds a blank line. |
| `Delete This Staff Line` | Removes the line. A part keeps at least one. |
| `Clone This Staff Line` | Copies the line, bars and notes, to a new line below. Studio Edition. |
| `Redistribute Staff Content` | Spaces the line's bars evenly. Their notes move with them. Studio Edition. |
| `Fill Line to the Margin` | Ticked, the line runs to the margin and edits re-space its bars. Unticked, it ends where its music ends and its bars stay where you put them. Studio Edition. |

`Measure` has `Insert Measure Before`, `Insert Measure After` and `Delete Measure`. `Bars per line`, in the `Notation` pane, is the number a newly added part is ruled with.

`Part` acts on the whole part, whichever of its lines you clicked. It adds and deletes parts, adds a line to the end of the part or deletes its last one, and has four ticks:

| `Part` ▸ | What it does |
|---|---|
| `Anacrusis` | Adds a pickup bar at the start of the part, or removes it. |
| `Repeated` | Switches the part between written once with repeat barlines and written out in full. |
| `2nd Time Staff Line` | Adds or removes a line for the second time through. |
| `Volta` | Adds or removes 1st and 2nd time endings at the end of the part. |

## Line heights

`Line Heights` is under `Staff lines down the page` in the `Engraving` pane. It needs the Studio Edition.

| Choice | How tall each staff line is drawn |
|---|---|
| `Legacy` | The same fixed room above and below every line. This is how a score from an earlier version has always been drawn. |
| `Uniform` | Every line of a tune is as tall as its tallest line's marks need, so the lines stay evenly spaced. With several instruments, each instrument's lines are sized among themselves. |
| `Fit Each Line` | Each line is as tall as its own marks need. |

Once a score leaves `Legacy` it cannot go back: `Legacy` is no longer in the list. The staff lines stay where they were at the moment it leaves.

The gap between lines is set just below:

- In `Legacy`, `Staff Line Gap Factor` adds or takes away space, as a percentage of the staff line's height.
- Otherwise, `Space Between Lines` is the clear space between the marks of one line and the next. `Space Between Instruments` is the same within one system.

`Distribute Staff Lines Evenly` spreads the lines over the height of the page instead. The score then stays on one page and can hold only one tune.

<!-- screenshot: the same four lines of a tune drawn three times, labelled Legacy, Uniform and Fit Each Line; one line carries accents and tuplet numbers so it is taller than the rest -->

## The page

The `Page` pane of `File` ▸ `Score Properties…` sets the paper.

| Setting | Choices |
|---|---|
| `Paper size` | `A4`, `A3`, `Letter` or `Legal`. |
| `Default orientation` | `Portrait` or `Landscape`. |
| `Size`, under `Margins` | `Small`, `Medium`, `Large` or `Custom`. |
| `Values` | The `Left`, `Top`, `Right` and `Bottom` margins. Type in them when `Size` is `Custom`. The list beside them shows the figures in `mm` or `inches`. |
| `Binding` | `Off`, `Left edge` or `Top edge`, with a `Width`: extra room kept clear on that edge. |
| `Mirror margins on facing pages` | The binding room changes sides on alternate pages. |

<!-- screenshot: Score Properties showing the Page pane, with Size set to Custom and Binding set to Left edge -->

**The size of the music.** Right-click in the music and choose `Score` ▸ `Point Size`, then a size from 12 to 48. It applies to the whole score. In the Studio Edition, `Music Font Size` in the `Music Font` pane takes a figure of your own when the score uses a music font.

## How the music flows

A music area is the box on a page that holds a tune's staff lines. You do not normally place it. When a tune's lines do not fit on the page, the tune runs on to as many pages as it needs, and adding or deleting a staff line re-flows the score.

Running on to further pages is part of the Studio Edition. A score made in the Community Edition keeps to one page, with its staff lines spread evenly down it.

- A part is kept together on one page where it can be. The lines of one system are never separated.
- A tune's header is never left by itself at the foot of a page. If the header and the first part do not fit, the tune starts a new page.

In `File` ▸ `Score Properties…`, under `Tunes`, each tune has two layout choices. `Start on a new page` makes the tune begin a fresh page. `Orientation` is `Inherit score default`, `Portrait` or `Landscape`, and a tune turned the other way from the page before it starts a new page.

### A page arranged by hand

A score with `Page Arranged By Hand` ticked, in the `Page` pane, is never re-flowed. Everything stays where you put it, and the score keeps to one page. A score from an earlier version opens this way if a tune has more than one music area on a page, or if text or a picture was placed on the page outside the header and footer.

On an arranged page you place the music areas yourself.

| To | Do this |
|---|---|
| Add a music area | Right-click on empty paper and choose `Insert Music Area`. It arrives holding one part. |
| Take hold of an area | Click on its edge, or inside it but not on the music. An outline with handles appears. |
| Resize it | Drag an edge or a handle. |
| Move it | Drag inside the outline, or use the nudge keys, with `Up` and `Down` as well. |
| Remove it | Press `Delete` while it is held, or right-click it and choose `Delete Music Area`. A tune keeps at least one. |
| Let go | Click inside it, or anywhere else. |

You can tick `Page Arranged By Hand` only while the score has one page and one tune. To untick it, first delete the extra music areas, and move loose text and pictures into the header or footer.

<!-- screenshot: an arranged page with two music areas side by side, the right-hand one held and showing its outline and handles -->

## This score, or every new score

Everything above that is in `File` ▸ `Score Properties…` belongs to the score in front of you and is saved in it. In the Studio Edition, `Settings` ▸ `New Score Defaults` has the same `Notation`, `Engraving` and `Page` panes for scores you have yet to make. `Page Arranged By Hand` and `Tunes` are not there. See [Score Properties](topic:score-properties) and [Settings](topic:settings).

Headers, footers, text and pictures are in [Text and Headers](topic:text-and-headers). Several instruments on a system, and the tenor's five-line stave, are in [Instruments and Staves](topic:instruments). For paper copies and files, see [Printing and Export](topic:export).
