# Director of Photography 1

## Problem Description

*Note: [Chapter 2](../../Level%202/Director%20of%20Photography%202/) is a harder version of this puzzle. The only difference is a larger constraint on $N$.*

A photography set consists of $N$ cells in a row, numbered from $1$ to $N$ in order, and can be represented by a string $C$ of length $N$. Each cell $i$ is one of the following types (indicated by $C_i$, the $i\text{th}$ character of $C$):
- If $C_i = \text{"P"}$, it is allowed to contain a photographer
- If $C_i = \text{"A"}$, it is allowed to contain an actor
- If $C_i = \text{"B"}$, it is allowed to contain a backdrop
- If $C_i = \text{"."}$, it must be left empty

A *photograph* consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered *artistic* if the distance between the photographer and the actor is between $X$ and $Y$ cells (inclusive), and the distance between the actor and the backdrop is also between $X$ and $Y$ cells (inclusive). The distance between cells $i$ and $j$ is $|i-j|$  (the absolute value of the difference between their indices).

Determine the number of different *artistic photographs* which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.

## Constraints

$1 \leq N \leq 200$

$1 \leq X \leq Y \leq N$

## Approach

### High-Level Solution

#### getArtisticPhotographCount(N, C, X, Y)

Top level function for the problem.

1. Initialize a variable ```artistic_photo_count``` to $0$.
2. Go through the cells in $C$. For each cell $C_i$, count the number of distinct *artistic photographs* that can be taken where cell $C_i$ is part of the photograph and all other cells $C_j$ in the photograph come after $C_i$ (i.e. $j > i$). Add this number to ```artistic_photo_count```.
    1. The number of *artistic photographs* including cell $C_i$ and only cells after it can easily be computed by a brute force search. If $C_i$ contains a photographer or backdrop, one can look at cells $C_j$ where $i+X \leq j \leq i+Y$ and then for each cell $C_j$ that contains an actor count the number of cells $C_k$ where $j + X \leq K \leq j + Y$ such that $\{C_i, C_j, C_K\}$ make up an *artistic photograph*.
3. Return ```artistic_photo_count```.

### Key Insights and Optimizations

- A given cell can only be used as the lowest-index cell for a photograph if it contains a photographer or a backdrop. The number of *artistic photographs* with that starting cell is simply the sum of the number of photographs that can be taken with an actor within $X$ and $Y$ cells of the starting cell, which is in turn the number of cells with the last remaining character within $X$ and $Y$ cells of the actor.