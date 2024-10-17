from typing import List
from sortedcontainers import SortedKeyList, SortedList
import bisect

# VERTICAL = "V"
# HORIZONTAL = "H"

# class Line:
#     def __init__(self, x, y, L, D):
#         if D == "D":
#             self.bottomLeft = (x, y - L)
#         elif D == "L":
#             self.bottomLeft = (x - L, y)
#         else:
#             self.bottomLeft = (x, y)

#         self.length = L
#         self.direction = VERTICAL if (D == "U" or D == "D") else HORIZONTAL
  

def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    verticalLines, horizontalLines = getLineInfo(N, L, D)
    horizontalYs = sorted(horizontalLines.keys())
    numHorizontalYs = len(horizontalYs)

    # print(verticalLines)
    # print(horizontalLines)
    plusSignCount = 0
    for x in verticalLines:
        for verticalLine in verticalLines[x]:
            bottomY, topY = verticalLine
            
            if topY - bottomY > 1:
                yIndex = bisect.bisect_right(horizontalYs, bottomY)
                while yIndex < numHorizontalYs and horizontalYs[yIndex] < topY:
                    y = horizontalYs[yIndex]
                    yIndex += 1

                    linesOnY = horizontalLines[y]
                    if linesOnY[0][0] >= x or linesOnY[-1][1] <= x:
                        continue

                    lastLineUpToY = linesOnY[max(linesOnY.bisect_key_left(x) - 1, 0)]

                    if lastLineUpToY[0] < x and lastLineUpToY[1] > x:
                        plusSignCount += 1

    return plusSignCount


def getLineInfo(N, L, D):
    curPos = [0, 0]
    verticalLines = {}  # Maps x-coordinate to a list of vertical lines on that x-coordinate
    horizontalLines = {}  # Maps y-coordinate to a list of horizontal lines on that y-coordinate

    maxX, maxY = 0, 0
    minX, minY = 0, 0
    for i in range(N):
        if i < N - 1 and D[i+1] == D[i]:
            L[i+1] += L[i]
            continue

        curX, curY = curPos
        nextX, nextY = getNextEndpoint(curPos, L[i], D[i])

        if nextX == curX:
            if curX not in verticalLines:
                verticalLines[curX] = SortedKeyList(key=lambda x: x[0])
                
            inlineLines = verticalLines[curX]
            mergedLineStart = min(curY, nextY)
            mergedLineEnd = max(curY, nextY)
            for line in getOverlappingLines(mergedLineStart, mergedLineEnd, inlineLines):
                inlineLines.remove(line)

                if line[0] < mergedLineStart:
                    mergedLineStart = line[0]
                
                if line[1] > mergedLineEnd:
                    mergedLineEnd = line[1]

            inlineLines.add((mergedLineStart, mergedLineEnd))
            
        else:
            if curY not in horizontalLines:
                horizontalLines[curY] = SortedKeyList(key=lambda x: x[0])
                
            inlineLines = horizontalLines[curY]
            mergedLineStart = min(curX, nextX)
            mergedLineEnd = max(curX, nextX)
            for line in getOverlappingLines(mergedLineStart, mergedLineEnd, inlineLines):
                inlineLines.remove(line)

                if line[0] < mergedLineStart:
                    mergedLineStart = line[0]
                
                if line[1] > mergedLineEnd:
                    mergedLineEnd = line[1]

            inlineLines.add((mergedLineStart, mergedLineEnd))

        curPos[0], curPos[1] = nextX, nextY
        maxX = max(maxX, nextX)
        maxY = max(maxY, nextY)
        minX = min(minX, nextX)
        minY = min(minY, nextY)

    if maxX in verticalLines:
        del verticalLines[maxX]
    
    if maxY in horizontalLines:
        del horizontalLines[maxY]
    
    if minX in verticalLines:
        del verticalLines[minX]

    if minY in horizontalLines:
        del horizontalLines[minY]

    return verticalLines, horizontalLines


def getNextEndpoint(curPos, L, D):
    if D == "U":
        return (curPos[0], curPos[1] + L)
    elif D == "D":
        return (curPos[0], curPos[1] - L)
    elif D == "L":
        return (curPos[0] - L, curPos[1])
    else:
        return (curPos[0] + L, curPos[1])


def getOverlappingLines(low: int, high: int, lines: SortedKeyList):
    lastOverlappingIndex = lines.bisect_key_right(high)
    firstOverlappingIndex = max(lines.bisect_key_left(low) - 1, 0)
    if firstOverlappingIndex < lastOverlappingIndex and lines[firstOverlappingIndex][1] < low:
        firstOverlappingIndex += 1

    return set(lines.islice(firstOverlappingIndex, lastOverlappingIndex))

