/**
 * @param {number} N
 * @param {number[]} V
 * @param {number} C
 * @param {number} S
 * @return {number}
 */
function getMaxExpectedProfit(N, V, C, S) {
    var maxExpectedProfitsFromStart = new Array(N)
    for (var i = 0; i <= N; i++) {
      maxExpectedProfitsFromStart[i] = 0
    }
    
    for (var i = N - 1; i >= 0; i--) {
      var expectedMailValue = 0
      for (var j = i; j < N; j++) {
        expectedMailValue = (1 - S) * expectedMailValue + V[j]
        const maxExpectedProfitIfSoldToday = expectedMailValue - C + maxExpectedProfitsFromStart[j+1]
        if (maxExpectedProfitIfSoldToday > maxExpectedProfitsFromStart[i]) {
          maxExpectedProfitsFromStart[i] = maxExpectedProfitIfSoldToday
        }
      }
    }
    
    return maxExpectedProfitsFromStart[0]
  }