from typing import Dict, List, Set, Tuple

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    start = ()  # The starting cell
    portals = {}  # Maps a portal letter to the set of locations with that portal
    # Parse the grid to find the starting cell and the locations of each portal
    for row in range(R):
        for col in range(C):
            cell = G[row][col]
        
            if cell == 'S':
                start = (row, col)
            
            if cell.isalpha():
                if cell not in portals:
                    portals[cell] = set()
                
                portals[cell].add((row, col))
            
    return getExitDistance(R, C, G, portals, {start}, {start})

# Returns the distance to the exit from the start cells, where distance is the number of adjacent movements and teleportations required to reach the exit
def getExitDistance(R: int, C: int, G: List[List[str]], portals: Dict[str, Set[Tuple[int, int]]], visitedCells: Set[Tuple[int, int]], startCells: Set[Tuple[int, int]]) -> int:
    if len(startCells) == 0:
        return -1

    nextCells = set()  # The cells to visit next
    portalsAdded = set()  # The portals that have been added to the next cells
    for cell in startCells:
        row, col = cell
        cellVal = G[row][col]
        
        if cellVal == 'E':
            return 0
        elif cellVal == '#':
            continue
        
        if cellVal.isalpha() and cellVal not in portalsAdded:
            portalsAdded.add(cellVal)
            
            # Add the other portal locations to the next cells
            for portalCell in portals[cellVal]:
                if portalCell not in visitedCells:
                    nextCells.add(portalCell)
                    visitedCells.add(portalCell)

        # Add the adjacent cells to the next cells
        for neighbor in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if neighbor[0] >= 0 and neighbor[0] < R and neighbor[1] >= 0 and neighbor[1] < C and neighbor not in visitedCells:
                nextCells.add(neighbor)
                visitedCells.add(neighbor)

    # Recursively call the function with the next cells
    exitDistance = getExitDistance(R, C, G, portals, visitedCells, nextCells)

    # If the exit distance is -1, the exit was not found so return -1
    if exitDistance == -1:
        return -1
    
    # Return the exit distance plus 1
    return exitDistance + 1