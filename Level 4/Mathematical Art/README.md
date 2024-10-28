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

1. Track and store all strokes, combining any strokes aligned on the same axis that overlap
2. Sort horizontal strokes by the x-coordinate of the leftmost point of the stroke
3. Map each x-coordinate containing a vertical stroke to a list of vertical strokes at that x position
4. Go through all vertical strokes and count the number of distinct horizontal strokes that pass through each stroke, adding this count to a total sum of crosses.

### Key Insights and Optimizations

- We can simplify the problem and avoid double-counting by "combining" overlapping strokes aligned along the same direction and same fixed coordinate. For example, if one stroke goes up from (0,0) to (0, 5) and another stroke goes down from (0, 1) to (0, -4), we can "combine" the strokes into one strokes that spans (0,5) to (0,-4)
- If we have two lists of merged horizontal strokes, one sorted by leftmost endpoint and another sorted by rightmost endpoint, we can determine the horizontal strokes that pass through a given x-coordinate by finding the intersection of the elements that start before the x-coordinate and end after the x-coordinate. If we search for this intersection continuously over strictly increasing x-coordinates, at most a single linear pass over both lists is required.