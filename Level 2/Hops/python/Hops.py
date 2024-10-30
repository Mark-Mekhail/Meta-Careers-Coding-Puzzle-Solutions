from typing import List
import math

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    
    first_frog_index = P[0]
    seconds = 0
    for i in range(F):
        if P[i] > first_frog_index + i:
            seconds += P[i] - first_frog_index
            first_frog_index = P[i]
    seconds += N - first_frog_index
    
    return seconds
