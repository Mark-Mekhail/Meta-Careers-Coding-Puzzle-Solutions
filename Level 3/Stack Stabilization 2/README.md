# Stack Stabilization (Chapter 2)

## Problem Description

There's a stack of $N$ inflatable discs, with the $i\text{th}$ disc from the top having an initial radius of $R_i$ inches.

The stack is considered *unstable* if it includes at least one disc whose radius is larger than or equal to that of the disc directly under it. In other words, for the stack to be *stable*, each disc must have a strictly smaller radius than that of the disc directly under it.

As long as the stack is unstable, you can repeatedly choose a disc and perform one of the following operations:
- Inflate the disc, increasing its radius by $1$ inch. This operation takes $A$ seconds and may be performed on discs of any radius (even those that exceed $10^9$ inches).
- Deflate the disc, decreasing its radius by $1$ inch. This operation takes $B$ seconds and may only be performed if the resulting radius is a positive integer number of inches (that is, if the disc has a radius of at least $2"$ before being deflated).

Determine the minimum number of seconds needed in order to make the stack stable.

## Constraints

$1 \leq N \leq 50$

$1 \leq R_i \leq 1{\small,}000{\small,}000{\small,}000$

$1 \leq A, B \leq 100$

## Solution

### Function Descriptions and Implementation Approaches

#### getMinimumSecondsRequired(N, R, A, B)

*Top level function for the problem.*

Go through all discs $1 \leq i \leq N$ in the stack in order (from top to bottom). For disc $i$, if $R_i > R_{i-1}$, there is no need to do anything because the stack is already stable up to $i$. Otherwise, inflate disc $i$ such that $R_i = R_{i-1} + 1$ and then proceed to deflate disc $i$ and any discs preceding it that would need to be deflated for the stack to remain stable with the deflated size of disc $i$ as long as this results in a net cost saving for the entire disc configuration up to disc $i$. Finally, return the cost of the inflations/deflations needed to update the disc radii to those of the optimal configuration found after completing the aforementioned process.

### Key Insights and Optimizations

- Let's define a chain interval to be a contiguous interval of discs where each disc in the interval has a radius that is within $1$ of other discs in the interval that are adjacent to it. Assuming a stable configuration of discs from disc $0$ (the top disc) down to a disc $i$ where $R_i = R_{i-1} + 1$, deflating disc $i$ by $1$ will only require deflating all discs in the chain interval of discs up to and including disc $i$ that disc $i$ is a part of. 
    - The amount we can deflate the discs in the chain interval of the $i\text{th}$ disc at the same cost/savings per deflation is the minimum of the amount any disc in the chain interval has been inflated and one less than the difference in the radius of the first disc in the current chain interval and the disc above it (if applicable).