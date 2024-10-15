# All Wrong

## Problem Description

There's a multiple-choice test with *N* questions, numbered from $1$ to $N$. Each question has $2$ answer options, labelled A and B. You know that the correct answer for the $i$th question is the $i$th character in the string $C$, which is either "A" or "B", but you want to get a score of 0 on this test by answering every question incorrectly.

Your task is to implement the function ```getWrongAnswers(N, C)``` which returns a string with $N$ characters, the $i$th of which is the answer you should give for question $i$ in order to get it wrong (either "A" or "B").

## Constraints

$1 \leq N \leq 100$

$C _i \in \{‘‘A",‘‘B"\}$

## Approach

Start with an empty string. Iterate through each character $c_i$ of $C$ and append an "A" to the string if $c_i = $ "B" and vice-versa.