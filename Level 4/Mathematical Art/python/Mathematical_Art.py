from typing import List
from sortedcontainers import SortedKeyList, SortedList
  

def getPlusSignCount(N: int, L: List[int], D: str) -> int:
    verticalLines, horizontalLines = getLineInfo(N, L, D)
    horizontalLineList = []
    for y in horizontalLines:
        for line in horizontalLines[y]:
            horizontalLineList.append((line[0], line[1], y))
    
    horizontalsByStart = sorted(horizontalLineList, key=lambda x: x[0])
    horizontalsByEnd = sorted(horizontalLineList, key=lambda x: x[1])
    
    plusSignCount = 0
    horizontalIndices = [0, 0]
    horizontalYs = SortedList()
    for x in sorted(verticalLines.keys()):
        lastHorizontalIndex = horizontalIndices[1]
        if lastHorizontalIndex < len(horizontalsByStart):
            lastHorizontal = horizontalsByStart[lastHorizontalIndex]
            while lastHorizontal[0] < x:
                horizontalYs.add(lastHorizontal[2])
                lastHorizontalIndex += 1
                if lastHorizontalIndex == len(horizontalsByStart):
                    break
                lastHorizontal = horizontalsByStart[lastHorizontalIndex]
            horizontalIndices[1] = lastHorizontalIndex

        firstHorizontalIndex = horizontalIndices[0]
        if firstHorizontalIndex < len(horizontalsByEnd):
            firstHorizontal = horizontalsByEnd[firstHorizontalIndex]
            while firstHorizontal[1] <= x:
                horizontalYs.remove(firstHorizontal[2])
                firstHorizontalIndex += 1
                if firstHorizontalIndex == len(horizontalsByEnd):
                    break
                firstHorizontal = horizontalsByEnd[firstHorizontalIndex]
            horizontalIndices[0] = firstHorizontalIndex

        for line in verticalLines[x]:
            start, end = line

            first = horizontalYs.bisect_right(start)
            last = horizontalYs.bisect_left(end)

            plusSignCount += last - first

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