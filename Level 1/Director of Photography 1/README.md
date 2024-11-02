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

*Top level function for the problem.*

Go through all positions $i$ from $0$ to the last possible start position for an artistic photograph and count the number of artistic photos that can be created where the first character in the photograph configuration is at $i$.

#### getArtisticPhotographsFromStartPos(N, C, X, Y, i)

*Given a starting cell $i$, counts the number of distinct *artistic photographs* that can be taken where cell $C_i$ is part of the photograph and all other cells $C_j$ in the photograph come after $C_i$ (i.e. $j > i$).*

Check the character at the starting cell. If the cell contains a photographer or backdrop, look for actors in the interval [$i+X$, $i+Y]. For every cell $j$ in this interval that contains an actor, count the number of occurences of the last character needed for an artistic photograph in the cells in the interval [$j+X$, $j+Y]. Return the total count of these last occurences.

#### countCharacterOccurenceInInterval(N, C, char, start, end)

*Counts the number of occurences of a given character ```char``` in $C$ in the interval [```start```, ```end```).*

Implementation is straightforward.

### Key Insights and Optimizations

- A given cell can only be used as the lowest-index cell for a photograph if it contains a photographer or a backdrop. The number of *artistic photographs* with that starting cell is simply the sum of the number of photographs that can be taken with an actor within $X$ and $Y$ cells of the starting cell, which is in turn the number of cells with the last remaining character within $X$ and $Y$ cells of the actor.