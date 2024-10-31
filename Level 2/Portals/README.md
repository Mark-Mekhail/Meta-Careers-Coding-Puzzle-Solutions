# Portals

## Problem Description

You've found yourself in a grid of cells with $R$ rows and $C$ columns. The cell in the $i\text{th}$ row from the top and $j\text{th}$ column from the left contains one of the following (indicated by the character $G_{i,j}$):
- If $G_{i,j} =$ ".", the cell is empty.
- If $G_{i,j} =$ "S", the cell contains your starting position. There is exactly one such cell.
- If $G_{i,j} =$ "E", the cell contains an exit. There is at least one such cell.
- If $G_{i,j} =$ "#", the cell contains a wall.
- Otherwise, if $G_{i,j}$ is a lowercase letter (between "a" and "z", inclusive), the cell contains a portal marked with that letter.

Your objective is to reach any exit from your starting position as quickly as possible. Each second, you may take either of the following actions:
- Walk to a cell adjacent to your current one (directly above, below, to the left, or to the right), as long as you remain within the grid and that cell does not contain a wall.
- If your current cell contains a portal, teleport to any other cell in the grid containing a portal marked with the same letter as your current cell's portal.

Determine the minimum number of seconds required to reach any exit, if it's possible to do so at all. If it's not possible, return $-1$ instead.

## Constraints

$1 \leq R,C \leq 50$

$G_{i,j} \in \{$".", "S", "E", "\#", "a"..."z" $\}$

## Approach

TODO