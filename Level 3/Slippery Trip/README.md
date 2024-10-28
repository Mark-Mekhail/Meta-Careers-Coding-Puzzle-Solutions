# Slippery Trip

## Problem Description

There's a grid of cells with $R$ rows (numbered from $1$ to $R$ from top to bottom) and $C$ columns (numbered from $1$ to $C$ from left to right). The grid wraps around horizontally, meaning that column $1$ is just to the right of column $C$ (and column $C$ is just to the left of column $1$).

The cell in row $i$ and column $j$ initially contains one of the following (indicated by the character $G_{i,j}$):
- If $G_{i,j}$ = "$.$", the cell is empty.
- If $G_{i,j}$ = "$*$", the cell contains a coin.
- If $G_{i,j}$ = ">", the cell contains an arrow pointing right.
- If $G_{i,j}$ = "v", the cell contains an arrow pointing down.

You may cyclically shift each row to the right as many times as you'd like (including not at all). Each such shift causes each of the row's cells to move $1$ column to the right, with its rightmost cell (in column $C$) wrapping around and moving to column $1$.

After you've finished rotating the rows to your liking, you'll take a trip through the grid, starting by entering the cell at the top-left corner (in row $1$ and column $1$) downward from above the grid. Upon entering a cell, if it contains a coin that you haven't yet collected, you'll collect it. If it contains an arrow, your direction of travel will change to that of the arrow (either right or down). Either way, you'll then proceed to the next adjacent cell in your direction of travel. If you move rightward from column $C$, you'll wrap around to column $1$ in the same row, and if you move downward from row $R$, you'll end your trip. Note that you may only collect each cell's coin at most once, that your trip might last forever, and that once you begin your trip you cannot shift the grid's rows further.

Determine the maximum number of coins you can collect on your trip.

## Constraints

$2 \leq R,C \leq 400{\small,}000$

$R*C \leq 800{\small,}000$

$G_{i,j} \in \{\text{".", "*", ">", "v"}\}$

## Approach

TODO