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

## Solution

### Function Descriptions and Implementation Approaches

#### getMaxAdditionalDinersCount(N, K, M, S)

*Top level function for the problem.*

Go through all occupied seats in $S$ in order from smallest to greatest position and calculate the maximum amount of diners that can be seated before the first occupied seat, between each adjacent pair of occupied seats, and after the last occupied seat.

#### getMaxDinersBetweenSeats(startPos, endPos, K)

*Given a starting seat position ```startPos``` and an ending seat position ```endPos```, returns the maximum number of socially-distanced seats in the interval [```startPos```, ```endPos```] that can be occupied assuming that the seats at ```startPos``` and ```endPos``` are socially distanced from occupied seats before and after them.*

Implementation is straightforward.

### Key Insights and Optimizations

- We can seat **ceil**($(j-i) \over (K+1)$) people in a way that satisfies social distancing protocols in a sequence of available seats in the interval [$i$, $j$], assuming the endpoints of the interval are socially-distanced from the seats around them. 