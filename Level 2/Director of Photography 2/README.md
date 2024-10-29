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

## Approach

### High-Level Solution

1. Start by populating two lists $P\text{s}$ and $B\text{s}$ which store at each index $i$ the total number of occurences of the letter "P" and "B", respectively, in the first $i$ letters of $C$.

2. Using $P\text{s}$ and $B\text{s}$, populate two new lists $AP\text{s}$ and $AB\text{s}$ that store, at each index $i$, the total number of distinct pairs of actors followed by a photographer and backdrop, respectively, within $X$ and $Y$ cells (from the definition of *artistic*) of the actor where the actor is in a cell $j \leq i$. 

3. Finally, for each cell in $C$, count the number of distinct artistic configurations possible such that the current cell holds the photographer/actor with the lowest index in the configuration. Add this count to a running total.

### Key Insights and Optimizations

- Using $P\text{s}$, we can easily populate $AP\text{s}$ by observing that the number of distinct *artistic* configurations of actors followed by photographers with the actor at cell $i$, which we can call $AP_i$, is simply the number of photographers in cells $(i + X)$...$(i + Y)$ (which can easily be calculated using $P\text{s}$ ) if cell $i$ contains an actor and $0$ otherwise. The cumulative number of such configurations up to cell $i$ is therefore $AP\text{s}[i-1]$ + $AP_i$. The same logic follows for $AB\text{s}$.
- Step 3 of the high-level solution is easy to complete using $AP\text{s}$ and $AB\text{s}$. All you need to do is check what the cell contains and use the relevant list (if any) to compute the number of *artistic* configurations of actors and photographers/backdrops follow the current cell.