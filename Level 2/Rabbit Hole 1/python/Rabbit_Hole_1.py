from typing import List
from collections import deque

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    maxVisitableWebpages = 0
        
    webpageHops = {}  # key: webpage index, value: number of webpages that can be visited from this webpage
    visitOrder = deque()  # order of webpages visited from each starting page (populated and cleared as we go)
    for i in range(N):
        if i in webpageHops:
            # We've already visited this webpage and calculated the number of webpages that can be visited from it
            continue

        # Start from webpage i and visit all webpages that can be visited from it
        visited = {i}
        visitOrder.append(i)
        linkedWebpage = L[i] - 1
        webpagesVisited = 1
        while linkedWebpage not in visited:
            if linkedWebpage in webpageHops:
                # We've already visited this webpage and calculated the number of webpages that can be visited from it
                webpagesVisited += webpageHops[linkedWebpage]
                break

            # Visit the next webpage
            webpagesVisited += 1
            visited.add(linkedWebpage)
            visitOrder.append(linkedWebpage)
            linkedWebpage = L[linkedWebpage] - 1

        maxVisitableWebpages = max(maxVisitableWebpages, webpagesVisited)

        reached_cycle = False
        # Update the number of webpages that can be visited from each webpage in the visit order
        while visitOrder:
            page = visitOrder.popleft()

            if page == linkedWebpage:
                # We've reached a cycle because the last webpage links back to a webpage we've already visited
                reached_cycle = True

            webpageHops[page] = webpagesVisited

            if not reached_cycle:
                # We haven't reached a cycle yet, so this webpage can visit one less webpage than the webpage that linked to it
                webpagesVisited -= 1

        # Minor optimization to break early if we've visited all webpages
        if len(webpageHops) == N:
            break

    return maxVisitableWebpages