from typing import List

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    start = (0,0)
    portals = {}
    for row in range(R):
        for col in range(C):
            cell = G[row][col]
        
            if cell == 'S':
                start = (row, col)
            
            if cell.isalpha():
                if cell not in portals:
                    portals[cell] = set()
                
                portals[cell].add((row, col))
    
    steps = 0
    visited = set()
    curCells = set([start])
    nextCells = set()
    while len(curCells) > 0:
        nextCells.clear()
        curCells -= visited
        
        for pos in curCells:
            visited.add(pos)
        
            row = pos[0]
            col = pos[1]
            
            cellVal = G[row][col]
            
            if cellVal == 'E':
                return steps
            elif cellVal == '#':
                continue
            
            if cellVal.isalpha():
                nextCells |= portals[cellVal]
            
            if row > 0:
                nextCells.add((row - 1, col))
            if row < R - 1:
                nextCells.add((row + 1, col))
            if col > 0:
                nextCells.add((row, col - 1))
            if col < C - 1:
                nextCells.add((row, col + 1))
        
        steps += 1
        tmp = curCells
        curCells = nextCells
        nextCells = tmp
            
    return -1