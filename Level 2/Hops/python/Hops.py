from typing import List
import math

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    
    first_frog_index = P[0]
    seconds = 0
    
    i = 1
    while i < F:
        seconds += P[i] - first_frog_index
        first_frog_index = P[i]
        
        while i + 1 < F and P[i + 1] < first_frog_index + i:
            i += 1
        
        i += 1
    
    seconds += N - first_frog_index
    
    return seconds
