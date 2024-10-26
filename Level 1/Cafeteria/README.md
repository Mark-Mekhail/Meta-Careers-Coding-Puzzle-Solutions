# Cafeteria

## Problem Description

A cafeteria table consists of a row of $N$ seats, numbered from $1$ to $N$ from left to right. Social distancing guidelines require that every diner be seated such that $K$ seats to their left and $K$ seats to their right (or all the remaining seats to that side if there are fewer than $K$) remain empty.

There are currently $M$ diners seated at the table, the $i\text{th}$ of whom is in seat $S_i$. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq N \leq 10^{15}$
 
$1 \leq K \leq N$

$1 \leq M \leq 500{\small,}000$

$M \leq N$

$1 \leq S_i \leq N$

## Approach

### High-Level Solution Steps

1. Go through each occupied seat in increasing order of seat number and calculate the maximum number of people that can occupy seats between the current occupied seat and the previously calculated next available location. Add this value to a cumulative sum.
2. Add the number of people that can be seated between the last occupied seat and the last available seat to the aforementioned sum.

### Key Insights and Optimizations

- Between each available seat $i$ and the following occupied seat (or last seat) $j$, floor($(j-i) \over (K+1)$) people can be seated without violating social distancing rules. 