from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    maxExpectedProfit = [0] * (N + 1)
    
    # For each day i, calculate the maximum expected profit if only days i to N are considered
    for i in range(N - 1, -1, -1):
        expectedMailValue = 0
        for j in range(i, N):
            # Calculate the expected value of mail in the mailroom assuming that mail was last collected on day i - 1
            expectedMailValue = (1 - S) * expectedMailValue + V[j]

            # Calculate the expected profit if mail is collected on day j
            maxExpectedProfitIfCollected = expectedMailValue - C + maxExpectedProfit[j + 1]
            if maxExpectedProfitIfCollected > maxExpectedProfit[i]:
                maxExpectedProfit[i] = maxExpectedProfitIfCollected
    
    return maxExpectedProfit[0]
