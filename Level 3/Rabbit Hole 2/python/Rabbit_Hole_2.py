from typing import List, Set, Dict

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
  linkMap = {}
  for i in range(M):
    fromPage =  A[i]
    toPage =  B[i]

    if fromPage not in linkMap:
      linkMap[fromPage] = set()

    linkMap[fromPage].add(toPage)

  # update cycle map with graph cycles
  cycleMap = {}
  idMap = {}
  traversalOrder = []
  traversedNodes = set()
  for page in linkMap:
    if page not in idMap:
      dfs(page, linkMap, cycleMap, idMap, traversalOrder)

  simplifiedLinkMap = {}
  simplifiedPageWeights = {}
  for page in cycleMap:
    cycleNum = cycleMap[page]
    if page in linkMap:
      if cycleNum not in simplifiedLinkMap:
        simplifiedLinkMap[cycleNum] = set()
      cycleLinks = simplifiedLinkMap[cycleNum]
      for toPage in linkMap[page]:
        if cycleMap[toPage] != cycleNum:
          cycleLinks.add(cycleMap[toPage])
      simplifiedPageWeights[cycleNum] = simplifiedPageWeights.get(cycleNum, 0) + 1

  maxDepth = 1
  depthMap = {}
  for page in traversalOrder:
    pageWeight = simplifiedPageWeights.get(page, 1)
    pageDepth = pageWeight
    if page in simplifiedLinkMap:
      for nextPage in simplifiedLinkMap[page]:
        pageDepth = max(pageDepth, pageWeight + depthMap[nextPage])
    depthMap[page] = pageDepth
    maxDepth = max(pageDepth, maxDepth)

  return maxDepth
  
  
def dfs(startPage: int, linkMap: Dict[int, Set[int]], lowlinkMap: Dict[int, int], idMap: Dict[int, int], traversalOrder: List[int]):
  ancestorStack = []
  ancestorSet = set()
  dfsStack = [startPage]
  
  newVisits = {}
  
  while len(dfsStack) > 0:
    page = dfsStack[-1]
    if page not in ancestorSet:
      ancestorSet.add(page)
      ancestorStack.append(page)
    
    if page not in lowlinkMap:
      nextId = len(lowlinkMap)
      lowlinkMap[page] = nextId
      idMap[page] = nextId
      newVisits[page] = set()

    if page in linkMap:
      recurse = False
      for toPage in linkMap[page]:
        if toPage not in lowlinkMap:
          recurse = True
          newVisits[page].add(toPage)
          dfsStack.append(toPage)
          break
        elif toPage in newVisits[page]:
          lowlinkMap[page] = min(lowlinkMap[page], lowlinkMap[toPage])
        elif toPage in ancestorSet:
          lowlinkMap[page] = min(lowlinkMap[page], idMap[toPage])
      
      if recurse:
        continue
          
    if lowlinkMap[page] == idMap[page]:
      nextNode = ancestorStack.pop()
      while nextNode != page:
        ancestorSet.remove(nextNode)
        lowlinkMap[nextNode] = lowlinkMap[page]
        nextNode = ancestorStack.pop()
      ancestorSet.remove(nextNode)
      traversalOrder.append(lowlinkMap[page])
    
    dfsStack.pop()
        
def getDepth(startPage: int, depthMap: Dict[int, int], simplifiedLinkMap: Dict[int, int], simplifiedPageWeights: Dict[int, int]) -> int:
  dfsStack = [startPage]
  
  while len(dfsStack) > 0:
    page = dfsStack[-1]
    
    if page not in depthMap:
      pageWeight = simplifiedPageWeights.get(page, 1)
      
      if page in simplifiedLinkMap:
        for nextPage in simplifiedLinkMap[page]:
          if nextPage not in depthMap:
            dfsStack.append(nextPage)
      
      if dfsStack[-1] == page:
        maxChildDepth = 0
        if page in simplifiedLinkMap:
          for nextPage in simplifiedLinkMap[page]:
            maxChildDepth = max(maxChildDepth, depthMap[nextPage])
        depthMap[page] = maxChildDepth + pageWeight
    
    if dfsStack[-1] == page:
      dfsStack.pop()
        
  return depthMap[startPage]