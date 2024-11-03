from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    
    firstFrogPos = P[0]
    secondsRequired = 0
    for i in range(1, F):
        # If the current frog is ahead of the chain of frogs connected to the first frog, add the time for all frogs in the chain hop over the current frog
        if P[i] > firstFrogPos + i:
            secondsRequired += P[i] - firstFrogPos
            firstFrogPos = P[i]

    # Add the time needed for all remaining frogs to hop to shore
    secondsRequired += N - firstFrogPos
    
    return secondsRequired
