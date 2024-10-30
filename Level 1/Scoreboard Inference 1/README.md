# Scoreboard Inference (Chapter 1)

## Problem Description

*Note: [Chapter 2](../../Level%202/Scoreboard%20Inference%202/) is a harder version of this puzzle. The only difference is a larger set of possible problem point values.*

You are spectating a programming contest with $N$ competitors, each trying to independently solve the same set of programming problems. Each problem has a point value, which is **either 1 or 2**.

On the scoreboard, you observe that the $i\text{th}$ competitor has attained a score of $S_i$, which is a positive integer equal to the sum of the point values of all the problems they have solved.

The scoreboard does not display the number of problems in the contest, nor their point values. Using the information available, you would like to determine the minimum possible number of problems in the contest.

## Constraints

$1 \leq N \leq 500{\small,}000$

$1 \leq S_i \leq 1{\small,}000{\small,}000{\small,}000$

## Approach

### High-Level Solution

#### getMinProblemCount(N, S)

Top level function for the problem.

1. Initialize the variables ```max_score``` to $-1$ and ```contains_odd``` to ```false```.
2. For each score $S_i$ in $S$, set ```max_score``` to the greater of its current value and $S_i$. Also set ```contains_odd``` to ```true``` if $S_i$ is odd.
3. Set ```min_problem_count``` to ```max_score / 2``` (integer division).
4. Increment ```min_problem_count``` by 1 if ```contains_odd``` is ```true```.

### Key Insights and Optimizations

- The smallest possible set of problems must contain enough points to allow the maximum score to be possible. This can be attained by allocating as many 2-point problems as needed to reach at least the maximum score - 1. If there are any odd scores, we also need a 1-point problem which combined with any number of two-point problems can create any odd score needed up to the maximum score.