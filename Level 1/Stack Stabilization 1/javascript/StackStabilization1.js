/**
 * @param {number} N
 * @param {number[]} R
 * @return {number}
 */
function getMinimumDeflatedDiscCount(N, R) {
    count = 0
    for (i = N - 2; i >= 0; i--) {
        if (R[i] >= R[i+1]) {
            R[i] = R[i+1] - 1
            if (R[i] == 0) {
                return -1
            }
            count++
        }
    }
    
    return count
}