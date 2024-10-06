from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
  numCells = R * C
  numShipCells = 0
  
  for row in G:
    for cell in row:
      if cell == 1:
        numShipCells += 1
  
  return numShipCells / numCells