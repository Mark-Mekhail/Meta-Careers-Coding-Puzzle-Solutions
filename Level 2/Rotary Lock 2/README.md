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

## Solution

### Function Descriptions and Implementation Approaches

#### getMinCodeEntryTime(N, M, C)

*Top level function for the problem.*

Go through all integers in the code in reverse order. At each iteration, determine and store the amount of time needed to get from any previous valid lock configuration (i.e. any configuration where at least one lock is at the position of the previous integer in the code). Refer to the [insights](#key-insights-and-optimizations) section for an explanation of the dynamic programming (DP) relation to use to populate these values. Finally, return the time calculated starting from the initial lock position.

1. Initialize the variable ```time_to_unlock``` to a map that maps every value in $C$ to $0$.
2. Go through the integers $C_i$ in $C$ in reverse order. At each iteration, create a map ```cur_time_to_unlock``` and map every value $C_j$ in $C$ to the minimum of the amount of time required to move the pair of lock positions from $C_{i-1}$ and $C_j$ to $C_i$ and $C_k$ plus the value of ```time_to_unlock[C[k]]```. Set ```time_to_unlock``` to ```cur_time_to_unlock``` before moving on to $C_{i-1}$.
3. Return ```time_to_unlock[1]```.

#### getRotationTime(N, start, end)

*Given a lock with $N$ integers, returns the minimum amount of time required to rotate the lock from ```start``` to ```end```.*

Return the minimum of the time required to rotate from ```start``` to ```end``` by turning right and left.

### Key Insights and Optimizations

- We can employ a dynamic programming (DP) solution to this problem by starting from the final number in the code sequence and working backwards, continuously tracking the minimum amount of time needed to get from a given valid previous configuration of lock positions to the end of the code sequence. The DP relation is formally $T_{i,j} = \text{min} \{ T_{i+1,j} + \text{getRotationTime}(N, C_{i+1}, C_i), T_{i+1,i} + \text{getRotationTime}(N, C_j, C_i))$ where $C_0=1$. The problem entails finding $T_{0,0}$.