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

$G_{i,j} \in \{$ ".", "S", "E", "\#", "a"..."z" $\}$

## Approach

### High-Level Solution

#### getSecondsRequired(R, C, G)

Top level function for the problem.

1. Initialize a variable ```portal_cells``` to an empty map.
2. Go through all cells $G_{i,j}$ in $G$. If $G_{i,j}=$ "S", store $(i,j)$ in a variable ```start_cell```. Otherwise, if $G_{i,j}$ contains a lowercase letter $x$, add $(i,j)$ to the set mapped to by $x$ in ```portal_cells```.
3. Initialize a variable ```seconds``` to 1.
4. Perform a breadth-first search (BFS) of $G$ starting at cell ```start_cell```, where each cell $G_{i,j}$ is a node in the graph and an edge exists between every pair of cells that are one second away from each other (i.e. adjacent non-wall cells and portal cells with the same letter). Begin each search iteration (i.e. finding neighbours of all new cells found in the last step) by incrementing ```seconds```. Once an exit cell is reached, return ```seconds```.
5. If the bfs completes without the function returning, no exit can be reached. Return $-1$.

### Key Insights and Optimizations

- For this problem, the grid $G$ can be thought of as a graph, where each cell in $G$ is a node and an edge exists between every pair of cells that are one second away from each other (i.e. adjacent non-wall cells and portal cells with the same letter). This reduces the problem to a shortest-path problem, where we're trying to find the shortest path between the starting cell node and any exit cell node. As we know, BFS is an algorithm that can help us out with this!