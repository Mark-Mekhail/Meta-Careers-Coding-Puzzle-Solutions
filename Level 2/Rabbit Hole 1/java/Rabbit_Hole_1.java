import java.util.*;

class Solution {
  
  public int getMaxVisitableWebpages(int N, int[] L) {
    int maxVisits = 0;
    
    Map<Integer, Integer> webpageHops = new HashMap<>();
    LinkedList<Integer> visitOrder = new LinkedList<>();
    
    for (int i = 0; i < N; i++) {
      if (webpageHops.containsKey(i)) {
        continue;
      }
      
      Set<Integer> visited = new HashSet<>();
      visited.add(i);
      visitOrder.add(i);
      
      int nextPos = L[i] - 1;
      int size = 1;
      while (!visited.contains(nextPos)) {
        if (webpageHops.containsKey(nextPos)) {
          size += webpageHops.get(nextPos);
          break;
        }
        
        size++;
        visited.add(nextPos);
        visitOrder.add(nextPos);
        nextPos = L[nextPos] - 1;
      }
      
      if (size > maxVisits) {
        maxVisits = size;
      }
      
      boolean reachedCycle = false;
      while (visitOrder.size() > 0) {
        Integer page = visitOrder.poll();
        
        if (page == nextPos) {
          reachedCycle = true;
        }
        webpageHops.put(page, size);
        
        if (!reachedCycle) {
          size--;
        }
      }
      
      if (webpageHops.size() == N || maxVisits == N) {
        break;
      }
    }
    
    return maxVisits;
  }
  
}
