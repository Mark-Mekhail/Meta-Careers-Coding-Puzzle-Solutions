from typing import List

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()

    additional_diners_count = 0
    cur_start = 1
    for i in range(M):
        cur_seat = S[i]

        free_seats = cur_seat - K - cur_start
        if free_seats > 0:
            additional_diners_count += free_seats // (K + 1)
            if free_seats % (K + 1) > 0:
                additional_diners_count += 1

        cur_start = cur_seat + K + 1

    if N + 1 > cur_start:
        free_seats = N + 1 - cur_start
        additional_diners_count += free_seats // (K + 1)
        if free_seats % (K + 1) > 0:
            additional_diners_count += 1

    return additional_diners_count