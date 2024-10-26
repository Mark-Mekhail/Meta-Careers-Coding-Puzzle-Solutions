import java.util.*;

class Solution {
  
  public long getMaxAdditionalDinersCount(long N, long K, int M, long[] S) {
    Arrays.sort(S);
    
    long curStart = 1;
    long additionalDinersCount = 0;
    for (int i = 0; i < M; i++) {
      long curSeat = S[i];
      
      long freeSeats = (curSeat - K - curStart);
      if (freeSeats > 0) {
        additionalDinersCount += freeSeats / (K + 1);
        if (freeSeats % (K + 1) > 0) {
          additionalDinersCount++;
        }
      }
      
      curStart = curSeat + K + 1;
    }
    
    if (N + 1 > curStart) {
      additionalDinersCount += (N + 1 - curStart) / (K + 1);
      if ((N + 1 - curStart) % (K + 1) > 0) {
        additionalDinersCount++;
      }
    }
    
    return additionalDinersCount;
  }
  
}
