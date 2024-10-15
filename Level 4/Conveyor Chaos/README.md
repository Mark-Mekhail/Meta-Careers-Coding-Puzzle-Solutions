# Conveyor Chaos

## Problem Description

A distribution center moves packages around using a system of conveyor belts, which can be represented as line segments on the 2D Cartesian plane. The $i\text{th}$ conveyor belt runs from coordinates $(A_i,H_i)$ to $(B_i,H_i)$. No two conveyor belts share any points in common, including endpoints or interior points. Gravity points in the direction of the negative y-axis, meaning that objects normally fall vertically downwards, with their y-coordinate decreasing over time.

Each conveyor belt runs to either the left or the right. A package can be considered to occupy a single point on the plane. If a package lands strictly within conveyor belt $i$ (excluding its endpoints), then it will be transported to its left or right end (either $(A_i,H_i)$ or $(B_i,H_i)$), depending on the conveyor belt's direction, before continuing to fall vertically downwards.

You'll start by selecting a single conveyor belt and choosing a fixed direction (either left or right) for it to run in. Then, random directions will be independently chosen for each of the remaining $N-1$ conveyor belts (each being either left or right with equal probability). Finally, a single package will be dropped into the system from high above, at coordinates $(x,1{\small,}000{\small,}000)$, where $x$ is a real value drawn uniform randomly from the inclusive interval $[0, 1{\small,}000{\small,}000]$. Your objective is to minimize the expected horizontal distance which this package will travel along conveyor belts before hitting the ground (any point with y-coordinate $0$).

For example, consider the following system of conveyor belts (as are present in the second sample case):

![system](images/system.png)

Consider picking the conveyor belt at y-coordinate $5$ and causing it to run to the left. If it then so happens that the bottommost conveyor belt also runs to the left while the other three run to the right and the package falls at x-coordinate $3{\small,}000$, then the package will travel a total of $6{\small,}000$ units horizontally across conveyor belts, as illustrated below:

![annotated system](images/annotated%20system.png)

Determine the minimum achievable expected horizontal distance traveled by the package assuming an ideal initial choice of conveyor belt and direction.

## Constraints

$1 \leq N \leq 500{\small,}000 \\\n 1 \leq H_i \leq 999{\small,}999 \\\n 0 \leq A_i < B_i \leq 1{\small,}000{\small,}000$

## Approach

TODO