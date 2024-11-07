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

$G_{i,j} \in \\{$ ".", "S", "E", "\#", "a"..."z" $\\}$

## Solution

### Function Descriptions and Implementation Approaches

#### getSecondsRequired(R, C, G)

*Top level function for the problem.*

Go through all cells in $G$ to find the starting cell position and to populate a map that maps each portal character to all positions containing that portal. Using this information, call **getExitDistance** to find the amount of time needed to get from the starting cell to an exit.

#### getExitDistance(R, C, G, portals, startCells, visitedCells)

*Performs a breadth-first search (BFS) on the grid, starting from startCells, where adjacent cells and cells with the same portal are considered to have edges between them. The number of BFS iterations needed to find an exit, or -1 if no exit is found, is returned.*

Fairly standard BFS-like algorithm with graph equivalencies as mentioned above. On each recursive call of the function, if ```startCells``` is empty then return $-1$ because no exit could be reached. Otherwise, find all unvisited neighbors of cells in ```startCells```. If an exit is a neighbor, return 0. Otherwise, recursively call the function on the set of unvisited neighbours found and use the return value of this call to return an appropriate value.

### Key Insights and Optimizations

- For this problem, the grid $G$ can be thought of as a graph, where each cell in $G$ is a node and an edge exists between every pair of cells that are one second away from each other (i.e. adjacent non-wall cells and portal cells with the same letter). This reduces the problem to a shortest-path problem, where we're trying to find the shortest path between the starting cell node and any exit cell node. As we know, BFS is an algorithm that can help us out with this!