---
title: Rudiments, Rolls and Tuplets
topic: rudiments
summary: Putting flams, drags, rolls, accents, dynamics, tuplets, ties, unison marks and tenor flourishes on your notes, and keeping phrases in a rudiment library.
---

Most of what is on this page is added to notes that are already written. Select the notes first, then put the mark on. See [Entering Notes](topic:entering-notes) for writing and selecting notes.

## Three ways to put a mark on

- **A key.** Most marks have one. Press it again to take the mark off.
- **The `Editing Toolbar`.** It runs along the top of the window and works while something is selected. Each button's tip names its key, such as `Flam [z]`. Show it with `View` ▸ `Show` ▸ `Editing Toolbar`.
- **The right-click menu.** Right-click the selected notes. The marks are grouped under `Note`, `Group` and `Embellishment`. A tick shows that the selection already has the mark. Choose a ticked item to take the mark off.

A key and a menu item treat a mixed selection differently. The key changes each note in turn, so notes that had the mark lose it and the others gain it. The menu makes every selected note the same.

<!-- screenshot: the right-click menu on three selected notes, with the Embellishment submenu open showing Accent, Heavy Accent, Marcato, Tenuto, Staccato, Fermata, Flam, Drag, Open Drag, Swiss Ruff and Ruff -->

## Grace notes

| To write | Key | `Editing Toolbar` | Right-click, `Embellishment` |
|---|---|---|---|
| A flam | `Z` | `Flam [z]` | `Flam` |
| A drag | `X` | `Drag [x]` | `Drag` |
| An open drag | `C` | `Open drag [c]` | `Open Drag` |
| A Swiss ruff | `V` | `Swiss ruff [v]` | `Swiss Ruff` |
| A ruff | `B` | `Ruff [b]` | `Ruff` |

You do not choose left or right. The grace notes are written on the hand opposite the note they lead into. To change the hand of a note, press `Shift+K` or choose `Note` ▸ `Swap Hands`. The grace notes change sides with it.

A note carries one of these at a time. Putting a drag on a note that has a flam replaces the flam.

A ruff is also known as a rough.

To write a Swiss ruff that stands by itself, with no main note, press `I` for the left hand or `Shift+I` for the right. It takes up no time in the bar.

![A flam, a drag, an open drag, a Swiss ruff and a ruff](images/v4/grace-notes.png){: width="495" }

### Ruffs before the barline

A Swiss ruff or a ruff on the first note of a bar can be drawn before the barline, leading into the bar, with its note-head on the beat. Tick `Ruffs before the barline` in the `Engraving` pane. It only happens where the bar before leaves room. Nothing is moved to make space. This setting needs the Studio Edition.

The `Engraving` pane is in `Settings` ▸ `New Score Defaults` for new scores, and in `File` ▸ `Score Properties…` for the score in front of you. See [Score Properties](topic:score-properties).

![The same two bars with the ruff inside the bar, and with it drawn before the barline](images/v4/roughs-before-barline.png){: width="757" }

## Rolls and buzzes

Press `R`, use `Buzz / roll [r]` on the `Editing Toolbar`, or choose `Note` ▸ `Roll`.

- **One note selected** becomes a roll.
- **Several notes selected** become one roll. Each note except the last is rolled and tied to the next. The last note is left plain: it is the note the roll arrives on. The notes may run on from the end of one line to the start of the next.

Do the same again to take the roll and its ties off.

The number of slashes through the stem is worked out from the note's length and the time signature. To choose it yourself, press `Shift+R` or choose `Note` ▸ `Override Slashes`. Each press steps through one, two and three slashes.

`Note` ▸ `Stroke Count…` sets how many strokes the roll is played with, from 4 to 13. Taking the roll off a note clears both choices.

Two settings change how rolls are drawn:

- `Roll ties below accents`, in the `Engraving` pane, pulls a roll's tie down close over the note-heads so that it passes under any accent.
- `Use Z through stem for rolls`, in the `Music Font` pane, draws a Z through the stem instead of slashes. It applies when the score uses a music font, and the pane is part of the Studio Edition.

![A five-stroke roll: two rolled semiquavers tied on to an accented quaver](images/v4/five-stroke-roll.png){: width="495" }

## Dotted and cut notes

| To write | Key | `Editing Toolbar` | Right-click, `Note` |
|---|---|---|---|
| A dot | `.` | `Dot [.]` | `Dot` |
| A cut | `-` | `Cut [-]` | `Cut` |
| A double dot | `Shift+.` | | `Double Dot` |

The dot and cut keys work on pairs. Select an even number of notes and press `.`: the first note of each pair is dotted and the second is halved, so two quavers become a dotted quaver and a semiquaver. Press `-` for the other way round: a semiquaver and a dotted quaver. The bar still adds up. Press the key again to put the pair back.

With an odd number selected, or a rest among them, `.` dots each one and `-` halves each one.

A dot can go on a rest. A note or rest has a dot or a double dot, not both.

## Accents and other marks on a note

