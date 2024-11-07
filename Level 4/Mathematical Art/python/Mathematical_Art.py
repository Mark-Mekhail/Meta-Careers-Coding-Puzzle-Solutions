from typing import Callable, List, Tuple
from sortedcontainers import SortedKeyList, SortedList

# A class representing a line with a fixed coordinate and a start and end coordinate for the other axis
class Line:
    start: int       # The start coordinate of the line
    end: int         # The end coordinate of the line
    fixedCoord: int  # The coordinate that is fixed for this line

    def __init__(self, start: int, end: int, fixedCoord: int):
        self.start = start
        self.end = end
        self.fixedCoord = fixedCoord

    # Natural order is based on the fixed coordinate and then the start coordinate
    def __lt__(self, other):
        if self.fixedCoord != other.fixedCoord:
            return self.fixedCoord < other.fixedCoord
        else:
            return self.start < other.start
  
def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    # Get the sorted lists of horizontal and vertical stroke lines
    verticalStrokeLines, horizontalStrokeLines = getStrokeLines(N, L, D)

    # Get the sorted (by various measures) lists of merged vertical and horizontal lines
    verticalsSortedByXCoord = getSortedMergedLineList(verticalStrokeLines, key=lambda line: line.fixedCoord)
    horizontalsSortedByStart = getSortedMergedLineList(horizontalStrokeLines, key=lambda line: line.start)
    horizontalsSortedByEnd = SortedKeyList(horizontalsSortedByStart, key=lambda line: line.end)
    
    numHorizontalLines = len(horizontalsSortedByStart)
    
    lastOverlappingHorizontalIndex = 0  # The index following the last horizontal line in horizontalLinesByStart found to overlap a given increasing x-coordinate
    firstOverlappingHorizontalIndex = 0  # The index following the first horizontal line in horizontalLinesByEnd found to overlap a given increasing x-coordinate
    overlappingHorizontalYCoords = SortedList()  # The y-coordinates of horizonal lines that overlap a given increasing x-coordinate
    plusSignCount = 0
    for verticalLine in verticalsSortedByXCoord:
        # Update the list of y-coordinates of horizontal lines to include any lines that overlap the x-coordinate of the current vertical line but do not overlap that of the previous vertical line
        if lastOverlappingHorizontalIndex < numHorizontalLines:
            lastOverlappingHorizontal = horizontalsSortedByStart[lastOverlappingHorizontalIndex]

            while lastOverlappingHorizontal.start < verticalLine.fixedCoord:
                # Add the y-coordinate of the next horizontal line that overlaps the x-coordinate of the current vertical line 
                overlappingHorizontalYCoords.add(lastOverlappingHorizontal.fixedCoord)
                lastOverlappingHorizontalIndex += 1
                if lastOverlappingHorizontalIndex == numHorizontalLines:
                    break
                lastOverlappingHorizontal = horizontalsSortedByStart[lastOverlappingHorizontalIndex]

        # Update the list of y-coordinates of horizontal lines to exclude any lines that overlap the x-coordinate of the previous vertical line but do not overlap that of the current vertical line
        if firstOverlappingHorizontalIndex < numHorizontalLines:
            firstOverlappingHorizontal = horizontalsSortedByEnd[firstOverlappingHorizontalIndex]

            while firstOverlappingHorizontal.end <= verticalLine.fixedCoord:
                # Remove the y-coordinate of the next horizontal line that no longer overlaps the x-coordinate of the current vertical line
                overlappingHorizontalYCoords.remove(firstOverlappingHorizontal.fixedCoord)
                firstOverlappingHorizontalIndex += 1
                if firstOverlappingHorizontalIndex == numHorizontalLines:
                    break
                firstOverlappingHorizontal = horizontalsSortedByEnd[firstOverlappingHorizontalIndex]

        # Update the count of plus signs based on the number of horizontal lines that overlap the current vertical line
        plusSignCount += overlappingHorizontalYCoords.bisect_left(verticalLine.end) - overlappingHorizontalYCoords.bisect_right(verticalLine.start)

    return plusSignCount

# Returns a tuple of two sorted (according to natural order) lists containing the horizontal and vertical stroke lines, respectively
def getStrokeLines(N: int, L: List[int], D: str) -> Tuple[SortedList, SortedList]:
    horizontalStrokeLines = SortedList()
    verticalStrokeLines = SortedList()

    brushPos = (0,0)
    for i in range(N):
        if i < N - 1 and D[i+1] == D[i]:
            # If the next stroke is in the same direction, just add the length of the current stroke to that of the next stroke and move on to the next stroke
            L[i+1] += L[i]
            continue

        prevBrushPos = brushPos
        brushPos = getStrokeEndpoint(brushPos, L[i], D[i])

        # Create and add the new line to the appropriate list based on the orientation of the stroke
        if prevBrushPos[0] == brushPos[0]:
            verticalStrokeLines.add(Line(min(prevBrushPos[1], brushPos[1]), max(prevBrushPos[1], brushPos[1]), prevBrushPos[0]))
        else:
            horizontalStrokeLines.add(Line(min(prevBrushPos[0], brushPos[0]), max(prevBrushPos[0], brushPos[0]), prevBrushPos[1]))

    return horizontalStrokeLines, verticalStrokeLines

# Given a sorted (by natural order) list of lines with the same orientation, returns a list of lines with overlapping/touching lines merged sorted by the given key
def getSortedMergedLineList(lines: SortedList, key: Callable[[Line], int]) -> SortedKeyList:
    mergedLines = SortedKeyList(key=key)

    curMergedLine = Line(lines[0].start, lines[0].end, lines[0].fixedCoord)  # Tracks the resulting line after merging overlapping lines
    for i in range(1, len(lines)):
        nextLine = lines[i]

        if curMergedLine.fixedCoord != nextLine.fixedCoord or curMergedLine.end < nextLine.start:
            # If there are no more lines that overlap with the current merged line, add the current merged line to the list of merged lines and set parameters for the next merged line
            mergedLines.add(curMergedLine)
            curMergedLine = Line(nextLine.start, nextLine.end, nextLine.fixedCoord)
        else:
            # Update the end coordinate of the current merged line
            curMergedLine.end = max(curMergedLine.end, nextLine.end)

    # Add the last merged line to the list of merged lines
    mergedLines.add(curMergedLine)

    return mergedLines

# Given the current position, the length of the stroke, and the direction of the stroke, returns the endpoint of the stroke
def getStrokeEndpoint(brushPos: Tuple[int, int], strokeLen: int, strokeDir: str) -> Tuple[int, int]:
    if strokeDir == "U":
        return (brushPos[0], brushPos[1] + strokeLen)
    elif strokeDir == "D":
        return (brushPos[0], brushPos[1] - strokeLen)
    elif strokeDir == "L":
        return (brushPos[0] - strokeLen, brushPos[1])
    else:
        return (brushPos[0] + strokeLen, brushPos[1])