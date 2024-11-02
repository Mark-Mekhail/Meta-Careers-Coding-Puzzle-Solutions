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

### High-Level Solution

#### getMinCodeEntryTime(N, M, C)

Top level function for the problem.

1. Initialize the variable ```time_to_unlock``` to a map that maps every value in $C$ to $0$.
2. Go through the integers $C_i$ in $C$ in reverse order. At each iteration, create a map ```cur_time_to_unlock``` and map every value $C_j$ in $C$ to the minimum of the amount of time required to move the pair of lock positions from $C_{i-1}$ and $C_j$ to $C_i$ and $C_k$ plus the value of ```time_to_unlock[C[k]]```. Set ```time_to_unlock``` to ```cur_time_to_unlock``` before moving on to $C_{i-1}$.
3. Return ```time_to_unlock[1]```.

#### get_time_to_rotate(N, start, end)

Given a lock with $N$ integers, returns the minimum amount of time required to rotate the lock from ```start``` to ```end```.

1. Return the minimum of the time required to rotate from ```start``` to ```end``` by turning right and left.

### Key Insights and Optimizations

- We can employ a dynamic programming (DP) solution to this problem by starting from the final number in the code sequence and working backwards, continuously tracking the minimum amount of time needed to get from a given valid previous configuration of lock positions to the end of the code sequence. The DP relation is formally $\text{min\_entry\_time}_{i,j} = \text{min} (\text{min\_entry\_time}_{i+1,j} + \text{time\_to\_rotate}(N, C_{i+1}, C_i), \text{min\_entry\_time}_{i+1,i} + \text{time\_to\_rotate}(N, C_j, C_i))$ where $C_0=1$ and we need to find $\text{min\_entry\_time}_{0,0}$.