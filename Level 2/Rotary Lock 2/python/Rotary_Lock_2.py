from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    c_vals = set(C)
    c_vals.add(1)
    
    next_times = {}
    for c1 in c_vals:
        next_times[c1] = {}
        if c1 == C[M - 1]:
            for c2 in c_vals:
                next_times[c1][c2] = 0
        next_times[c1][C[M - 1]] = 0

    for i in range(M - 1, -1, -1):
        cur_num = C[i]
        prev_num = C[i - 1] if i > 0 else 1
        cur_times = {c1: {} for c1 in c_vals}

        for c1 in c_vals:
            if c1 == prev_num:
                for c2 in c_vals:
                    cur_times[c1][c2] = min(
                        get_time_to_rotate(N, c1, cur_num) + next_times[cur_num].get(c2, float('inf')),
                        get_time_to_rotate(N, c2, cur_num) + next_times[c1].get(cur_num, float('inf'))
                    )
            else:
                cur_times[c1][prev_num] = min(
                    get_time_to_rotate(N, c1, cur_num) + next_times[cur_num].get(prev_num, float('inf')),
                    get_time_to_rotate(N, prev_num, cur_num) + next_times[c1].get(cur_num, float('inf'))
                )

        next_times = cur_times

    return next_times[1].get(1, float('inf'))

def get_time_to_rotate(N: int, start: int, end: int) -> int:
    return min(abs(end - start), N + min(start, end) - max(start, end))