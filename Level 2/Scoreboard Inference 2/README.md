# Scoreboard Inference (Chapter 2)

## Problem Description

*Note: [Chapter 1](../../Level%201/Scoreboard%20Inference%201/) is an easier version of this puzzle. The only difference is a smaller set of possible problem point values.*

You are spectating a programming contest with $N$ competitors, each trying to independently solve the same set of programming problems. Each problem has a point value, which is **either 1, 2, or 3**.

On the scoreboard, you observe that the $i\text{th}$ competitor has attained a score of $S_i$, which is a positive integer equal to the sum of the point values of all the problems they have solved.

The scoreboard does not display the number of problems in the contest, nor their point values. Using the information available, you would like to determine the minimum possible number of problems in the contest.

## Constraints

$1 \leq N \leq 500{\small,}000$

$1 \leq S_i \leq 1{\small,}000{\small,}000{\small,}000$

## Approach

### High-Level Solution

#### getMinProblemCount(N, S)

Top level function for the problem.

1. Go through all problems in $S$ and store the highest score, second-highest score, presence of a score of $1$, presence of a score greater than $1$ with a remainder of $1$ when divided by $3$, and presence of a score with a remainder of $2$ when divided by $3$ in variables ```max_score```, ```second_max_score```, ```has_one```, ```has_one_remainder```, and ```has_two_remainder```, respectively.
2. Using the information gathered in step 1, determine the number of problems with $1$ and $2$ points that the minimal set of problems should have. Store these values in variables ```ones``` and ```twos```. See the [insights section](#key-insights-and-optimizations) for an explanation of the logic behind this step.
3. Using the information from step 2, determine the minimum number of problems with $3$ points needed to make it possible to achieve a score of ```max_score```. Store this number in a variable ```threes```.
4. Return ```ones + twos + threes```.

### Key Insights and Optimizations

- The key to solving this question lies in how we determine the value of ```ones``` and ```twos```. An important fact to keep in mind is that we should never have more than two problems that are not worth $3$ points (I will not prove this here but come up with examples to gain intuition if this is unclear). The next sub-points describe different scenarios and what they say about these values. 
    - If all scores are multiples of $3$ then ```ones``` and ```twos``` should both be $0$ because $3$-point problems can minimally make up all scores.
    - Otherwise, f ```has_two_remainder``` is ```false``` but at least one problem has a remainder of $1$ when divided by $3$ then there must be at least one problem with a value of $1$, so ```ones``` $= 1$, and all other scores can be achieved through a combination of $3$-point problems and the $1$-point problem so ```twos``` should be $0$.
    - Otherwise, if ```has_two_remainder``` is ```true```, we set ```twos``` to $1$ because we know that at least one $2$-point problem can be part of the minimal set of problems since even if a $1$ is needed, the remainder of $2$ can be made up for by another $1$-point problem or a $2$-point problem. 
        - If ```has_one``` is ```true```, then we need a $1$-point problem, so ```ones``` should equal $1$. This is sufficient for creating any score, when combined with enough $3$-point problems.
        - If ```has_one``` is ```false``` but ```has_one_remainder``` is ```true``` the situation becomes a bit more complicated. If the ```second_max_score``` is just one point lower than ```max_score``` and is a multiple of $3$, we set ```ones``` to $1$ because with a cap of two problems with under $3$ points and the desire to minimize the total number of problems we need at least one problem to have the value $1$ to make up ```second_max_score```, which is a multiple of $3$, and ```max_score```, which is greater by $1$. Otherwise, we can get by with no $1$-point problems and two $2$-point problems because the two $2$-point problems give us a total of $4$ points and can be added to any number of $3$-point problems to achieve a score that has a remainder of $1$ when divided by $3$ (except for $1$, which we already know is not a score since ```has_one``` is ```false```). We therefore set ```twos``` to $2$ and keep ```ones``` as $0$.