from typing import List
from math import ceil

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()

    additionalDiners = 0
    nextOccupiableSeat = 1
    for i in range(M):
        curSeat = S[i]

        additionalDiners += getMaxDinersBetweenSeats(nextOccupiableSeat, curSeat - K - 1, K)

        # Set nextOccupiableSeat to the next socially distanced seat after the current seat
        nextOccupiableSeat = curSeat + K + 1

    # Add the number of diners that can be seated between the last occupied seat and the last seat
    additionalDiners += getMaxDinersBetweenSeats(nextOccupiableSeat, N, K)

    return additionalDiners

# Determine the maximum number of diners that can be seated between two seat positions
def getMaxDinersBetweenSeats(startPos: int, endPos: int, K: int) -> int:
    num_seats = endPos - startPos + 1
    return ceil(num_seats / (K + 1)) if num_seats > 0 else 0