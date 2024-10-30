# Stack Stabilization (Chapter 1)

## Problem Description

*Note: [Chapter 2](../../Level%203/Stack%20Stabilization%202/) is a harder version of this puzzle.*

There's a stack of $N$ inflatable discs, with the $i\text{th}$ disc from the top having an initial radius of $R_i$ inches.

The stack is considered *unstable* if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be *stable*, each disc must have a strictly smaller radius than that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose any disc of your choice and deflate it down to have a radius of your choice which is strictly smaller than the disc’s prior radius. The new radius must be a positive integer number of inches.

Determine the minimum number of discs which need to be deflated in order to make the stack stable, if this is possible at all. If it is impossible to stabilize the stack, return $-1$ instead.

## Constraints

$1 \leq N \leq 50$

$1 \leq R_i \leq 1{\small,}000{\small,}000{\small,}000$

## Approach

### High-Level Solution

1. Initialize a variable ```deflation_count``` to $0$.
2. Go through each disc radius $R_i$ in $R$ in reverse order (i.e. from bottom to top). If $R_i$ is not smaller than $R_{i+1}$, set $R_i = R_{i+1} - 1$ and increment ```deflation_count```.
3. Return ```deflation_count```.

### Key Insights and Optimizations

- Assuming the stack is stable below a disc $i$, disc $i$ will need to be deflated if and only if the disc below it is larger or equal in size to it. 