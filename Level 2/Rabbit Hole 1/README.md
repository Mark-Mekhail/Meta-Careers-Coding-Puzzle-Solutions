# Rabbit Hole (Chapter 1)

## Problem Description

*Note: [Chapter 2](../../Level%203/Rabbit%20Hole%202/) is a harder version of this puzzle.*

You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.

The encyclopedia consists of $N$ different web pages, numbered from $1$ to $N$. Each page $i$ contains nothing but a single link to a different page $L_i$.

A session spent on this website involves beginning on one of the $N$ pages, and then navigating around using the links until you decide to stop. That is, while on page $i$, you may either move to page $L_i$, or stop your browsing session.

Assuming you can choose which page you begin the session on, what's the maximum number of different pages you can visit in a single session? Note that a page only counts once even if visited multiple times during the session.

## Constraints

$1 \leq N \leq 500{\small,}000$

$1 \leq L_i \leq N$

$L_i \neq i$

## Approach

### High-Level Solution

#### getMaxVisitableWebpages(N, L)

Top level function for the problem.

1. Initialize the variables ```max_visits``` to $0$ and ```webpage_hops``` to an empty map.
2. Go through every page $1 \leq i \leq N$. For each page $i$, if the page has already been visited skip the steps below and move on to the next page. Otherwise, follow the steps below for page $i$:
    1. Initialize the variables ```visit_order``` to a queue containing $i$, ```next_page``` to $L_i$, and ```visits``` to $1$. 
    2. While ```next_page``` is not in ```visit_order```, if ```next_page``` is a key in ```webpage_hops```, increment ```visits``` by ```webpage_hops[next_page]``` and move on to the next step. Otherwise, increment ```visits```, add ```next_page``` to the end of ```visit_order```, and set ```next_page``` to $L_{\text{next\_page}}$.
    3. Set ```max_visits``` to the greater of its current value and ```visits```.
    4. Initialize ```reached_cycle``` to ```false```.
    5. Go through the pages in ```visit_order``` in order from the front to the end of the queue. For each page $j$, if ```next_pos``` $= j$, set ```reached_cycle``` to ```true```. Next, set ```webpage_hops[j]``` to ```visits```. If ```reached_cycle``` is ```false```, decrement ```visits```.
3. Return ```max_visits```.

### Key Insights and Optimizations

- For this problem, webpages can be thought of as nodes in a directed graph, where an edge exists from each node $i$ to $L_i$. Since each node links to only a single page, the problem can be simplified to that of finding the size of the largest connected component in this directed graph. To do this, we can go through every node and perform a depth-first search (DFS) to find the number of nodes that can be reached from that starting node. The maximum number of visitable pages will simply be the greatest value of all these values.
- We can reduce the number of DFS operations needed by observing that all nodes in a cycle will be visited during the same DFS and will be able to reach the same number of nodes. Furthermore, if we perform a DFS on a given node and encounter a node for which a DFS has already been performed, we don't need to continue the DFS because we've already computed the number of nodes that can be reached from the encountered node and we can just use this value since all nodes reached by it in its DFS will be unique (otherwise the previous node is in a loop with it, in which case it would have been reached in the previous DFS).