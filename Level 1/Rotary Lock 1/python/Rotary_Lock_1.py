from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    time = 0
    prev = 1
    
    for i in range(M):
        digit = C[i]
        time += min(abs(digit - prev), N + min(prev, digit) - max(prev, digit))
        prev = digit
    
    return time