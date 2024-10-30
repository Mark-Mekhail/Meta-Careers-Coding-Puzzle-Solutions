# Uniform Integers

## Problem Description

A positive integer is considered uniform if all of its digits are equal. For example, $222$ is uniform, while $223$ is not.

Given two positive integers $A$ and $B$, determine the number of uniform integers between $A$ and $B$, inclusive.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq A \leq B \leq 10^{12}$

## Approach

### High-Level Solution

#### getUniformIntegerCountInInterval(A, B)

Top level function for the problem.

1. Initialize the variables ```uniform_int_count``` to $0$ and ```next_uniform_int``` to ```getNextUniformInt(A)```.
2. While ```next_uniform_int``` $\leq B$, increment ```uniform_int_count``` and set ```next_uniform_int``` to ```getNextUniformInt(next_uniform_int + 1)```.
3. Return ```uniform_int_count```.

#### getNextUniformInt(floor)

Given an integer ```floor```, returns the smallest uniform integer greater than or equal to floor.

1. Determine the value of the first digit of ```floor```. Store this value in the variable ```first_digit```.
2. Construct an integer ```next_uniform``` that has same number of digits as ```floor``` but where all digits have the value of ```first_digit```.
3. If ```next_uniform < floor```, increment all digits in ```next_uniform```.
4. Return ```next_uniform```.

### Key Insights and Optimizations

- For any integer $I$ with $d$ digits and leading digit $i$, the smallest uniform integer $j \geq I$ will be either $d$ repetitions of $i$ or $d$ repetitions of $(i+1)$.