from typing import List

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  circumferenceTunnelTime = 0
  for i in range(N):
    circumferenceTunnelTime += B[i] - A[i]
  
  totalSeconds = (K // circumferenceTunnelTime) * C
  remainingTime = K % circumferenceTunnelTime
  
  A.sort()
  B.sort()
  if remainingTime == 0:
    return totalSeconds - C + B[-1]
  else:
    for i in range(N):
      tunnelTime = B[i] - A[i]
      
      remainingTime -= tunnelTime
      if remainingTime <= 0:
        return totalSeconds + B[i] + remainingTime