| To write | Key | `Editing Toolbar` | Right-click |
|---|---|---|---|
| An accent | `Y` | `Accent [y]` | `Embellishment` ▸ `Accent` |
| A heavy accent | `Shift+Y` | `Heavy accent [shift-y]` | `Embellishment` ▸ `Heavy Accent` |
| A marcato | `Alt+O` (`Option+O` on a Mac) | | `Embellishment` ▸ `Marcato` |
| A staccato | `Shift+O` | | `Embellishment` ▸ `Staccato` |
| A tenuto | | | `Embellishment` ▸ `Tenuto` |
| A fermata | | | `Embellishment` ▸ `Fermata` |
| A backstick | `Shift+B` | | `Note` ▸ `Backstick` |
| Both sticks together | | | `Note` ▸ `Both Strike` |
| A shoulder strike | | | `Note` ▸ `Shoulder Strike` |

A note has one of accent, heavy accent, marcato, tenuto and fermata. Choosing another replaces it. A staccato can sit with an accent, a marcato or a tenuto.

`Marcato`, `Tenuto`, `Staccato` and `Fermata` are on the menu in the Studio Edition only.

A backstick is drawn with a cross for its note-head. `Both Strike` draws a second note-head on the other hand's side of the line. `Shoulder Strike` draws a B above the note.

`Align all accents`, in the `Engraving` pane, lifts left-hand accents so that every accent in a bar sits on one row.

## Dynamics

In the Studio Edition the right-click menu has a `Dynamic` submenu: `ppp`, `pp`, `p`, `mp`, `mf`, `f`, `ff`, `fff` and `sfz`. Choose one to put it on the selected notes. A note has one dynamic, so choosing another replaces it. Choose the ticked one to take it off.

### Crescendo and diminuendo

| To write | Key | `Editing Toolbar` | Right-click, `Group` |
|---|---|---|---|
| A crescendo | `K` | `Crescendo [k]` | `Crescendo` |
| A diminuendo | `M` | `Diminuendo [m]` | `Diminuendo` |

With two or more notes selected, the hairpin runs from the first to the last. With one note selected, it runs from that note to the end of its bar. A hairpin can run on from one line to the next.

![A bar marked mf with a crescendo hairpin from its first note to its last](images/v4/dynamic-and-hairpin.png){: width="495" }

## Ties and slurs

Select two or more notes and press `T`, use `Tie [t]` on the `Editing Toolbar`, or choose `Group` ▸ `Tie / Slur`. The tie joins the first selected note to the last. It can run on from one line to the next.

With one note selected, `T` ties that note to the end of its bar. `Group` ▸ `Tie To End Of Bar` does the same. `Group` ▸ `Tie From Start Of Line` draws a tie coming into the note instead.

## Tuplets

Select the notes and press the number.

| To write | Key | Elsewhere |
|---|---|---|
| A triplet | `3` | `Triplet [3]` on the `Editing Toolbar`, or `Group` ▸ `Triplet` |
| A group of 2, 4, 5, 6, 7, 8 or 9 | That digit | `Group` ▸ `Other Irregular`, then the number |

- The group runs from the first selected note to the last. You need at least two things selected.
- A tuplet can start or end on a rest. Select the rest along with the notes.
- Press the same number again to take the tuplet off.
- Press a different number over the same notes to change it. A 5 replaces a 3.
- A tuplet cannot run across a line break.

### A tuplet inside a tuplet

Make the outer tuplet first. Then select the notes of the inner group and press its number. The inner tuplet is drawn on the opposite side of the notes from the outer one, so the two do not run into each other.

![A triplet whose last note is divided into an inner triplet, the outer number above and the inner below](images/v4/tuplet-nested.png){: width="495" }
![A triplet that begins on a quaver rest](images/v4/tuplet-starting-on-a-rest.png){: width="495" }

### How tuplets are drawn

These are in the `Engraving` pane, under `Irregular groups` and `Spacing`.

| Setting | What it does |
|---|---|
| `Tuplet number size` | Draws the number `Large`, `Medium` or `Small`. A new score starts at `Medium`. |
| `Irregular groups below notes` | Puts the number under the beams in a squared-off bracket, instead of above the music under a curved slur. |
| `Draw ties for irregular groups` | Draws the slur or bracket. Unticked, only the number is drawn. |
| `Beautify tuplets as they are made` | Making a tuplet re-spaces its bar from the tuplet's first note, which stays where it is. Taking a tuplet off does not re-space. It works in the `Standard` layout with the `Traditional spacing` spacing policy, and needs the Studio Edition. |

## Unison

Press `U`, use `Unison [u]` on the `Editing Toolbar`, or choose `Group` ▸ `Unison`, to mark the selected notes as unison.

- `Group` ▸ `Fill To Next Note` is ticked to start with: the mark runs on from each note to the next. Untick it, or press `Shift+U`, for a mark that stops at the note.
- `Group` ▸ `Include Grace Notes` is also ticked to start with: the mark takes in the note's grace notes. Untick it to leave them out.

