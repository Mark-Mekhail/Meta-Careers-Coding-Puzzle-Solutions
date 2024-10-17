from typing import List
from sortedcontainers import SortedList, SortedKeyList
import math

CENTER_WIDTH = 1_000_000

class Conveyor:
    def __init__(self, x1, x2, h):
        self.x1 = x1
        self.x2 = x2
        self.h = h
        self.leftChild = None
        self.rightChild = None
        self.expectedPackages = 0
        self.expectedLeftHorizontal = 0
        self.expectedRightHorizontal = 0
        self.expectedHorizontalMultiplier = None

    def __lt__(self, other):
        return self.h < other.h
    
    def __repr__(self):
        return f"(left: {self.x1}, right: {self.x2}, height: {self.h}, packages: {self.expectedPackages}, movementMultiplier: {self.expectedHorizontalMultiplier})"


def getMinExpectedHorizontalTravelDistance(N: int, H: List[int], A: List[int], B: List[int]) -> float:
    conveyors = getSortedConveyors(N, H, A, B)
    populateConveyorRelationships(conveyors)
    populateConveyorExpectedHorizontals(conveyors)
    populateRemainingConveyorInfo(conveyors)

    expectedHorizontalMovement = 0
    bestOrientationDiff = 0
    for conveyor in conveyors:
        expectedHorizontalMovement += conveyor.expectedPackages * (conveyor.x2 - conveyor.x1) / 2

        conveyorContribution = conveyor.expectedPackages * conveyor.expectedHorizontalMultiplier
        leftOnlyContribution = conveyor.expectedLeftHorizontal
        if conveyor.leftChild:
            leftOnlyContribution += conveyor.leftChild.expectedHorizontalMultiplier * conveyor.expectedPackages

        rightOnlyContribution = conveyor.expectedRightHorizontal
        if conveyor.rightChild:
            rightOnlyContribution += conveyor.rightChild.expectedHorizontalMultiplier * conveyor.expectedPackages  

        bestOrientationDiff = max(bestOrientationDiff, conveyorContribution - leftOnlyContribution, conveyorContribution - rightOnlyContribution)

    result = (expectedHorizontalMovement - bestOrientationDiff) / CENTER_WIDTH
    
    return result


def populateRemainingConveyorInfo(conveyors):
    packageDropIntervals = SortedKeyList([(0, CENTER_WIDTH)], key=lambda x: x[0])
    dropoffPoints = SortedList([])
    expectedPackagesAtDropoffs = {}
    for conveyor in conveyors:
        x1, x2 = conveyor.x1, conveyor.x2

        overlappingRanges = getOverlappingRanges(packageDropIntervals, x1, x2)
        for interval in overlappingRanges:
            packageDropIntervals.remove(interval)

            intervalStart, intervalEnd = interval

            if intervalStart < x1:
                prevInterval = (intervalStart, x1)
                packageDropIntervals.add(prevInterval)
                intervalStart = x1
            
            if intervalEnd > x2:
                nextInterval = (x2, intervalEnd)
                packageDropIntervals.add(nextInterval)
                intervalEnd = x2

            intervalSize = intervalEnd - intervalStart
            intervalMidPoint = (intervalStart + intervalEnd) / 2

            conveyor.expectedPackages += intervalSize
            conveyor.expectedLeftHorizontal += intervalSize * (intervalMidPoint - x1)
            conveyor.expectedRightHorizontal += intervalSize * (x2 - intervalMidPoint)

        overlappingDropoffPoints = list(dropoffPoints.irange(x1, x2, inclusive=(False, False)))
        for dropoffPoint in overlappingDropoffPoints:
            dropoffPoints.remove(dropoffPoint)
            expectedPackagesAtDropoff = expectedPackagesAtDropoffs.pop(dropoffPoint)
            conveyor.expectedPackages += expectedPackagesAtDropoff

            conveyor.expectedLeftHorizontal += expectedPackagesAtDropoff * abs(dropoffPoint - x1)
            conveyor.expectedRightHorizontal += expectedPackagesAtDropoff * abs(x2 - dropoffPoint)

        if x1 not in expectedPackagesAtDropoffs:
            dropoffPoints.add(x1)
            expectedPackagesAtDropoffs[x1] = 0
        
        if x2 not in expectedPackagesAtDropoffs:
            dropoffPoints.add(x2)
            expectedPackagesAtDropoffs[x2] = 0
        
        expectedPackagesAtDropoffs[x1] += conveyor.expectedPackages / 2
        expectedPackagesAtDropoffs[x2] += conveyor.expectedPackages / 2
    

def populateConveyorRelationships(conveyors):
    endpointParents = {}  # Tracks the conveyors that each endpoint is currently a part of
    endpoints = SortedList()  # Tracks the endpoints of processed conveyors that have not yet reached a child conveyor
    for conveyor in conveyors:
        x1, x2 = conveyor.x1, conveyor.x2
        
        endpointsInConveyor = set(endpoints.irange(x1, x2, inclusive=(False, False)))
        for endpoint in endpointsInConveyor:
            for parent in endpointParents.pop(endpoint):
                if endpoint == parent.x1:
                    parent.leftChild = conveyor
                else:
                    parent.rightChild = conveyor
            endpoints.remove(endpoint)

        if x1 not in endpoints:
            endpoints.add(x1)
            endpointParents[x1] = set()
        
        if x2 not in endpoints:
            endpoints.add(x2)
            endpointParents[x2] = set()

        endpointParents[x1].add(conveyor)
        endpointParents[x2].add(conveyor)


def populateConveyorExpectedHorizontals(conveyors):
    for conveyor in reversed(conveyors):
        conveyor.expectedHorizontalMultiplier = (conveyor.x2 - conveyor.x1) / 2

        if conveyor.leftChild:
            conveyor.expectedHorizontalMultiplier += conveyor.leftChild.expectedHorizontalMultiplier / 2

        if conveyor.rightChild:
            conveyor.expectedHorizontalMultiplier += conveyor.rightChild.expectedHorizontalMultiplier / 2



def getSortedConveyors(N, H, A, B):
    conveyors = [Conveyor(A[i], B[i], H[i]) for i in range(N)]
    conveyors.sort(reverse=True)
    return conveyors


def getOverlappingRanges(possiblePackageRanges, x1, x2):
    lastOverlappingRangeIndex = possiblePackageRanges.bisect_key_left(x2)
    firstOverlappingRangeIndex = max(possiblePackageRanges.bisect_key_left(x1) - 1, 0)
    while firstOverlappingRangeIndex < lastOverlappingRangeIndex and possiblePackageRanges[firstOverlappingRangeIndex][1] <= x1:
        firstOverlappingRangeIndex += 1

    return list(possiblePackageRanges.islice(firstOverlappingRangeIndex, lastOverlappingRangeIndex))