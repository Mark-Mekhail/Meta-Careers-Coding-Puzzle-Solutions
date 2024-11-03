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

*Top level function for the problem.*

Go through all webpages. If a webpage has not yet been visited, perform a depth-first search (DFS) from the webpage to determine the number of pages that can be visited from the webpage (as well as each of its child webpages). Stop the DFS early if a webpage is visited that has already been visited and simply add the number of visitable pages from that page to whatever DFS depth has been achieved so far from the start webpage. Return the maximum DFS depth achieved.

### Key Insights and Optimizations

- For this problem, webpages can be thought of as nodes in a directed graph, where an edge exists from each node $i$ to $L_i$. Since each node links to only a single page, the problem can be simplified to that of finding the size of the largest connected component in this directed graph. To do this, we can go through every node and perform a DFS to find the number of nodes that can be reached from that starting node. The maximum number of visitable pages will simply be the greatest value of all these values.
- We can reduce the number of DFS operations needed by observing that all nodes in a cycle will be visited during the same DFS and will be able to reach the same number of nodes. Furthermore, if we perform a DFS on a given node and encounter a node for which a DFS has already been performed, we don't need to continue the DFS because we've already computed the number of nodes that can be reached from the encountered node and we can just use this value since all nodes reached by it in its DFS will be unique (otherwise the previous node is in a loop with it, in which case it would have been reached in the previous DFS).