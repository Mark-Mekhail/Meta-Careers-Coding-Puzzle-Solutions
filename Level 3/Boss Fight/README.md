# Boss Fight

## Problem Description

There are $N$ warriors, the $i\text{th}$ of which has a health of $H_i$ units and can deal $D_i$ units of damage per second. They are confronting a boss who has unlimited health and can deal $B$ units of damage per second. Both the warriors and the boss deal damage continuously - for example, in half a second, the boss deals $B/2$  units of damage.

The warriors feel it would be unfair for many of them to fight the boss at once, so they'll select just two representatives to go into battle. One warrior $i$ will be the front line, and a different warrior $j$ will back them up. During the battle, the boss will attack warrior $i$ until that warrior is defeated (that is, until the boss has dealt $H_i$ units of damage to them), and will then attack warrior $j$ until that warrior is also defeated, at which point the battle will end. Along the way, each of the two warriors will do damage to the boss as long as they are undefeated.

Of course, the warriors will never prevail, but they'd like to determine the maximum amount of damage they could deal to the boss for any choice of warriors $i$ and $j$ before the battle ends.

## Constraints

$2 \leq N \leq 500{\small,}000$

$1 \leq H_i \leq 1{\small,}000{\small,}000{\small,}000$

$1 \leq D_i \leq 1{\small,}000{\small,}000{\small,}000$

$1 \leq B \leq 1{\small,}000{\small,}000{\small,}000$

## Approach

My approach starts by pairing two random warriors. I then attempt to improve the pair by swapping the second warrior to be whatever warrior pairs best with the first warrior to inflict the most possible damage and then swapping the first warrior with whatever warrior pairs best with the new second warrior. If the new pair improves upon the damage dealt by the old pair then I perform this operation again, otherwise I know I've found the optimal pair and I return the amount of damage this optimal pair can deal against the boss.