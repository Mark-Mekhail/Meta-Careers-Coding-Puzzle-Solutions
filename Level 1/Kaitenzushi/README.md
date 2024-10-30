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

## Approach

### High-Level Solution

1. Create a queue ```dish_queue``` and a set ```dish_set```. These will help track the $K$ most recently consumed dishes.
2. Add $K$ "garbage" dishes to ```dish_queue```.
3. Initialize a variable ```dish_count``` to $0$.
4. Go through the dishes in $D$ in order. For each dish $D_i$, if $D_i$ is not already in the dish set (i.e. it is not one of the previous $K$ dishes seen), increment ```dish_count```, add $D_i$ to ```dish_set``` and remove the dish at the top of ```dish_queue``` from ```dish_set```. 
5. Return ```dish_count```.

### Key Insights and Optimizations

- We can track the last $K$ dishes consumed when going through the dishes by keeping a set and a queue of the last $K$ dishes eaten. Whenever a new dish is encountered, we can remove the dish at the front of the queue (i.e. the Kth most recently consumed dish) from the queue and the set and add the new dish to both in constant time.