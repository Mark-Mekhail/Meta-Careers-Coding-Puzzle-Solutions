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

## Solution

### Function Descriptions and Implementation Approaches

#### getSecondsElapsed(C, N, A, B, K)

*Top level function for the problem.*

Determine the sum of the lengths of the tunnels covering the track. Using this value, calculate the number of full rotations $R$ that the train can take on the track without exceeding $K$ time under tunnels. Finally, go through all tunnel positions in order of start position and determine the position $p$ at which the train will meet $K$ seconds of tunnel time. Return $R \times C + p$.

### Key Insights and Optimizations

- If the total length of all tunnels in the track is $L$, we know that the train will circle around all tunnels in the track $R = \text{floor}({K - 1 \over L})$ times. Giving us a total travel time of $R \times C$ before the last trip around the track. All we need to do now is determine where along the track the train will have reached the target tunnel time and add this position to $R \times C$ to get the total time elapsed.