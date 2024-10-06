/**
 * @param {number} R
 * @param {number} C
 * @param {string[][]} G
 * @return {number}
 */
function getSecondsRequired(R, C, G) {
    var S;
    var portals;
    for (var r = 0; r < R; r++) {
      for (var c = 0; c < C; c++) {
        const cur = G[r][c]
        if (cur == 'S') {
          S = [r,c]
        }
        else if ('a' <= cur <= 'z') {
          if (!(cur in portals)) {
            portals[cur] = new Set()
          }
          portals[cur].add([r,c])
        }
      }
    }
    
    var steps = 1
    var visited = new Set([S])
    var cur = new Set([S])
    var next = new Set()
    while (cur.size() > 0) {
      for (pos of cur) {
        const posVal = G[pos[0]][pos[1]]
        
        if (posVal == 'E') {
          return steps
        }
        
        if (!(pos in visited)) {
          visited.add(pos)
        }
        else {
          continue
        }
        
        neighbours = Set()
        if (pos[0] > 0) {
          neighbours.add([pos[0] - 1, pos[1]])
        }
        if (pos[0] < R - 1) {
          neighbours.add([pos[0] + 1, pos[1]])
        }
        if (pos[1] > 0) {
          neighbours.add([pos[0], pos[1] - 1])
        }
        if (pos[1] < C - 1) {
          neighbours.add([pos[0], pos[1] + 1])
        }
        if ('a' <= posVal <= 'z') {
          for (portal of portals[posVal]) {
            neighbours.add(portal)
          }
        }
      }
      
      steps++
    }
  }