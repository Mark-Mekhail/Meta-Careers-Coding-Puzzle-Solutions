from typing import List

def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
  circumferenceTunnelTime = 0
  for i in range(N):
    circumferenceTunnelTime += B[i] - A[i]
  

  totalSeconds = (K // circumferenceTunnelTime) * C
  remainingTime = K % circumferenceTunnelTime
  
  # We can sort the list separately since tunnels do not overlap or cross position 0
  A.sort()
  B.sort()
  if remainingTime == 0:
    return totalSeconds - C + B[-1]
  else:
    for i in range(N):
      tunnelTime = B[i] - A[i]
      
      remainingTime -= tunnelTime
      if remainingTime <= 0:
        # The train exceeds K seconds in the tunnel by -remainingTime seconds so we need to add the remaining time to the total time it takes to reach B[i]
        return totalSeconds + B[i] + remainingTime