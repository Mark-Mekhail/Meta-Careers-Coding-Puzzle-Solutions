from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    deflatedDiscCount = 0
    
    for i in range(N - 2, -1, -1):
        # If the current disc is bigger than the next disc, deflate the current disc to the size of the next disc minus 1
        if R[i] >= R[i + 1]:
            R[i] = R[i + 1] - 1
            if R[i] == 0:
                return -1
            deflatedDiscCount += 1
    
    return deflatedDiscCount