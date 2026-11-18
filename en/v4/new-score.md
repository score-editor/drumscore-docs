---
title: Starting a Score
topic: new-score
summary: Making a new score in two steps: the kind of tune, its time signature and tempo, then its name and layout.
draft: true
---

A new score is made in the `Create New Score` window. It asks two things: what kind of tune you are writing, then what to call it and how to lay it out. When you finish, the score opens with its parts and bars already ruled, ready for notes.

## Make a score

1. Choose `File` ▸ `New…`, or press `Cmd+N` on a Mac or `Ctrl+N` on Windows and Linux. The `New` button on the toolbar does the same.
2. Under `What kind of tune?`, choose a tune type.
3. Check the `Time Signature` and `Tempo`, and change them if you need to.
4. Choose `Next`.
5. Type a `Title`. Fill in `Author` and `Band` if you want them.
6. Check `Orientation`, `Parts` and the anacrusis.
7. Choose `Create Score`.

The score opens in a new tab. It has no file yet, so save it when you are ready. See [Files and Older Scores](topic:files).

`Cancel`, or the `Esc` key, closes the window at either step without making anything. `Back` returns from the second step to the first.

<!-- screenshot: the Create New Score window, step 1, with the tune type tiles and the time signature pictures -->

## Step 1: the kind of tune

### Tune type

There are eight tune types. Click one, or move between them with the arrow keys. Double-clicking a tile chooses it and goes straight to step 2.

Some tune types set a starting time signature or tempo. Both can be changed straight away. A type that sets nothing leaves what was there.

| Tune type | Time signature it sets | Tempo it sets |
|---|---|---|
| `March` | none | 78 |
| `Strathspey` | 4/4 | 116 |
| `Reel` | 2/2 | 78 |
| `Hornpipe` | none | 82 |
| `Jig` | 6/8 | 120 |
| `Slow Air` | none | 64 |
| `Waltz` | none | none |
| `Fanfare` | none | none |

The window opens on `March`, in 2/4, at 78.

The tune type also decides how long a part is. A march in 4/4, 3/4 or 12/8 has four bars to a part. Everything else has eight.

### Time signature

Nine time signatures are shown as pictures: 2/4, 6/8, 4/4, 12/8, 3/4, 9/8, 2/2, the common time symbol and the cut common time symbol. Click the one you want.

For anything else, choose `Other time signatures`. You then get:

- two number boxes, the upper from 2 to 28 and the lower 2, 4 or 8;
- `Irregular Grouping`, with boxes for the groups. Typing 2 and 3 over 8 gives a 5/8 bar grouped 2+3;
- `Display using Common symbol` in 4/4, or `Display using Cut-Common symbol` in 2/2.

`Back to typical time signatures` returns to the nine pictures. An irregular grouping is dropped when you go back.

<!-- screenshot: the time signature row after choosing Other time signatures, showing an irregular grouping -->

### Tempo

Type the tempo in beats per minute. The note beside it shows what one beat is: a dotted crotchet in 6/8, for example. With an irregular grouping there is no single beat to count, so you type the number against the note shown.

### If the pictures are hard to read

The tune types and time signatures can be shown as drop-down lists with text instead of tiles and pictures. The time signature is then two lists, `Upper` and `Lower`. Set this in [Settings](topic:settings), under `Appearance`, with `Choose time signatures with`.

## Step 2: the score

The heading shows the tune type you chose, such as `New March`.

<!-- screenshot: the Create New Score window, step 2, with Advanced options closed -->

| Choice | What it sets |
|---|---|
| `Title` | The name of the tune. The box starts with the word "Title" selected, so type over it. |
| `Author` | Who wrote the score. |
| `Band` | The band the score is for. |
| `Orientation` | `Portrait` or `Landscape` paper. |
| `Parts` | How many parts to rule. It starts at 4. |
| `Anacrusis, % of a line` | Room for a pickup, as a percentage of the line's width. Leave it empty for no anacrusis. |

The paper size is not asked for. It comes from `New Score Defaults` in [Settings](topic:settings).

### Advanced options

Choose `Advanced options` to see the rest. The window keeps its size and scrolls down to show them.

| Choice | What it sets |
|---|---|
| `Repeat dots on each part` | Ticked, each part is written once with repeat dots. Unticked, each part is written out in full, at twice the number of bars. A strathspey or reel is not doubled. |
| `Bars per line` | How many bars go on each line. It starts at 4. |
| `General layout` | `DrumScoreEditor` or `Standard`. In `DrumScoreEditor` the time signature sits in an area of its own, apart from the music, and there is no clef. |
| `Clef` | `None`, `Unpitched`, `Treble` or `Bass`. `Standard` layout only. |
| `Clef on every line` | Draws the clef at the start of every line. `Standard` layout only, and not available when `Clef` is `None`. |
| `Inline Time Signature` | Draws the time signature on the first line of music instead of in an area of its own. `Standard` layout only. |
| `Header design` | Which of your saved header designs the score starts with. |
| `Footer design` | Which of your saved footer designs the score starts with. |

<!-- screenshot: step 2 with Advanced options open -->

`Header design` and `Footer design` only appear once you have saved a design. A header design is saved for one layout, so the list changes with `General layout`, and the row disappears if you have none for that layout. Choose `Built-in` for the plain header or footer.

To save a design, right-click the header or footer of a score you have arranged and choose `Save Header as Template` or `Save Footer as Design`. See [Text and Headers](topic:text-and-headers).

## Where the starting values come from

In the Studio Edition, the window opens with your own defaults. `Author`, `Band`, `Orientation`, the anacrusis, `Repeat dots on each part`, `General layout` and `Clef` all start as `New Score Defaults` in [Settings](topic:settings) has them. What you choose in the window is used for this score only. It does not change your defaults.

In the Community Edition, the window opens with fixed starting values, and `Author` and `Band` start empty.

## After the score is made

The score is ruled with the parts, bars per line and repeats you asked for. If the lines do not fit on one page, it runs on to as many pages as it needs.

Your choices are written into the score. Changing `New Score Defaults` later does not change a score you have already made.

To look at them afterwards, choose `File` ▸ `Score Properties…`, or the `Properties` button on the toolbar. See [Score Properties](topic:score-properties). Three choices are fixed once the score is made. They are shown there but cannot be changed: the general layout, `Inline Time Signature` and the anacrusis.
