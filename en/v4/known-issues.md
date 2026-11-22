---
title: Known Issues
topic: known-issues
summary: Faults found in version 4 since it was released, what to do about each, and the version that fixes it.
---

This page lists faults found in version 4 since it was released. Each entry says what goes wrong, who it affects, what to do in the meantime, and which version fixes it.

To see which version you have, open the About box. On Windows and Linux choose `Help` ▸ `About Drum Score Editor`. On a Mac it is in the application menu.

## In version 4.0.0

### Notes cannot be typed in an anacrusis added to a DrumScoreEditor layout score

**What happens.** You make a score with `General layout` set to `DrumScoreEditor` and the anacrusis left empty. Later you right-click a part and tick `Part` ▸ `Anacrusis`. Room appears before the part's opening barline, but notes typed there do not appear.

**Who it affects.** Scores in the DrumScoreEditor layout that were made with no anacrusis. Scores in the Standard layout are not affected. Nor is a DrumScoreEditor layout score whose anacrusis was set when it was made.

**What to do.**

- For a new score, set the anacrusis when you make it. In the New Score window, type a figure in `Anacrusis, % of a line`; 5 is the usual one. See [Starting a Score](topic:new-score).
- Or make the score in the Standard layout. There `Part` ▸ `Anacrusis` adds a short bar after the opening barline, and notes go into it. See [Layout and Spacing](topic:layout).
- For a score that already has music in it, there is no way round this in 4.0.0. The general layout is fixed once a score is made.

**Fixed in.** Version 4.0.1.
