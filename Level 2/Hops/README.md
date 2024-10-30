# Hops

## Problem Description

A family of frogs in a pond are traveling towards dry land to hibernate. They hope to do so by hopping across a trail of $N$ lily pads, numbered from $1$ to $N$ in order.

There are $F$ frogs, numbered from $1$ to $F$. Frog $i$ is currently perched atop lily pad $P_i$. No two frogs are currently on the same lily pad. Lily pad $N$ is right next to the shore, and none of the frogs are initially on lily pad $N$.

Each second, one frog may hop along the trail towards lily pad $N$. When a frog hops, it moves to the nearest lily pad after its current lily pad which is not currently occupied by another frog (hopping over any other frogs on intermediate lily pads along the way). If this causes it to reach lily pad $N$, it will immediately exit onto the shore. Multiple frogs may not simultaneously hop during the same second.

Assuming the frogs work together optimally when deciding which frog should hop during each second, determine the minimum number of seconds required for all $F$ of them to reach the shore.

## Constraints

$1 \leq N \leq 10^{12}$

$1 \leq F \leq 500{\small,}000$

$1 \leq P_i \leq N - 1$

## Approach

### High-Level Solution

#### getSecondsRequired(N, F, P)

Top level function for the problem.

1. Sort $P$ in ascending order.
2. Initialize the variable ```seconds``` to 0 and ```first_frog_index``` to $P_0$.
3. Go over the starting positions $P_i$ in $P$ in order. For each position $P_i$, if $P_i$ is greater than ```first_frog_index``` $+ i$, add $P_i -$ ```first_frog_index``` to ```seconds``` and set ```first_frog_index``` $= P_i$.
4. Add $N-$ ```first_frog_index``` to ```seconds```.
5. Return ```seconds```.

### Key Insights and Optimizations

- If the frogs cooperate well, they can minimize the number of hops required by always letting the first (i.e. lowest-index) frog hop until all frogs have reached the shore. With this insight for deciding which frog should hop next at a given moment, we can observe that after a frog is hopped over for the first time, it will become the first frog in a chain of all frogs that started on an earlier lily pad, with all frogs in the chain pertching atop successive lily pads.
- The number of hops that it takes for all frogs in a chain starting at a position $j$ to hop over a frog at a position $P_i$ ahead of the chain can be observed to be $P_i - j$.
- Once all frogs are in a chain with the first frog in the chain being pertched atop lily pad $j$, it will take $N - j$ hops for all frogs in the chain to reach the shore.