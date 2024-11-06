from typing import Iterable, List, Tuple
from sortedcontainers import SortedKeyList, SortedList

CENTER_WIDTH = 1_000_000

# Class representing a conveyor belt
class Conveyor:
    x1: int                       # Left endpoint of the conveyor
    x2: int                       # Right endpoint of the conveyor
    h: int                        # Height of the conveyor
    leftChild: 'Conveyor'         # The conveyor that the package will land on if dropped on the left side of this conveyor
    rightChild: 'Conveyor'        # The conveyor that the package will land on if dropped on the right side of this conveyor
    packageDropProbability: int   # The probability that the package will land on this conveyor assuming all conveyors above it run in a random direction
    expectedLeftHorizontal: int   # The expected horizontal distance that the package will travel on this conveyor if it runs to the left
    expectedRightHorizontal: int  # The expected horizontal distance that the package will travel on this conveyor if it runs to the right
    expectedHorizontal: int       # The expected horizontal distance that the package will travel if dropped on this conveyor

    def __init__(self, x1, x2, h):
        self.x1                      = x1
        self.x2                      = x2
        self.h                       = h
        self.leftChild               = None
        self.rightChild              = None
        self.packageDropProbability  = 0
        self.expectedLeftHorizontal  = 0
        self.expectedRightHorizontal = 0
        self.expectedHorizontal      = None

    # The natural ordering of conveyors is by height in non-ascending order
    def __lt__(self, other):
        return self.h > other.h

def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
    # Sort the conveyors by height in non-ascending order
    conveyors = SortedList([Conveyor(A[i], B[i], H[i]) for i in range(N)])

    populateConveyorRelationships(conveyors)
    populateConveyorExpectedHorizontals(conveyors)
    populateConveyorMovementExpectations(conveyors)

    expectedHorizontalMovement = 0  # Track the total expected horizontal movement of the package assuming all conveyor directions are random
    bestPossibleMovementReduction = 0  # Track the best possible reduction in expected horizontal movement if any single conveyor's direction is set to the optimal direction
    for conveyor in conveyors:
        # Expected horizontal movement of the package on the current conveyor is half the width of the conveyor
        expectedHorizontalMovement += conveyor.packageDropProbability * (conveyor.x2 - conveyor.x1) / 2

        # Calculate the expected horizontal movement of the package if the conveyor is set to run in a random direction
        expectedHorizontalMovementFromConveyor = conveyor.packageDropProbability * conveyor.expectedHorizontal

        # Calculate the expected horizontal movement of the package if the conveyor is set to either direction
        expectedMovementWhenRunningLeft = conveyor.expectedLeftHorizontal
        if conveyor.leftChild:
            expectedMovementWhenRunningLeft += conveyor.leftChild.expectedHorizontal * conveyor.packageDropProbability

        expectedMovementWhenRunningRight = conveyor.expectedRightHorizontal
        if conveyor.rightChild:
            expectedMovementWhenRunningRight += conveyor.rightChild.expectedHorizontal * conveyor.packageDropProbability  

        # Update the best possible reduction in expected horizontal movement, which is the biggest difference in expected horizontal movement when the conveyor is set to run in a random direction and when it is set to run in either direction
        bestPossibleMovementReduction = max(bestPossibleMovementReduction, expectedHorizontalMovementFromConveyor - min(expectedMovementWhenRunningLeft, expectedMovementWhenRunningRight))
    
    # Return the expected horizontal movement of the package minus the best possible reduction in expected horizontal movement by setting a single conveyor's direction to the optimal direction
    return expectedHorizontalMovement - bestPossibleMovementReduction


