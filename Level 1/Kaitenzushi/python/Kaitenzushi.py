from typing import List
import queue

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    dishQueue = queue.Queue(maxsize=K)  # Queue of the last K dishes
    dishSet = set()  # Use a set to keep track of the dishes in the queue
    
    for _ in range(K):
        # Initialize the queue with -1, which is not a valid dish
        dishQueue.put(-1)
    
    eatenDishCount = 0
    for dish in D:
        if dish in dishSet:
            # If the dish is already in the queue, skip it
            continue 
        
        # Remove the oldest dish from the queue
        dishSet.discard(dishQueue.get())
        
        dishQueue.put(dish)
        dishSet.add(dish)
        eatenDishCount += 1
    
    return eatenDishCount