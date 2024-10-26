from typing import List
import math

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    
    first_frog_index = P[0]
    seconds = 0
    
    i = 1
    while i < F:
        next_frog_index = P[i]
        dist_to_next_frog = next_frog_index - (first_frog_index + i - 1)
        hops_to_next_frog = math.ceil(dist_to_next_frog / i)
        seconds += hops_to_next_frog * i + next_frog_index - (first_frog_index + hops_to_next_frog * i)
        first_frog_index = next_frog_index
        
        while i + 1 < F and P[i + 1] < first_frog_index + i:
            next_frog_index = P[i + 1]
            i += 1
        
        i += 1
    
    dist_to_end = N - (first_frog_index + F - 1)
    hops_to_end = math.ceil(dist_to_end / F) if dist_to_end > 0 else 0
    seconds += hops_to_end * F + N - (first_frog_index + hops_to_end * F)
    
    return seconds
