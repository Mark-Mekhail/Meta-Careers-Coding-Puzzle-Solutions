from typing import List

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    numCells = R * C

    # Count the number of cells that contain a ship
    shipCount = 0
    for row in G:
        for cellVal in row:
            if cellVal == 1:
                shipCount += 1
    
    return shipCount / numCells