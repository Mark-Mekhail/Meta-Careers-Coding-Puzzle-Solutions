from typing import List

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    discRadiusDiffs = [0] * N  # Difference between a disc's starting radius and its current radius
    chainIntervalStarts = [0]  # Start indices of intervals of discs with radii within 1 of adjacent discs in the interval
    for i in range(1, N):
        # Inflate the ith disc if it is smaller than the previous disc
        minDiscInflationNeeded = R[i - 1] + 1 - R[i]
        if minDiscInflationNeeded >= 0:
            R[i] += minDiscInflationNeeded
            discRadiusDiffs[i] = minDiscInflationNeeded
        else:
            # The ith disc is in a chain interval by itself
            chainIntervalStarts.append(i)
        
        # Deflate all discs in the chain interval containing the ith disc as long as it saves total cost
        while True:
            curIntervalStartDisc = chainIntervalStarts[-1]
            curIntervalSize = i + 1 - curIntervalStartDisc

            posDiffs = [diff for diff in discRadiusDiffs[curIntervalStartDisc: i + 1] if diff > 0]
            if not posDiffs:
                # No discs in the chain interval are inflated so it's pointless to deflate
                break

            posDiffCount = len(posDiffs)
            negDiffCount = curIntervalSize - posDiffCount

            # The amount we can deflate at the same cost/savings per deflation is min diff of current interval and diff between current interval and previous interval
            minPosDiff = min(posDiffs)
            minPosDiff = min(minPosDiff, ((R[curIntervalStartDisc] - R[curIntervalStartDisc - 1]) if curIntervalStartDisc > 0 else R[0]) - 1)

            # Cost change is cost of deflating what is not inflated minus savings from deflating what was inflated
            costChange = (negDiffCount * B - posDiffCount * A) * minPosDiff  
            if costChange >= 0:
                # If we cease to save cost by deflating, stop deflating
                break

            # Update the radii all of discs in a chain interval with the ith disc
            for j in range(curIntervalStartDisc, i + 1):
                discRadiusDiffs[j] -= minPosDiff
                R[j] -= minPosDiff

            # Merge the current interval with the previous interval if needed
            if curIntervalStartDisc > 0 and R[curIntervalStartDisc] == R[curIntervalStartDisc - 1] + 1:
                chainIntervalStarts.pop()

    # Calculate the total cost of inflating and deflating discs
    return sum([diff * A if diff > 0 else abs(diff * B) for diff in discRadiusDiffs])