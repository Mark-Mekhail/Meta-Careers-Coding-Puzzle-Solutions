# Missing Mail

## Problem Description

You are the manager of a mail room which is frequently subject to theft. A period of $N$ days is about to occur, such that on the $i\text{th}$ day, the following sequence of events will occur in order:

1. A package with a value of $V_i$ dollars will get delivered to the mail room (unless $V_i = 0$, in which case no package will get delivered).
2. You can choose to pay $C$ dollars to enter the mail room and collect all of the packages there (removing them from the room), and then leave the room.
3. With probability $S$, all packages currently in the mail room will get stolen (and therefore removed from the room).

Note that you're aware of the delivery schedule $V_{1...N}$, but can only observe the state of the mail room when you choose to enter it, meaning that you won't immediately be aware of whether or not packages were stolen at the end of any given day.

Your profit after the $N\text{th}$ day will be equal to the total value of all packages which you collected up to that point, minus the total amount of money you spent on entering the mail room.

Please determine the maximum expected profit you can achieve (in dollars).

*Note: Your return value must have an absolute or relative error of at most $10^{-6}$ to be considered correct.*

## Constraints

$1 \leq N \leq 4{\small,}000$

$0 \leq V_i \leq 1{\small,}000$

$1 \leq C \leq 1{\small,}000$

$0.0 \leq S \leq 1.0$

## Approach

### High-Level Solution

#### getMaxExpectedProfit(N, V, C, S)

Top level function for the problem.

1. Initialize a variable ```max_expected_profit``` to a list of $N+1$ zeroes.
2. Populate ```max_expected_profit``` from the end to the beginning of the list. Perform the following for each cell $i$:
    1. Initialize a variable ```expected_mail``` to $0$.
    2. Go through all days $j \geq i$ in order. For each day $j$, update ```expected_mail_value``` to be the expected amount of mail remaining in the mail room on that day assuming mail was last collected on day $i-1$. Use this value to help calculate the maximum expected profit if mail was to be collected on day $j$. Set ```max_expected_profit[i]``` to the maximum of this value and its current value.
3. Return ```max_expected_profit[0]```.

### Key Insights and Optimizations

- A dynamic programming (DP) solution helps us solve the problem within the time limit. The DP relation is ```max_expected_profit[i]``` $=\text{max}_{j \geq i}$ {```expected_mail[j]```$+$```max_expected_profit[j+1]```} where ```expected_mail[j]``` is the expected value of all the mail in the mailroom on day $j$ assuming mail was last collected on day $i-1$. Essentially, we take the max expected profit of all days $j  \geq i$ where mail is first collected on day $j$, ignoring any days prior to $i$.