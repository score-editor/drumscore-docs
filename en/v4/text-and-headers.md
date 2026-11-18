---
title: Text and Headers
topic: text-and-headers
summary: Tune headers and the page footer, text and pictures, text tags on the music, watermarks, saved designs, and page, line and part numbers.
---

Everything on a page that is not music is covered here: the header over each tune, the footer at the foot of each page, words written on the music, pictures, the watermark and the numbering.

Each tune carries its own header where it begins. As a new score is made, the header shows the tune's title in the middle, its tune type at the left and its author at the right. The footer shows the band at the left and the date the score was last changed at the right.

Arranging headers and footers, pictures and watermarks need the Studio Edition. See *Community Edition* at the end of this page.

## Change what the header says

1. Choose `File` ▸ `Score Properties…` and go to `Tunes`.
2. Select the tune, and change its `Title`, `Tune Type` or `Author`.
3. For the band's name, go to `Score`. In the `Score` pane, change `Band`.
4. Choose `OK`.

The header and footer change to match. In the Studio Edition you can also type straight on the page. See *Type into a piece of text* below.

## Move things around in the header

1. Double-click the header. Resting the pointer on it shows `Double-click to edit the Tune Header`.
2. Click a piece of text or a picture. It shows an outline with eight handles.
3. Drag it to move it, or drag a handle to resize it.
4. Click in the music, or press `Esc`, when you have finished.

The footer works the same way: double-click it. Either way in, every tune's header and the footer can all be arranged until you leave.

![A tune header being arranged: the header outlined, the title selected and showing its handles](images/v4/header-being-arranged.png){: width="898" }

## Arranging a header or footer

A score has one header design. What you do to one tune's header is done to every tune's header: a piece you move, add or delete is moved, added or deleted in them all.

| To | Do this |
|---|---|
| Move a piece | Drag it. It snaps to the margins, to the edges and centre of the header, to the top of the music, and to the edges and centres of the other pieces. Hold `Alt` (`Option` on a Mac) to drag without snapping. |
| Move it a little | Nudge it with the keys below. |
| Resize a piece | Drag one of its handles. |
| Make the header deeper | Drag the header's bottom edge. The music moves down to make room. For the footer, drag its top edge. |
| Add words | Right-click an empty place in the header or footer and choose `Add Text`. A piece saying `New Text` appears there. |
| Add a picture | Right-click an empty place and choose `Add Image`. |
| Delete a piece | Select it and press `Delete` or `Backspace`, or right-click it and choose `Delete`. |

| | Nudge a selected piece |
|---|---|
| Mac | `Option+Shift` with an arrow key |
| Windows | `Ctrl+Shift` with an arrow key |
| Linux | `Alt+Shift` with an arrow key |

Text stays inside its header or footer, and a piece inside the margins cannot be dragged out past them. A picture may hang below the header, over the music.

Each drag, nudge, addition and deletion is one step for `Edit` ▸ `Undo`.

### The right-click menus

Right-clicking **a piece** offers:

- `Text`, for a piece of text. See *Format text* below.
- `Anchor`, with `Across` and `Down`. `Across` holds the piece to the `Left edge`, `Centred` or the `Right edge` of the header. `Down` holds it to the `Top of header` or the `Bottom of header`. `Nearest edge` leaves the choice to where the piece sits, and names the edge it is using. The anchor matters when a header is a different width, as on a landscape tune: the piece keeps its distance from the edge it is anchored to.
- `Delete`.

Right-clicking **an empty place** in a header or footer offers `Add Text` and `Add Image`, then `Save Header as Template` and `Reset Header to Design`. In the footer the last two read `Save Footer as Design` and `Reset Footer to Design`. See *Saved designs* below.

## Text

### Type into a piece of text

While arranging, double-click the text. Its words are selected, ready to type over. Press `Enter`, or click elsewhere, to keep what you typed. Press `Esc` to abandon it. Double-click inside the words to select one word, and click three times to select them all.

The title, tune type and author in a header are not fixed words. Each shows what `Score Properties…` holds, and typing over one changes the tune itself. In a score of one tune, typing a new title renames the score as well. The band and the date in the footer cannot be typed over: change `Band` in `Score Properties…`.

Your own text can print these facts too. Type one of these names among the words:

| Type | It prints |
|---|---|
| `%title`, `%tunetype`, `%author`, `%bpm` | The tune's title, tune type, author and tempo |
| `%band`, `%version` | The `Band` and `Version` from the `Score` pane |
| `%filename` | The `Filename` from the `Score` pane |
| `%updated` | The date the score was last changed |

So `%bpm bpm` prints the tempo followed by "bpm".

### Format text

Right-click a piece of text and open `Text`.

| `Text` ▸ | What it does |
|---|---|
| `Bold`, `Italic`, `Underline` | Ticked when on. If you are typing in text of your own and have some of its words selected, only those words change. |
| `Point Size` | Sizes from 8 to 72. |
| `Alignment` | `Left`, `Centre` or `Right` within the piece's own box. |
| `Sans Serif`, `Serif`, `Choose Font…` | The font. `Choose Font…` offers every font on your computer, with its style and size. |
| `Colour` | `Page Ink` for the ordinary colour, or `Choose…` for any other. |

