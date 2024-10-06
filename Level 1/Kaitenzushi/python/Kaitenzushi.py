from typing import List
import queue

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  dishQueue = queue.Queue(maxsize=K)
  dishSet = set()
  
  for _ in range(K):
    dishQueue.put(-1)
  
  count = 0
  for dish in D:
    if dish not in dishSet:
      prev = dishQueue.get()
      if prev in dishSet:
        dishSet.remove(prev)
        
      dishQueue.put(dish)
      dishSet.add(dish)
      count += 1
  
  return count