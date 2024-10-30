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
      seconds += P[i] - firstFrogIndex
      firstFrogIndex = P[i]
      for (;i + 1 < F && P[i+1] < firstFrogIndex + i; i++);
    }
    
    seconds += N - firstFrogIndex
    
    return seconds
  }