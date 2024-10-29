# Rotary Lock (Chapter 2)

## Problem Description

*Note: [Chapter 1](../../Level%201/Rotary%20Lock%201/) is an easier version of this puzzle.*

You're trying to open a lock. The lock comes with two wheels, each of which has the integers from $1$ to $N$ arranged in a circle in order around it (with integers $1$ and $N$ adjacent to one another). Each wheel is initially pointing at $1$.

For example, the following depicts the lock for $N = 10$ (as is presented in the second sample case).

![Double lock image](images/Double%20Lock%20Image.png)

It takes $1$ second to rotate a wheel by $1$ unit to an adjacent integer in either direction, and it takes no time to select an integer once a wheel is pointing at it.

The lock will open if you enter a certain code. The code consists of a sequence of $M$ integers, the $i\text{th}$ of which is $C_i$. For each integer in the sequence, you may select it with either of the two wheels. Determine the minimum number of seconds required to select all $M$ of the code's integers in order.

## Constraints

$3 \leq N \leq 1{\small,}000{\small,}000{\small,}000$

$1 \leq M \leq 3{\small,}000$

$1 \leq C_i \leq N$

## Approach

TODO