from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    codeIntegers = set(C)
    codeIntegers.add(1)
    
    # Create a dictionary to store the minimum time to enter the code from given lock positions
    codeEntryTimesFromPos = {codeInteger: 0 for codeInteger in codeIntegers}

    for i in range(M - 1, -1, -1):
        curCodeInteger = C[i]
        prevCodeInteger = C[i - 1] if i > 0 else 1
        
        prevToCurRotationTime = getRotationTime(N, prevCodeInteger, curCodeInteger)
        
        codeEntryTimesFromPrev = {}
        for codeInteger in codeIntegers:
            # Calculate the minimum time needed to enter the code integers from i to M from a given lock position where locks are at positions prevCodeInteger and codeInteger
            codeEntryTimesFromPrev[codeInteger] = min(prevToCurRotationTime + codeEntryTimesFromPos[codeInteger], getRotationTime(N, codeInteger, curCodeInteger) + codeEntryTimesFromPos[prevCodeInteger])

        codeEntryTimesFromPos = codeEntryTimesFromPrev

    # Return the minimum time needed to enter the code with both locks starting at position 1
    return codeEntryTimesFromPos[1]

# Calculates the minimum time needed to rotate the lock from start to end
def getRotationTime(N: int, start: int, end: int) -> int:
    return min(abs(end - start), N + min(start, end) - max(start, end))