def populateConveyorMovementExpectations(conveyors: SortedList):
    packageDropIntervals = SortedKeyList([(0, CENTER_WIDTH)], key=lambda x: x[0])  # Tracks the intervals that a higher conveyor has not yet covered
    dropoffPoints = SortedList([])  # Tracks the conveyor endpoints that a higher conveyor has not yet overlapped
    packageProbabilityAtDropoffs = {}  # Maps a dropoff point to the probability that a package will be dropped at that point
    for conveyor in conveyors:
        x1, x2 = conveyor.x1, conveyor.x2

        # Go through all uncovered intervals that the current conveyor overlaps with
        for interval in list(getOverlappingIntervals(packageDropIntervals, x1, x2)):
            intervalStart, intervalEnd = interval

            if intervalStart < x1:
                # If the interval starts before the current conveyor, split the interval into two intervals
                prevInterval = (intervalStart, x1)
                packageDropIntervals.add(prevInterval)
                intervalStart = x1
            
            if intervalEnd > x2:
                # If the interval ends after the current conveyor, split the interval into two intervals
                nextInterval = (x2, intervalEnd)
                packageDropIntervals.add(nextInterval)
                intervalEnd = x2

            intervalPackageProbability = (intervalEnd - intervalStart) / CENTER_WIDTH  # The probability that a package will be dropped in the current interval
            intervalMidPoint = (intervalStart + intervalEnd) / 2

            conveyor.packageDropProbability += intervalPackageProbability

            # Update the expected horizontal distance that the package will travel on the current conveyor to account for a random drop within the current interval
            conveyor.expectedLeftHorizontal += intervalPackageProbability * (intervalMidPoint - x1)
            conveyor.expectedRightHorizontal += intervalPackageProbability * (x2 - intervalMidPoint)

            packageDropIntervals.remove(interval)

        # Go through all dropoff points that the current conveyor overlaps
        for dropoffPoint in list(dropoffPoints.irange(x1, x2, inclusive=(False, False))):
            # Add the probability that a package will be dropped at the current dropoff point to the current conveyor's package drop probability
            packageProbabilityAtDropoff = packageProbabilityAtDropoffs.pop(dropoffPoint)
            conveyor.packageDropProbability += packageProbabilityAtDropoff

            # Update the expected horizontal distance that the package will travel if the conveyor runs in either direction to account for the probability that a package will land from the current dropoff point
            conveyor.expectedLeftHorizontal += packageProbabilityAtDropoff * abs(dropoffPoint - x1)
            conveyor.expectedRightHorizontal += packageProbabilityAtDropoff * abs(x2 - dropoffPoint)

            dropoffPoints.remove(dropoffPoint)

        # Add the endpoints of the current conveyor to the list of dropoff points if they are not already in the list
        if x1 not in packageProbabilityAtDropoffs:
            dropoffPoints.add(x1)
            packageProbabilityAtDropoffs[x1] = 0
        
        if x2 not in packageProbabilityAtDropoffs:
            dropoffPoints.add(x2)
            packageProbabilityAtDropoffs[x2] = 0
        
        # The probability that a package will fall off each endpoint of the current conveyor is half the probability that a package will be dropped on the current conveyor
        packageProbabilityAtDropoffs[x1] += conveyor.packageDropProbability / 2
        packageProbabilityAtDropoffs[x2] += conveyor.packageDropProbability / 2
    
# Given a list of conveyors sorted by height in non-ascending order, populates the parent-child relationships between conveyors
def populateConveyorRelationships(conveyors: SortedList):
    endpointParents = {}      # Maps an endpoint location to the conveyors with an endpoint at that location that have not yet been assigned a child conveyor
    endpoints = SortedList()  # Tracks the endpoints of higher conveyors that have not yet reached a child conveyor
    for conveyor in conveyors:
        x1, x2 = conveyor.x1, conveyor.x2
        
        # Go through all endpoints that the current conveyor overlaps with
        for endpoint in list(endpoints.irange(x1, x2, inclusive=(False, False))):
            # Assign the current conveyor as a child of the conveyors above it with the current endpoint that have not yet been assigned a child conveyor
            for parent in endpointParents.pop(endpoint):
                if endpoint == parent.x1:
                    parent.leftChild = conveyor
                else:
                    parent.rightChild = conveyor

            # Now that the current conveyor has been assigned as a child conveyor, remove the endpoint from the list of endpoints that have not yet reached a child conveyor
            endpoints.remove(endpoint)

        # Add the endpoints of the current conveyor to the list of endpoints that have not yet reached a child conveyor
        if x1 not in endpoints:
            endpoints.add(x1)
            endpointParents[x1] = set()
        
        if x2 not in endpoints:
            endpoints.add(x2)
            endpointParents[x2] = set()

        # Add the current conveyor to the list of conveyors with an endpoint at the current endpoint that have not yet been assigned a child conveyor
        endpointParents[x1].add(conveyor)
        endpointParents[x2].add(conveyor)

# Given a list of conveyors sorted by height in non-ascending order, populates the expected horizontal distance that a package will travel when dropped on each conveyor
def populateConveyorExpectedHorizontals(conveyors: SortedList):
    for conveyor in reversed(conveyors):
        # The expected horizontal distance that the package will travel on the current conveyor is half the width of the conveyor
        conveyor.expectedHorizontal = (conveyor.x2 - conveyor.x1) / 2

        # The expected horizontal distance that the package will travel must account for the expected horizontal distance that the package will travel on its children conveyors
        if conveyor.leftChild:
            conveyor.expectedHorizontal += conveyor.leftChild.expectedHorizontal / 2

        if conveyor.rightChild:
            conveyor.expectedHorizontal += conveyor.rightChild.expectedHorizontal / 2

# Given a list of non-overlapping intervals sorted by their start points, returns an iterable of the intervals that overlap with the range (x1, x2)
def getOverlappingIntervals(intervals: SortedKeyList, x1: int, x2: int) -> Iterable[Tuple[int, int]]:
    lastOverlappingIntervalIndex = intervals.bisect_key_left(x2)  # The index of the interval with the first start point greater than or equal to max

    # The index of the first interval that overlaps min, or the first interval that starts after min if no intervals overlap min
    firstOverlappingIntervalIndex = max(intervals.bisect_key_left(x1) - 1, 0)
    if firstOverlappingIntervalIndex < lastOverlappingIntervalIndex and intervals[firstOverlappingIntervalIndex][1] <= x1:
        firstOverlappingIntervalIndex += 1

    return intervals.islice(firstOverlappingIntervalIndex, lastOverlappingIntervalIndex)