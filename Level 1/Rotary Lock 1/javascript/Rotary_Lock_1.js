/**
 * @param {number} N
 * @param {number} M
 * @param {number[]} C
 * @return {number}
 */
function getMinCodeEntryTime(N, M, C) {
    time = 0
    prev = 1
    for (i = 0; i < M; i++) {
      digit = C[i]
      time += Math.min(Math.abs(digit - prev), N + Math.min(prev, digit) - Math.max(prev, digit))
      prev = digit
    }
    
    return time
  }