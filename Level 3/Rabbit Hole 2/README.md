# Rabbit Hole (Chapter 2)

## Problem Description

You're having a grand old time clicking through the rabbit hole that is your favorite online encyclopedia.

The encyclopedia consists of $N$ different web pages, numbered from $1$ to $N$. There are $M$ links present across the pages, the $i\text{th}$ of which is present on page $A_i$ and links to a different page $B_i$. A page may include multiple links, including multiple leading to the same other page.

A session spent on this website involves beginning on one of the $N$ pages, and then navigating around using the links until you decide to stop. That is, while on page $i$, you may either move to any of the pages linked to from it, or stop your browsing session.

Assuming you can choose which page you begin the session on, what's the maximum number of different pages you can visit in a single session? Note that a page only counts once even if visited multiple times during the session.

## Constraints

$2 \leq N \leq 500{\small,}000$

$1 \leq M \leq 500{\small,}000$

$1 \leq A_i, B_i \leq N$

$A_i \neq B_i $

## Solution

### Function Descriptions and Implementation Approaches

#### getMaxVisitableWebpages(N, M, A, B)

*Top level function for the problem.*

Use the functions below to convert create a simplified directed acyclic graph (DAG) of the problem where strongly connected components (SCCs), which are essentially maximal groups of websites with a path between each pair of websites (in both directions) in the group, are nodes of the graph with a "value" equal to the size of the SCC (i.e. the number of websites that make up the SCC) and an edge exists between two SCCs $i$ and $j$ if a webpage in SCC $i$ links to a webpage in SCC $j$. Find and return the largest sum of node values in any simple path in this graph.

#### getWebpageLinkMap(M, A, B)

*Constructs and returns a map that maps every website to the set of other websites that the website contains a link to.*

Implementation is fairly straightforward.

#### getSCCs(webpageLinkMap)

*Creates a map that maps a webpage index to a lowlink value that is unique to the SCC that the webpage is a part of. Returns this map as well as a list containing the SCC lowlink values sorted in reverse topological order.*

Run the [tarjan](#tarjanstartpage-webpagelinkmap-lowlinkmap-indexmap-traversalorder) function on each page in ```webpageLinkMap``` and return the ```lowlinkMap``` and ```traversalOrder``` populated by the tarjan algorithm.

#### tarjan(startPage, webpageLinkMap, lowlinkMap, indexMap, traversalOrder)

*Executes [Tarjan's Algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm) from a given starting webpage ```startPage```. It populates the ```lowlinkMap```, ```indexMap``` and ```traversalOrder``` inputs with the SCCs found while running the algorithm and ensures newly assigned indices do not conflict with existing indices.*

Run Tarjan's SCC algorithm with some extra bookkeeping to track the SCC discovery order and ensure we can map each webpage with the index assigned to the webpage.

#### getSCCLinkMap(webpageToSCCIndexMap, webpageLinkMap)

*Constructs a new map that maps each SCC in ```webpageToSCCIndexMap``` to the other SCCs that a webpage in the SCC directly links to as well as a map that maps each SCC to the size of the SCC. Returns these maps.*

For each webpage $i$ in ```webpageToSCCIndexMap```, go through the pages it links to (contained in ```webpageLinkMap```) , add the SCCs containing these pages to the set of SCCs mapped to by the SCC of page $i$, and increment the calculated size of SCC $i$.

#### largestPathSum(reverseTopologicalNodeOrder, linkMap, nodeWeightMap)

*Calculates and returns the largest sum of node weights in any simple path of a DAG where ```linkMap``` is the graph adjacency list, ```nodeWeightMap``` maps each node to its weight, and ```reverseTopologicalNodeOrder``` contains the entire list of nodes sorted in reverse topological order.*

Go through the nodes in ```reverseTopologicalNodeOrder``` in order. For each node $i$, compute the value of the largest sum of node weights of nodes in any path starting from node $i$ by adding the weight of node $i$ to the maximum path sum starting from any of node $i$'s children. Return the maximum of these path sums.

### Key Insights and Optimizations

- This problem is essentially a graph problem where webpages are nodes and links are directed edges. We need to find the [longest path](https://en.wikipedia.org/wiki/Longest_path_problem) of this graph.
- We can simply the problem by representing it as a DAG. In this graph, nodes correspond to SCCs of webpages, which are groups of websites where a path (in both directoins) exists between each pair of websites in the group, and have a weight equal to the number of webpages in the SCC. An edge exists from SCCs $i$ to $j$ if a webpage in SCC $i$ links to a webpage in SCC $j$. We know that this graph will be acyclic because if it had any cycle then that would mean it contains an SCC of size $> 1$ and therefore we could combine all webpages in the nodes of this SCC to create a larger SCC, which contradicts the **maximal** property of SCCs.
- We can employ Tarjan's algorithm to conveniently group webpages into SCCs and determine a reverse topological ordering of the SCCs. This allows us to construct the DAG described in the bullet point above.
- Once we've generated a DAG that can represent the problem as described above as well as its topoligical node ordering, finding the [*longest path*](https://en.wikipedia.org/wiki/Longest_path_problem#Acyclic_graphs) is fairly simple. We just need to remember to measure the length of a path as the sum of weights of nodes in the path.