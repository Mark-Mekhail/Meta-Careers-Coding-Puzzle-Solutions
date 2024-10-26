/**
 * @param {number} N
 * @param {number[]} S
 * @return {number}
 */
function getMinProblemCount(N, S) {
    let max = 0
    let secondMax = 0
    let hasOne = false
    let hasOneRemainder = false
    let hasTwoRemainder = false
    
    for (let i = 0; i < N; i++) {
        const score = S[i]
        
        if (score > max) {
            secondMax = max
            max = score
        }
        else if (score > secondMax) {
            secondMax = score
        }
        
        
        hasOne = hasOne || score == 1
        hasOneRemainder = hasOneRemainder || (score > 1 && (score % 3 == 1))
        hasTwoRemainder = hasTwoRemainder || (score % 3 == 2)
    }
    
    let ones = 0
    let twos = 0
    if (hasTwoRemainder) {
        if (hasOne) {
          ones = 1
          twos = 1
        }
        else if (hasOneRemainder) {
            if (secondMax == max - 1 && max % 3 == 1) {
                twos = 1
                ones = 1
            }
            else {
                twos = 2
            }
        }
        else {
            twos = 1
        }
    }
    else if (hasOneRemainder || hasOne) {
        ones = 1
    }
    
    let threes = Math.floor(max / 3)
    let remainingSum = twos * 2 + ones;
    if (max % 3 == 0 && remainingSum == 3) {
        threes--;
    }
    else if (max % 3 == 1 && remainingSum == 4) {
        threes--;
    }
    
    if (twos + ones > 2 || (max % 3 == 2 && twos == 0)) {
        throw Error("ow")
    }
    
    return threes + twos + ones;
}