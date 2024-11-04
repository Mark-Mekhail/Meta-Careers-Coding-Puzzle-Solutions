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

### High-Level Solution

#### getMaxCollectableCoins(R, C, G)

*Top level function for the problem.*

Go through all rows in the grid in order from top to bottom. When processing each row, find the maximum number of coins that can be collected before either moving down a row or ending on the row (traveling forever on the row). Use these values to update ```max_ending_row_coint_count``` and ```running_coint_count```, which store the maximum number of coins that can be collected after getting stuck at or passing the given row, respectively. Stop after the last row or a row full of ">" characters is reached and return the maximum of ```max_ending_row_coint_count``` and ```running_coint_count```.

### Key Insights and Optimizations

- Moving down to a new row you will end doing one of the following:
    - Passing through a single ".", "v" and continuing downwards without picking up a coin.
    - Passing through a cell that contains a coin, picking up the coin, and continuing downwards.
    - Reaching a ">" cell and continuing rightwards, picking up any coins that appear along the way before reaching a "v" cell and continuing downwards or staying on the row forever if no "v" cell exists in the row. 
- The maximum number of coins that can be collected up to a given row is equal to the maximum number of coins that could be collected up to the previous row without getting stuck at that row plus the maximum number of coins that can be collected at that row if dropped at any given cell.