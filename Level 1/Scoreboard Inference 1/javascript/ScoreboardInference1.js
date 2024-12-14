/**
 * @param {number} N
 * @param {number[]} S
 * @return {number}
 */
function getMinProblemCount(N, S) {
    max = -1
    containsOdd = false
    for (score of S) {
        if (score > max) {
            max = score
        }
        
        containsOdd = containsOdd || (score % 2 == 1)
    }
    
    return Math.floor(max / 2) + (containsOdd ? 1 : 0)
}