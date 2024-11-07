# Uniform Integers

## Problem Description

A positive integer is considered uniform if all of its digits are equal. For example, $222$ is uniform, while $223$ is not.

Given two positive integers $A$ and $B$, determine the number of uniform integers between $A$ and $B$, inclusive.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq A \leq B \leq 10^{12}$

## Solution

### Function Descriptions and Implementation Approaches

#### getUniformIntegerCountInInterval(A, B)

*Top level function for the problem.*

Find the smallest uniform integer $i$ with a value greater than or equal to $A$. If $i \leq B$, find the next uniform integer greater than $i$. Repeat this process until $i > B$ and return the number of different uniform integers $i \leq B$ that were found.

#### getNextUniformInt(floor)

*Given an integer ```floor```, returns the smallest uniform integer greater than or equal to floor.*

Construct an integer $i$ that contains the same number of digits as ```floor```, where all digits are equal to the first digit of ```floor```. If $i < $ ```floor```, increment each digit of $i$. Return $i$.

### Key Insights and Optimizations

- For any integer $I$ with $d$ digits and leading digit $i$, the smallest uniform integer $j \geq I$ will be either $d$ repetitions of $i$ or $d$ repetitions of $(i+1)$.