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

### High-Level Solution

#### getMaxAdditionalDinersCount(N, K, M, S)

Top level function for the problem.

1. Initialize ```additional_diners``` to $0$.
2. Sort $S$ in increasing order.
3. Go through each occupied seat in $S$ in increasing order of seat number. For each occupied seat $S_i$, calculate the maximum number of people that can occupy seats between the previously calculated next occupiable seat position ($0$ at the start and the number of the most recently processed occupied seat plus $K + 1$ afterwards) and $S_i$. Add this value to ```additional_diners```.
4. Calculate the number of people that can be seated between the occupied seat with the greatest seat number in $S$ and $N$. Add this value to ```additional_diners```.
5. Return ```additional_diners```.

#### getMaxDinersBetweenSeats(startPos, endPos, K)

Given a starting seat position ```startPos``` and an ending seat position ```endPos```, returns the maximum number of socially-distanced seats in the interval [```startPos```, ```endPos```] that can be occupied assuming that the seats at ```startPos``` and ```endPos``` are socially distanced from occupied seats before and after them.

### Key Insights and Optimizations

- Between the previously calculated next occupiable seat position $i$ and the following occupied seat (or last seat) $j$, $(j-i) \over (K+1)$ people can be seated without violating social distancing rules. 