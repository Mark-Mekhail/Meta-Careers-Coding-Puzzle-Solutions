#include <stdlib.h>

using namespace std;

long long getTimeToRotate(int N, int start, int end) {
    return min(abs(end - start), N + min(start, end) - max(start, end));
  }

long long getMinCodeEntryTime(int N, int M, vector<int> C) {
  map<int, map<int, long long>> nextTimes = map<int, map<int, long long>>(); 
  
  set<int> cVals = set<int>(C.begin(), C.end());
  cVals.insert(1);
  
  for (auto& c1 : cVals) {
    map<int, long long> cellMap = map<int, long long>();
    if (c1 == C[M-1]) {
      for (auto& c2 : cVals) {
        cellMap[c2] = 0;
      }
    }
    cellMap[C[M-1]] = 0;
    nextTimes[c1] = cellMap;
  }
  
  for (int i = M - 1; i >= 0; i--) {
    int curNum = C[i];
    int prevNum = (i > 0) ? C[i-1] : 1;
    map<int, map<int, long long>> curTimes = map<int, map<int, long long>>();
    for (auto& c1 : cVals) {
      map<int, long long> c1Times = map<int, long long>();
      if (c1 == prevNum) {
        for (auto& c2 : cVals) {
          c1Times[c2] = min(getTimeToRotate(N, c1, curNum) + nextTimes[curNum][c2], getTimeToRotate(N, c2, curNum) + nextTimes[c1][curNum]);
        }
      }
      else {
        c1Times[prevNum] = min(getTimeToRotate(N, c1, curNum) + nextTimes[curNum][prevNum], getTimeToRotate(N, prevNum, curNum) + nextTimes[c1][curNum]);
      }
      
      curTimes[c1] = c1Times;
    }
    
    nextTimes = curTimes;
  }
  
  return nextTimes[1][1];
}