# Mathematical Art

## Problem Description

You are creating a special painting on a canvas which may be represented as a 2D Cartesian plane. You start by placing a thin brush at the origin $(0,0)$ and then make $N$ axis-aligned strokes without lifting the brush off of the canvas. For the $i\text{th}$ stroke, you'll move your brush $L_i$ units from its current position in a direction indicated by the character $D_i$, which is either U (up), D (down), L (left), or R (right), while leaving behind a line segment of paint between the brush's current and new positions. For example, if $L_1=L_5$ and $D_1=L$, you'll draw a stroke between coordinates $(0,0)$ and $(−5,0)$, with your brush ending up at coordinates $(−5,0)$. Note that each stroke is either horizontal or vertical, and that each stroke (after the first) begins where the previous stroke ended.

This painting is being marketed as a work of mathematical art, and its value is based on the number of times a certain mathematical symbol appears in it - specifically, the plus sign. A plus sign is considered to be present at a certain position if and only if, for each of the 4 cardinal directions (up, down, left, and right), there's paint leading from the point in that direction (or, vice versa, leading to that point from that direction). Note that the paint from arbitrarily many strokes of your brush might come together to form any given plus sign, and that at most one plus sign may be considered to exist at any given position.

Determine the number of positions in the painting at which a plus sign is present.

## Constraints

$2 \leq N \leq 2{\small,}000{\small,}000$

$1 \leq L_i \leq 1{\small,}000{\small,}000{\small,}000$

$D_i \in \{\text{U, D, L, R}\}$

## Approach

### High-Level Solution

#### getPlusSignCount(N, L, D)

*Top level function for the problem.*

Use the functions below to construct minimal lists of merged (i.e. non-touching) lines in each orientation (horizontal and vertical) that represent all of the lines painted on the canvas by the time the painting has been completed. Next, go through all merged vertical lines in order. For each vertical line, count the horizontal lines that cross the line. Return the sum of the counts of horizontal lines crossing vertical lines.

#### getStrokeLines(N, L, D)

*Returns lists of horizontal and vertical lines representing all strokes made.*

Go through all strokes in order. Add the line drawn by the stroke to the appropriate list of lines according to its orientation (horizontal or vertical). Return the lists of lines drawn.

#### getStrokeEndpoint(brushPos, strokeLen, strokeDir)

*Given the current brush position, a stroke length, and a stroke direction, returns the updated brush position after completing the stroke.*

Implementation is fairly straightforward.

#### getMergedLines(lines, key)

*Given a sorted (according to natural ordering) list of lines ```lines``` and a key function ```key``` for sorting the output list, returns a list of non-overlapping lines created by merging groups of lines in ```lines``` where every line in the group touches at least one other line in the group.*

Go through the lines in order. For each line, determine whether the last merged line in a running list of merged lines ```mergedLines``` touches the current line. If so, expand the merged line to cover the entirety of the current line. Otherwise, create a new merged line that is equivalent to the current line and add it to ```mergedLines```. Return ```mergedLines```.


### Key Insights and Optimizations

- We can simplify the problem and avoid double-counting crosses by "combining" touching strokes with the same orientation (horizontal or vertical) with the fixed coordinate. For example, if one stroke goes up from (0,0) to (0,5) and another stroke goes down from (0,1) to (0,-4), we can "combine" the strokes into line that spans (0,5) to (0,-4)
- If we have two lists of merged horizontal strokes, one sorted by leftmost endpoint, which we can call ```horizontals_by_start``` and another sorted by rightmost endpoint, which we can call ```horizontals_by_end```, we can determine the horizontal strokes that pass through a given x-coordinate by finding the intersection of the elements that start before the x-coordinate in ```horizontals_by_start``` and end after the x-coordinate in ```horizontals_by_end```. If we search for this intersection continuously over strictly increasing x-coordinates, at most a single linear pass over both lists is required because we will add each line to the list at most once (when the x-coordinate first falls within it) and remove it at most once (when the x-coordinate first falls outside of it).