# Uniform Integers

## Problem Description

A positive integer is considered uniform if all of its digits are equal. For example, $222$ is uniform, while $223$ is not.

Given two positive integers $A$ and $B$, determine the number of uniform integers between $A$ and $B$, inclusive.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq A \leq B \leq 10^{12}$

## Approach

### High-Level Solution

Starting with $A$, find the smallest uniform integer $C$ such that $C \geq A$. If $C \leq B$, add one to a running count, set $A=C+1$, and repeat until $C > B$. 

### Key Insights and Optimizations

- To get the smallest uniform integer $C$ such that $C \geq A$, we can simply take the first digit $a$ of $A$ and form a number that has as many digits as $A$ where all digits have the value $a$. If this number is less than $A$, we can simply do the same but with $a=a+1$ and this is guaranteed to be greater than $A$.