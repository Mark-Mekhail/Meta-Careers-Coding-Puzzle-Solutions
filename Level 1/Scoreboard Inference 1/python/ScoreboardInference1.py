from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    maxScore = -1
    containsOdd = False
    
    for score in S:
        if score > maxScore:
            maxScore = score
        containsOdd = containsOdd or (score % 2 == 1)
    
    return maxScore // 2 + (1 if containsOdd else 0)