from typing import List
from collections import deque

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    max_visits = 0
        
    webpage_hops = {}
    visit_order = deque()

    for i in range(N):
        if i in webpage_hops:
            continue

        visited = set()
        visited.add(i)
        visit_order.append(i)

        next_pos = L[i] - 1
        size = 1

        while next_pos not in visited:
            if next_pos in webpage_hops:
                size += webpage_hops[next_pos]
                break

            size += 1
            visited.add(next_pos)
            visit_order.append(next_pos)
            next_pos = L[next_pos] - 1

        max_visits = max(max_visits, size)

        reached_cycle = False
        while visit_order:
            page = visit_order.popleft()

            if page == next_pos:
                reached_cycle = True

            webpage_hops[page] = size

            if not reached_cycle:
                size -= 1

        if len(webpage_hops) == N or max_visits == N:
            break

    return max_visits