/**
 * @param {number} N
 * @param {number} F
 * @param {number[]} P
 * @return {number}
 */
function getSecondsRequired(N, F, P) {
    P.sort((a,b) => a - b)
    
    var firstFrogIndex = P[0]
    var seconds = 0
    for (let i = 1; i < F; i++) {
      nextFrogIndex = P[i]
      const distToNextFrog = nextFrogIndex - (firstFrogIndex + i - 1)
      const hopsToNextFrog = Math.ceil(distToNextFrog / i)
      seconds += hopsToNextFrog * i + nextFrogIndex - (firstFrogIndex + hopsToNextFrog * i)
      firstFrogIndex = nextFrogIndex
      while (i + 1 < F && P[i+1] < firstFrogIndex + i) {
        nextFrogIndex = P[++i]
      }
    }
    
    const distToEnd = N - (firstFrogIndex + F - 1)
    const hopsToEnd = distToEnd > 0 ? Math.ceil(distToEnd / F) : 0
    seconds += hopsToEnd * F + N - (firstFrogIndex + hopsToEnd * F)
    
    return seconds
  }