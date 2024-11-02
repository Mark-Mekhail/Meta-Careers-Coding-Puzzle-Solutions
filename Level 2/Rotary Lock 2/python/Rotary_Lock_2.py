from typing import List

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    c_vals = set(C)
    c_vals.add(1)
    
    next_times = {c1: 0 for c1 in c_vals}

    for i in range(M - 1, -1, -1):
        cur_num = C[i]
        prev_num = C[i - 1] if i > 0 else 1
        
        prev_to_cur_rotation_time = get_time_to_rotate(N, prev_num, cur_num)
        
        cur_times = {}
        for c1 in c_vals:
            cur_times[c1] = min(prev_to_cur_rotation_time + next_times[c1], get_time_to_rotate(N, c1, cur_num) + next_times[prev_num])

        next_times = cur_times

    return next_times[1]

def get_time_to_rotate(N: int, start: int, end: int) -> int:
    return min(abs(end - start), N + min(start, end) - max(start, end))
