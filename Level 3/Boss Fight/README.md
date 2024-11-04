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

### High-Level Solution

#### getMaxDamageDealt(N, H, D, B)

*Top level function for the problem.*

Start by pairing two random warriors $i$ and $j$ where $i \neq j$. Then attempt to improve the pair by keeping one warrior constant and finding the warrior that pairs best with this constant warrior to inflict the maximum possible damage. Do this again with the newly found warrior kept constant instead. If the best pair of warriors $(k, l)$ found after these two searches has not changed then return the damage dealt by these warriors. Otherwise, repeat the search with $k$ and $j$ as the starting pair of warriors. 

### Key Insights and Optimizations

- We can employ an algorithm that continuously finds "local" optimizations to a given starting pair of warriors until converging to a maximum (e.g. optimizing one warrior to be paired with another until it is impossible to increase damage dealt by swapping only a single warrior).