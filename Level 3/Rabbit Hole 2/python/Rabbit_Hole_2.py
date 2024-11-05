from typing import List, Set, Dict

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:
    webpageLinkMap = getWebpageLinkMap(M, A, B)

    # Get the index of the strongly connected component (SCC) that each webpage is a part of and the reverse topological ordering of the SCCs
    webpageToSCCIndexMap, SCCReverseTopologicalOrder = getSCCs(webpageLinkMap)

    # Get a map of the links between SCCs and the number of webpages in each SCC with more than one webpage
    SCCLinkMap, SCCSizeMap = getSCCLinkMap(webpageToSCCIndexMap, webpageLinkMap)

    return largestPathSum(SCCReverseTopologicalOrder, SCCLinkMap, SCCSizeMap)

# Map each webpage to the set of webpages it links to
def getWebpageLinkMap(M: int, A: List[int], B: List[int]) -> Dict[int, Set[int]]:
    webpageLinkMap = {}
    for i in range(M):
        fromPage =  A[i]
        toPage =  B[i]

        if fromPage not in webpageLinkMap:
            webpageLinkMap[fromPage] = set()

        webpageLinkMap[fromPage].add(toPage)

    return webpageLinkMap

# Get the index of the strongly connected component (SCC) that each webpage is a part of and a reverse topological ordering of the SCCs
def getSCCs(webpageLinkMap: Dict[int, Set[int]]) -> Dict[int, int]:
    webpageToSCCIndexMap = {}  # Maps a webpage index to the lowest index of any webpage in the connected component it belongs to
    SCCReverseTopologicalOrder = []  # Represents the topological ordering of the connected components

    webpageIndexMap = {}  # Maps a webpage to its tarjan algorithm index, which represents its position in the ordering of webpages visited
    for page in webpageLinkMap:
        if page not in webpageIndexMap:
            # Run Tarjan's algorithm starting from the webpage if it has not been visited yet
            tarjan(page, webpageLinkMap, webpageToSCCIndexMap, webpageIndexMap, SCCReverseTopologicalOrder)

    return webpageToSCCIndexMap, SCCReverseTopologicalOrder

# Tarjan's algorithm for finding strongly connected components from a given starting page startPage. 
# Populates the index to lowlink map lowlinkMap, the map of webpages to their tarjan index indexMap, and the SCC traversal order traversalOrder
def tarjan(startPage: int, webpageLinkMap: Dict[int, Set[int]], lowlinkMap: Dict[int, int], indexMap: Dict[int, int], traversalOrder: List[int]):
    ancestorStack = []  # A stack of the webpages in the current search path
    ancestorSet = set()  # A set of the webpages in the current search path

    dfsStack = [startPage]  # A stack of the webpages to visit
    while len(dfsStack) > 0:
        page = dfsStack[-1]  # The current webpage being visited
        if page not in ancestorSet:
            ancestorSet.add(page)
            ancestorStack.append(page)
        
        if page not in lowlinkMap:
            # The webpage has not been visited yet so assign it an index and lowlink value
            pagesFound = len(lowlinkMap)
            lowlinkMap[page] = pagesFound
            indexMap[page] = pagesFound

        if page in webpageLinkMap:
            # If the page has links, visit them
            recurse = False
            for toPage in webpageLinkMap[page]:
                if toPage not in lowlinkMap:
                    # If the linked page has not been visited yet, visit it before continuing
                    recurse = True
                    dfsStack.append(toPage)
                    break
                elif toPage in ancestorSet:
                    # If the linked page is in the current search path, update the lowlink value of both pages
                    lowlinkMap[page] = min(lowlinkMap[page], lowlinkMap[toPage])
                    lowlinkMap[toPage] = lowlinkMap[page]
            
            if recurse:
                continue
              
        if lowlinkMap[page] == indexMap[page]:
            # The webpage is the root of a connected component so update the lowlink values of its ancestor webpages in the connected component
            nextNode = ancestorStack.pop()
            while nextNode != page:
                ancestorSet.remove(nextNode)
                lowlinkMap[nextNode] = lowlinkMap[page]
                nextNode = ancestorStack.pop()
            ancestorSet.remove(nextNode)

            # Add the connected component to the traversal order
            traversalOrder.append(lowlinkMap[page])
        
        dfsStack.pop()

# Get a map of the links between SCCs and the number of webpages in each SCC
def getSCCLinkMap(webpageToSCCIndexMap: Dict[int, int], webpageLinkMap: Dict[int, Set[int]]) -> Dict[int, Set[int]]:
    SCCLinkMap = {}  # Maps a SCC index to the set of indices of SCCs it links to
    SCCSizeMap = {}  # Maps the index of a SCC with multiple webpages to the number of webpages in the SCC
    for page in webpageToSCCIndexMap:
        pageSCCIndex = webpageToSCCIndexMap[page]
        if page in webpageLinkMap:
            # If the webpage has links, add the SCCs it links to to the set of SCCs its SCC links to
            if pageSCCIndex not in SCCLinkMap:
                SCCLinkMap[pageSCCIndex] = set()

            for toPage in webpageLinkMap[page]:
                if webpageToSCCIndexMap[toPage] != pageSCCIndex:
                    SCCLinkMap[pageSCCIndex].add(webpageToSCCIndexMap[toPage])

            # Update the number of webpages in the SCC
            SCCSizeMap[pageSCCIndex] = SCCSizeMap.get(pageSCCIndex, 0) + 1

    return SCCLinkMap, SCCSizeMap

# Get the length of the longest path in a directed acyclic graph, where length is defined as the sum of the weights of the nodes in the path
def largestPathSum(reverseTopologicalNodeOrder: List[int], linkMap: Dict[int, int], nodeWeightMap: Dict[int, int]) -> int:
    largestPathSumMap = {}  # Maps a node to the length of the longest path starting from the node

    # By computing in reverse topological order, we know that longest path starting from any node linked to from the current node has already been calculated
    for node in reverseTopologicalNodeOrder:
        # Find the longest path length starting from any node linked to from the current node
        longestChildPathSize = 0
        if node in linkMap:
            for childSCC in linkMap[node]:
                longestChildPathSize = max(longestChildPathSize, largestPathSumMap[childSCC])

        # The longest path length starting from the current node is the weight of the node plus the longest path length starting from any node linked to from the current node
        pathSize = longestChildPathSize + nodeWeightMap.get(node, 1)

        largestPathSumMap[node] = pathSize

    return max(largestPathSumMap.values())