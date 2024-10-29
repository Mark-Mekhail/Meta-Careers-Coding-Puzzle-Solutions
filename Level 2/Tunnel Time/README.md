# Tunnel Time

## Problem Description

There’s a circular train track with a circumference of $C$ metres. Positions along the track are measured in metres, clockwise from its topmost point. For example, the topmost point is position $0$, $1$ metre clockwise along the track is position $1$, and $1$ metre counterclockwise along the track is position $C - 1$.

A train with negligible length runs clockwise along this track at a speed of $1$ metre per second, starting from position $0$. After $C$ seconds go by, the train will have driven around the entire track and returned to position $0$, at which point it will continue going around again, with this process repeated indefinitely.

There are $N$ tunnels covering sections of the track, the $i\text{th}$ of which begins at position $A_i$ and ends at position $B-i$ (and therefore has a length of $B_i - A_i$ metres). No tunnel covers or touches position $0$ (including at its endpoints), and no two tunnels intersect or touch one another (including at their endpoints). For example, if there's a tunnel spanning the interval of positions 
$[1,4]$, there cannot be another tunnel spanning intervals $[2,3]$ nor $[4,5]$.

The train’s *tunnel time* is the total number of seconds it has spent going through tunnels so far. Determine the total number of seconds which will go by before the train’s tunnel time becomes $K$.

## Constraints

$3 \leq C \leq 10^{12}$

$1 \leq N \leq 500{\small,}000$

$1 \leq A_i < B_i \leq C - 1$

$1 \leq K \leq 10^{12}$

## Approach

TODO