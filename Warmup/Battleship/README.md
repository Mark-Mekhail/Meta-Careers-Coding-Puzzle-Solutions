# Battleship

## Problem Description

You're playing Battleship on a grid of cells with $R$ rows and $C$ columns. There are 0 or more battleships on the grid, each occupying a single distinct cell. The cell in the $i\text{th}$ row from the top and $j\text{th}$ column from the left either contains a battleship ($G_{i,j}=1$) or doesn't ($G_{i,j}=0$).

You're going to fire a single shot at a random cell in the grid. You'll choose this cell uniformly at random from the $R*C$ possible cells. You're interested in the probability that the cell hit by your shot contains a battleship.

Your task is to implement the function ```getHitProbability(R, C, G)``` which returns this probability.

## Constraints

$1 \leq R,C \leq 100 \newline 0 \leq G_{i,j} \leq 1$

## Approach

Count the number of cells containing ships ($G_{i,j}=1$) and divide this by the total number of cells in the grid ($R*C$) to get the probability that a ship will be hit by a random shot.