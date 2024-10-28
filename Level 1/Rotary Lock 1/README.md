# Rotary Lock (Chapter 1)

## Problem Description

*Note: [Chapter 2](../../Level%202/Director%20of%20Photography%202/) is a harder version of this puzzle.*

You're trying to open a lock. The lock comes with a wheel which has the integers from $1$ to $N$ arranged in a circle in order around it (with integers $1$ and $N$ adjacent to one another). The wheel is initially pointing at $1$.

For example, the following depicts the lock for $N = 10$ (as is presented in the second sample case).

![Lock Image](images/Lock%20Image.png)

It takes $1$ second to rotate the wheel by $1$ unit to an adjacent integer in either direction, and it takes no time to select an integer once the wheel is pointing at it.

The lock will open if you enter a certain code. The code consists of a sequence of $M$ integers, the $i\text{th}$ of which is $C_i$. Determine the minimum number of seconds required to select all $M$ of the code's integers in order.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq N \leq 50{\small,}000{\small,}000$

$1 \leq M \leq 1{\small,}000$

$1 \leq C_i \leq N$

## Approach

### High-Level Solution

Go through the sequence of integers in the code in order. For each integer, determine the minimum amount of time needed to rotate the wheel from its previous position to the position of the current integer. Add this value to a running total.

### Key Insights and Optimizations

- We can calculate the minimum time needed to rotate the wheel from one position to another by taking the minimum of the time needed to do so by rotating to the right and to the left.