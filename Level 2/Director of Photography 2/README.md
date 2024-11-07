# Director of Photography (Chapter 2)

## Problem Description

*Note: [Chapter 1](../../Level%201/Director%20of%20Photography%201/) is an easier version of this puzzle. The only difference is a smaller constraint on $N$.*

A photography set consists of $N$ cells in a row, numbered from $1$ to $N$ in order, and can be represented by a string $C$ of length $N$. Each cell $i$ is one of the following types (indicated by $C_i$, the $i\text{th}$ character of $C$):
- If $C_i = \text{"P"}$, it is allowed to contain a photographer
- If $C_i = \text{"A"}$, it is allowed to contain an actor
- If $C_i = \text{"B"}$, it is allowed to contain a backdrop
- If $C_i = \text{"."}$, it must be left empty

A *photograph* consists of a photographer, an actor, and a backdrop, such that each of them is placed in a valid cell, and such that the actor is between the photographer and the backdrop. Such a photograph is considered *artistic* if the distance between the photographer and the actor is between $X$ and $Y$ cells (inclusive), and the distance between the actor and the backdrop is also between $X$ and $Y$ cells (inclusive). The distance between cells $i$ and $j$ is $|i-j|$  (the absolute value of the difference between their indices).

Determine the number of different *artistic photographs* which could potentially be taken at the set. Two photographs are considered different if they involve a different photographer cell, actor cell, and/or backdrop cell.

## Constraints

$1 \leq N \leq 300{\small,}000$

$1 \leq X \leq Y \leq N$

## Solution

### Function Descriptions and Implementation Approaches

#### getArtisticPhotographCount(N, C, X, Y)

*Top level function for the problem.*

Go through values of $i$ where $0 \leq i < N$, in order. At each iteration, if $C_i$ contains a photographer or backdrop count the number of artistic photographs that can be created where $C_i$ is the first cell in the photograph. Return the sum of all these counts.

#### getCumulativeArtisticActorCharacterCounts(N, C, X, Y, char)

*Creates a list $L$ of cumulative counts of pairs of actors at indexes $X \leq j \leq i$ followed by a given character specified by ```char``` within $C_{j+X, j+Y}.*

Create a list $L$. Go through values of $i$ where $0 \leq i < N$, in order. At each iteration, set $L_i = L_{i-1}$ and if $C_i =$ "A", add the number of occurences of ```char``` that exist in $C_{i+X...i+Y} to $L_i$. Finally, return $L$.

#### getCumulativeCharCounts(N, C, char)

*Creates a list $L$ of cumulative counts of occurences of ```char``` in $C$, where $L_i$ contains the number of occurences of ```char``` in $C_{0...i}$.*

Implementation is straightforward.

### Key Insights and Optimizations

- An important observation for this solution is that if we have a list $L$ of cumulative counts of a some value in a list $C$, where $L_i$ equals the number of occurences of the value in $C_{0...i}$, the number of occurences of the value in the subinterval $C_{j...k}$ is simply $L_k - L_{j-1}$.