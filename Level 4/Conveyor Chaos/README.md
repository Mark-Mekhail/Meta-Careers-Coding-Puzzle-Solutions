# Conveyor Chaos

## Problem Description

A distribution center moves packages around using a system of conveyor belts, which can be represented as line segments on the 2D Cartesian plane. The $i\text{th}$ conveyor belt runs from coordinates $(A_i,H_i)$ to $(B_i,H_i)$. No two conveyor belts share any points in common, including endpoints or interior points. Gravity points in the direction of the negative y-axis, meaning that objects normally fall vertically downwards, with their y-coordinate decreasing over time.

Each conveyor belt runs to either the left or the right. A package can be considered to occupy a single point on the plane. If a package lands strictly within conveyor belt $i$ (excluding its endpoints), then it will be transported to its left or right end (either $(A_i,H_i)$ or $(B_i,H_i)$), depending on the conveyor belt's direction, before continuing to fall vertically downwards.

You'll start by selecting a single conveyor belt and choosing a fixed direction (either left or right) for it to run in. Then, random directions will be independently chosen for each of the remaining $N-1$ conveyor belts (each being either left or right with equal probability). Finally, a single package will be dropped into the system from high above, at coordinates $(x,1{\small,}000{\small,}000)$, where $x$ is a real value drawn uniform randomly from the inclusive interval $[0, 1{\small,}000{\small,}000]$. Your objective is to minimize the expected horizontal distance which this package will travel along conveyor belts before hitting the ground (any point with y-coordinate $0$).

For example, consider the following system of conveyor belts (as are present in the second sample case):

![system](images/system.png)

Consider picking the conveyor belt at y-coordinate $5$ and causing it to run to the left. If it then so happens that the bottommost conveyor belt also runs to the left while the other three run to the right and the package falls at x-coordinate $3{\small,}000$, then the package will travel a total of $6{\small,}000$ units horizontally across conveyor belts, as illustrated below:

![annotated system](images/annotated%20system.png)

Determine the minimum achievable expected horizontal distance traveled by the package assuming an ideal initial choice of conveyor belt and direction.

## Constraints

$1 \leq N \leq 500{\small,}000$

$1 \leq H_i \leq 999{\small,}999$

$0 \leq A_i < B_i \leq 1{\small,}000{\small,}000$

## Approach

### High-Level Solution

#### getMinExpectedHorizontalTravelDistance(N, H, A, B)

*Top level function for the problem.*

Create a sorted (in non-ascending order of height) list of conveyor objects (refer to the [Python solution](./python/Conveyor_Chaos.py) for a description of the Conveyor class). Use the functions below to populate the objects. Once all conveyor objects have had their fields populated, go through each conveyor and track the sum of the expected horizontal movement of the package on each conveyor assuming it runs in a random direction as well as the reduction in movement assuming the conveyor is set to run in a single direction. Subtract the largest reduction found from the computed sum to get the smallest possible expected movement and return this value.

#### populateConveyorRelationships(conveyors)

*Given a sorted list of conveyors, determines which conveyor a package from a given conveyor will land on if dropped from either end of the conveyor, which we refer to as a child (left or right depends on which end of the conveyor the child gets packages from). All conveyors will be populated with this information after the function completes execution.*

Go through the conveyors in order and for each higher conveyor that hasn't had its child information populated already, check if packages from these higher conveyors will land on the current conveyor. If so, we know that the current conveyor is a child of the higher conveyor so track this information in the object representing the higher conveyor.

#### populateConveyorExpectedHorizontals(conveyors)

*Given a sorted list of conveyors with conveyor-child relationships already populated, calculates the expected horizontal movement that a package dropped on the conveyor will experience assuming all conveyors have a random direction. All conveyors will be populated with this information after the function completes execution.*

Go through conveyors in reverse order (from lowest to highest) and calculate the expected horizontal movement of a package dropped on the conveyor using its size and the already computed (because they must be lower than the current conveyor) value of the expected movement from its children.

#### populateConveyorMovementExpectations(conveyors)

*Given a sorted list of conveyors with conveyor-child relationship information already populated, populates conveyor objects with the expected horizontal movement of the package on the conveyor, assuming the conveyor operates in either direction, as well as the probability that the package lands on the conveyor.*

Go through the conveyors in order and determine the probability that a probability that the package falls directly on the conveyor. Add this probability to the probability that it falls from another conveyor onto the current conveyor and use it to update the probability that either of its child conveyors has the package land on it from the current conveyor. 

#### getOverlappingIntervals(intervals, x1, x2)

*Given a sorted list of intervals (with a start and end value) ```intervals```, returns a subset of the intervals that overlap the interval (x1, x2).*

Implementation is fairly straightforward.

### Key Insights and Optimizations

- TODO