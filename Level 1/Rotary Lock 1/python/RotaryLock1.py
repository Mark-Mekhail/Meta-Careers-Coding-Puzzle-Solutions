from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    codeEntryTime = 0
    lockPos = 1
    for i in range(M):
        digit = C[i]

        # Get the time to rotate the lock to the next digit and update the lock position
        codeEntryTime += getRotationTime(N, lockPos, digit)
        lockPos = digit
    
    return codeEntryTime

def getRotationTime(N: int, startDigit: int, endDigit: int) -> int:
    return min(abs(endDigit - startDigit), N + min(startDigit, endDigit) - max(startDigit, endDigit))