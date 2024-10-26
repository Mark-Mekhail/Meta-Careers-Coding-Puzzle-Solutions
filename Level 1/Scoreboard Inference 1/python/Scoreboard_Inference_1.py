from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    max_score = -1
    contains_odd = False
    
    for score in S:
        if score > max_score:
            max_score = score
        contains_odd = contains_odd or (score % 2 == 1)
    
    return max_score // 2 + (1 if contains_odd else 0)