from typing import List
import math

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    # A is inflation cost, B is deflation cost
    cost = 0
    diffs = [0] * N
    intervals = [0] # start indices of intervals
    for i in range(1, N):
        # inflate
        neededSizeDiff = R[i - 1] + 1 - R[i]
        if neededSizeDiff >= 0:
            cost += neededSizeDiff * A
            R[i] += neededSizeDiff
            diffs[i] = neededSizeDiff
        else:
            intervals.append(i)
        
        # deflate as long as we save cost
        while True:
            curIntervalStart = intervals[-1]
            intervalSize = i + 1 - curIntervalStart

            # count positive and negative diffs
            posDiffs = [diff for diff in diffs[curIntervalStart: i + 1] if diff > 0]
            posDiffCount = len(posDiffs)
            negDiffCount = intervalSize - posDiffCount
            minPosDiff = min(posDiffs) if posDiffs else math.inf
            minPosDiff = min(minPosDiff, ((R[curIntervalStart] - R[curIntervalStart - 1]) if curIntervalStart > 0 else R[0]) - 1) # minimum amount we can deflate at same cost is min diff of current interval and diff between current interval and previous interval

            costChange = (negDiffCount * B - posDiffCount * A) * minPosDiff  # cost change is cost of deflating what is not inflated minus savings from deflating what was inflated
            if costChange >= 0:
                break  # if we cease to save cost by deflating, stop deflating

            # apply cost change
            cost += costChange

            # deflate
            for j in range(curIntervalStart, i + 1):
                diffs[j] -= minPosDiff
                R[j] -= minPosDiff

            # merge current interval with previous interval if needed
            if curIntervalStart > 0 and R[curIntervalStart] == R[curIntervalStart - 1] + 1:
                intervals.pop()

    return cost