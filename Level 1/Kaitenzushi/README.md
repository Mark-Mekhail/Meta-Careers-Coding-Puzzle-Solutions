# Kaitenzushi

## Problem Description

There are $N$ dishes in a row on a kaiten belt, with the $i\text{th}$ dish being of type $D_i$. Some dishes may be of the same type as one another.

You're very hungry, but you'd also like to keep things interesting. The $N$ dishes will arrive in front of you, one after another in order, and for each one you'll eat it as long as it isn't the same type as any of the previous $K$ dishes you've eaten. You eat very fast, so you can consume a dish before the next one gets to you. Any dishes you choose not to eat as they pass will be eaten by others.

Determine how many dishes you'll end up eating.

*Please take care to write a solution which runs within the time limit.*

## Constraints

$1 \leq N \leq 500{\small,}000$

$1 \leq K \leq N$

$1 \leq D_i \leq 1{\small,}000{\small,}000$

## Solution

### Function Descriptions and Implementation Approaches

#### getMaximumEatenDishCount(N, D, K)

*Top level function for the problem.*

Create a queue ```dish_queue``` that is initially filled with $K$ "garbage" dishes.

Go through the dishes in $D$ in order. For each dish $D_i$, if $D_i$ is not already in ```dish_queue``` (i.e. it is not one of the previous $K$ dishes seen), remove the dish at the front of ```dish_queue``` and add $D_i$ to the queue. Return a count of the removals from ```dish_queue``` that took place. 

### Key Insights and Optimizations

- We can track the last $K$ dishes consumed when going through the dishes by keeping a set and a queue of the last $K$ dishes eaten. Whenever a new dish is encountered, we can remove the dish at the front of the queue (i.e. the Kth most recently consumed dish) from the queue and the set and add the new dish to both in constant time.