While a piece of text is selected or being typed in, the editing toolbar is replaced by a text toolbar with the same choices, and `Larger` and `Smaller` buttons. The size box there takes any figure you type.

![The text toolbar, in place of the editing toolbar, while the title is being typed](images/v4/text-toolbar.png){: width="900" }

### The score's own font

The `Score` pane of `File` ▸ `Score Properties…` has a `Text` group with `Font`, `Choose…` and `Font Size`. This font is used for line numbers, page numbers, instrument names and the stroke counts on rolls, and it is the font a new piece from `Add Text` starts in. It does not restyle text already on the page.

## Text on the music

A text tag is a few words attached to a note or a barline.

1. Select the note or the barline. To select a barline, tick `Edit` ▸ `Select Bar Lines` first.
2. Press `Ctrl+T`. This is the Control key on a Mac too. Or right-click the selection and choose `Note` ▸ `Text Tag`, or `Bar Line` ▸ `Text Tag` for a barline.
3. The tag appears saying `New Text Comment`. Double-click it and type your own words.

Right-click the tag for the same `Text` menu, without `Colour` and with `Position` ▸ `Above` or `Below` to put it over or under the line. While typing in a tag, `Alt+Up` and `Alt+Down` (`Option` on a Mac) do the same.

To remove a tag, select its note or barline and press `Ctrl+T` again. `Text Tag` on the menu is ticked while the selection has one.

![A text tag reading 2nd time above a note, open for typing](images/v4/text-tag.png){: width="372" }

## Pictures

`Add Image` takes a PNG, JPEG, GIF or BMP file. The picture is fitted to the header where you right-clicked, and you can then drag and resize it like any other piece.

A picture is normally saved inside the score file. If you tick `Keep score images in the library, not inside the score file`, in `Settings` ▸ `Libraries` ▸ `Images`, a score refers to its pictures in your library folder instead. The file is smaller, but it opens without its pictures on a computer that does not have them. To send such a score to somebody, use `File` ▸ `Export` ▸ `Export as Portable .ds…`, which puts the pictures back in. That command is shown only while the box is ticked. The folder itself is set in `Settings` ▸ `Libraries` ▸ `Location`.

## Watermark

A watermark is faint words or a faint picture behind the music on every page. It is set in the `Watermark` pane of `File` ▸ `Score Properties…`.

| Setting | What it does |
|---|---|
| `Watermark` | `None`, `Text` or `Image`. `Image` is offered once your library holds a watermark picture. |
| `% Weight of watermark` | How strongly it prints. |
| `Watermark Text`, `Font Size` | The words and their size. They are written along the page's diagonal. |
| `Library:` | Which of your watermark pictures to use. It is drawn in the middle of the page. |

Watermark pictures are kept in `Settings` ▸ `Libraries` ▸ `Watermarks`, from PNG or JPEG files. The watermark that new scores start with is under `Settings` ▸ `New Score Defaults` ▸ `Watermark`.

## Saved designs

When a header or footer is as you want it, keep it for other scores. While arranging, right-click an empty place in it and choose `Save Header as Template` or `Save Footer as Design`, and give the design a name. Its pictures are stored in your library folder with it.

- A header design is saved for the general layout of the score it came from. A footer design suits either layout.
- The first design you save becomes the one new scores are made with. After that, choose under `Settings` ▸ `New Score Defaults` ▸ `Score`, in `Headers and footers`. `Built-in` is the plain header or footer.
- One score can be given a different design as it is made. See [Starting a Score](topic:new-score).
- `Reset Header to Design` and `Reset Footer to Design` put the design that new scores are made with back onto this score. This is one step to undo.

Saving a header again under a name you have already used replaces that name's header for that layout. One name can hold a header for each layout.

## Text and pictures on the page itself

Outside the header and footer, text and pictures can be placed only on a page arranged by hand. See [Layout and Spacing](topic:layout). On such a page, right-click empty paper and choose `Add Text` or `Add Image`. The piece can be dragged and resized at any time. Right-clicking it offers `Delete`, and `Text` for a piece of text.

## Numbering

The `Numbering` group is in the `Score` pane of `File` ▸ `Score Properties…`. Numbering is part of the Studio Edition.

| Tick | What it prints |
|---|---|
| `Pages` | The page number at the foot of each page, in the middle, written like `- 1 -`. |
| `Lines` | A number at the left of each staff line, counted down the whole score. |
| `Parts` | Each part's number, in a box, at the left of the part's first line. The count starts again at one for each tune. |

![Score Properties, Score pane: the Identity, Numbering, Text and File groups](images/v4/score-properties-score.png){: width="700" }

![Part numbers in boxes above the line numbers, at the first line of each part](images/v4/part-numbers.png){: width="315" }

## Community Edition

In the Community Edition the header and footer show the built-in design, and their words are changed in `Score Properties…`. Text tags work as described above. These need the Studio Edition:

- arranging a header or footer, and `Add Text` and `Add Image`;
- pictures, which are not shown or printed;
- the `Watermark` pane. Every page instead carries a faint `Drumscore.scot Free Edition` mark;
- `Settings` beyond the `Licence` pane, and so the libraries and `New Score Defaults`.

See [Licensing](topic:licensing).
