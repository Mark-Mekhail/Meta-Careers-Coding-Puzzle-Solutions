# Stack Stabilization (Chapter 2)

## Problem Description

There's a stack of $N$ inflatable discs, with the $i\text{th}$ disc from the top having an initial radius of $R_i$ inches.

The stack is considered *unstable* if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be *stable*, each disc must have a strictly smaller radius than that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose a disc and perform one of the following operations:
- Inflate the disc, increasing its radius by $1$ inch. This operation takes $A$ seconds and may be performed on discs of any radius (even those that exceed $10^9$ inches).
- Deflate the disc, decreasing its radius by $1$ inch. This operation takes $B$ seconds and may only be performed if the resulting radius is a positive integer number of inches (that is, if the disc has a radius of at least $2"$ before being deflated).

Determine the minimum number of seconds needed in order to make the stack stable.

## Constraints

$1 \leq N \leq 50 \\\\\n 1 \leq R_i \leq 1{\small,}000{\small,}000{\small,}000 \\\\\n 1 \leq A, B \leq 100$

## Approach

TODO