Unison is highlighted in colour unless the score says otherwise. The `Unison` pane sets the colour, and can draw a bracket over the notes instead of the colour or as well as it. Choosing the bracket needs the Studio Edition.

![A unison bar shown with a colour highlight, and under a bracket](images/v4/unison-colour-and-bracket.png){: width="892" }

## Highlight pens

There are ten pens at the right-hand end of the `Editing Toolbar`, each drawn in its own colour. Select notes or rests and click a pen. Click the same pen again to take the highlight off. A note is under one pen at a time, so another pen replaces the first.

From the keyboard, hold `Shift` and press a digit: `Shift+0` is `Pen 1`, `Shift+1` is `Pen 2`, and so on to `Shift+9` for `Pen 10`.

The pens' colours belong to the score. Change them in the `Highlighters` pane. `Continuous highlights` there joins a run of highlighted notes into one band.

A pen can also stand for a note on a tenor line, so that a tenor score can be played back. See [Instruments and Staves](topic:instruments).

## Showing and hiding marks

In the Studio Edition, `View` ▸ `Markup` has three ticks: `Dynamics`, `Highlight Marks` and `Unison Marks`. Untick one to hide those marks. They stay in the score, and they come back when you tick it again. The score is printed and exported as it is shown.

## Tenor flourishes

The `Note Toolbox` at the right of the window has a `Tenor` tab with thirty flourish symbols. Show the toolbox with `View` ▸ `Show` ▸ `Note Toolbox`. Hold the pointer over a button to see its name.

1. Click in the music to put the caret where the flourish belongs.
2. Click the flourish on the `Tenor` tab.

A flourish takes up no time in the bar, and the caret stays where it is, so you can go on writing the notes under it. Make sure no notes are selected first: like a new note, a flourish replaces what is selected.

To remove a flourish, select it and press `Delete`.

| Family | Symbols |
|---|---|
| Reverses | Reverse left, Reverse right |
| Throwouts and pushouts | Throwout right, left and both; Pushout right, left and both |
| Figures of eight | Forward figure 8, Reverse figure 8, Flat figure 8, Reverse figure 8 up, Reverse figure 8 down |
| Crossovers and Quiggs | Crossover up and down; Quiggs up and down |
| Spins and bounces | Inward spin right and left; Bounce high and low |
| Cartwheels and feathers | Cartwheel, Split feather, Split feather cartwheel, Cartwheel split feather |
| Others | Fan, Butterfly, Reverse butterfly, Stop regular, Stop St Andrews |

Three more tenor marks are on the right-click menu. `Group` ▸ `Regimental Piano` and `Group` ▸ `Traditional Piano` draw a piano bracket from the first selected note to the last. `Note` ▸ `Shoulder Strike` is in the table above.

![The note toolbox, Tenor tab: thirty flourish buttons](images/v4/note-toolbox-tenor.png){: width="168" }

## Rudiment libraries

A rudiment library holds phrases you use often. You drag a phrase from the library into a score rather than writing it again. Each library is a `.dsl` file.

The `Rudiments` panel is part of the Studio Edition. Show it with `View` ▸ `Show` ▸ `Rudiments`. It sits down the left of the window.

![The Rudiments panel with two libraries, one open showing four phrases](images/v4/rudiments-panel.png){: width="240" }

### Open or make a library

Go to `Settings` ▸ `Libraries` ▸ `Rudiments`.

| Button | What it does |
|---|---|
| `New…` | Asks for a name and makes an empty library in your library folder. |
| `Add…` | Opens a `.dsl` file you already have. |
| `Remove` | Takes the library off the list. The file is not deleted. |
| `Properties` | Changes the library's title. |
| `Move Up`, `Move Down` | Change the order of the libraries in the panel. |
| `Copy to Library Folder…` | Copies libraries kept elsewhere into your library folder. The originals stay where they are. |

The libraries you add stay open between sessions. When none is open, the panel says `No rudiment libraries are open.` and offers `New…` and `Add…` itself.

In the panel, click a library's name to open it. One library is open at a time. Click the name again to close it.

### Put a rudiment into a score

Drag the phrase from the panel onto a line of music. Once the pointer is over the music the phrase is shown as real notes, beamed and spaced with what is already there. Let go where you want it. One `Undo` takes it out again.

### Save notes as a rudiment

1. Select the run of notes in the score.
2. Hold `Option` on a Mac, or `Ctrl` on Windows and Linux, and drag the notes onto the `Rudiments` panel.
3. Let go over the open library, at the place among its phrases where you want the new one.

Holding the notes over a closed library's name for a moment opens it. The library file is saved straight away.

### Tidy a library

- **Name a phrase.** Right-click it and choose `Name…`. The name shows when you hold the pointer over the phrase.
- **Reorder.** Drag a phrase up or down within its own library.
- **Remove.** Right-click the phrase and choose `Remove Rudiment`, or select it and press `Delete`. This cannot be undone.
