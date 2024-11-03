from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    highestScore = 0
    secondHighestScore = 0
    containsScoreOf1 = False
    containsScoreWithOneRemainder = False
    containsScoreWithTwoRemainder = False
    
    for score in S:
        if score > highestScore:
            secondHighestScore = highestScore
            highestScore = score
        elif score > secondHighestScore and score < highestScore:
            secondHighestScore = score
        
        containsScoreOf1 = containsScoreOf1 or (score == 1)
        containsScoreWithOneRemainder = containsScoreWithOneRemainder or (score > 1 and (score % 3 == 1))
        containsScoreWithTwoRemainder = containsScoreWithTwoRemainder or (score % 3 == 2)

    ones = 0
    twos = 0
    if containsScoreWithTwoRemainder:
        # If there is a score with a remainder of 2, then it is always optimal to have a 2-point problem
        twos = 1
        if containsScoreOf1:
            # If there is a score of 1, then we must have a 1-point problem
            ones = 1
        elif containsScoreWithOneRemainder:
            if secondHighestScore == highestScore - 1 and secondHighestScore % 3 == 0:
                ones = 1
            else:
                twos += 1
    elif containsScoreWithOneRemainder or containsScoreOf1:
        # If no score has a remainder of 2 but there is a score with a remainder of 1, then it is always optimal to have a 1-point problem
        ones = 1

    threes = highestScore // 3  # Number of 3-point problems needed to reach the highest score
    remaining_sum = twos * 2 + ones  # Sum of points of problems that are not 3-point problems
    if highestScore % 3 == 0 and remaining_sum == 3:
        # If the highest score is a multiple of 3 and the sum of the remaining problems is 3, then we can remove one 3-point problem
        threes -= 1
    elif highestScore % 3 == 1 and remaining_sum == 4:
        # If the highest score has a remainder of 1 and the sum of the remaining problems is 4, then we can remove one 3-point problem
        threes -= 1

    # Return the total number of problems needed
    return threes + twos + ones