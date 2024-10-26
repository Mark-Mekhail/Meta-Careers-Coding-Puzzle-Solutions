from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    max_score = 0
    second_max = 0
    has_one = False
    has_one_remainder = False
    has_two_remainder = False
    
    for score in S:
        if score > max_score:
            second_max = max_score
            max_score = score
        elif score > second_max:
            second_max = score
        
        has_one = has_one or (score == 1)
        has_one_remainder = has_one_remainder or (score > 1 and (score % 3 == 1))
        has_two_remainder = has_two_remainder or (score % 3 == 2)

    ones = 0
    twos = 0
    if has_two_remainder:
        if has_one:
            ones = 1
            twos = 1
        elif has_one_remainder:
            if second_max == max_score - 1 and max_score % 3 == 1:
                twos = 1
                ones = 1
            else:
                twos = 2
        else:
            twos = 1
    elif has_one_remainder or has_one:
        ones = 1

    threes = max_score // 3
    remaining_sum = twos * 2 + ones
    if max_score % 3 == 0 and remaining_sum == 3:
        threes -= 1
    elif max_score % 3 == 1 and remaining_sum == 4:
        threes -= 1

    return threes + twos + ones