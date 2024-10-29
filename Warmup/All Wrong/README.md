# All Wrong

## Problem Description

There's a multiple-choice test with *N* questions, numbered from $1$ to $N$. Each question has $2$ answer options, labelled A and B. You know that the correct answer for the $i\text{th}$ question is the $i\text{th}$ character in the string $C$, which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.

Your task is to implement the function ```getWrongAnswers(N, C)``` which returns a string with $N$ characters, the $i\text{th}$ of which is the answer you should give for question $i$ in order to get it wrong (either "A" or "B").

## Constraints

$1 \leq N \leq 100$

$C _i \in \{\text{"A","B"}\}$

## Approach

### High-Level Solution

1. Create an empty string called ```answers```.
2. Iterate through each character $c_i$ of $C$ in order. For each character $c_i$, append an "A" to ```answers``` if $c_i=\text{"B"}$ and vice-versa.
3. Return ```answers```.

### Key Insights and Optimizations

N/A (the problem is trivial)