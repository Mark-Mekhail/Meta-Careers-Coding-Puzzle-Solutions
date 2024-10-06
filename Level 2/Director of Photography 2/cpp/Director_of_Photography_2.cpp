#include <vector>

using namespace std;
// Write any include statements here

long long getArtisticPhotographCount(int N, string C, int X, int Y) {
  long long count = 0;
  vector<long> cumulativePs = vector<long>();
  vector<long> cumulativeBs = vector<long>();
  
  cumulativePs.push_back(C[0] == 'P' ? 1 : 0);
  cumulativeBs.push_back(C[0] == 'B' ? 1 : 0);
  for (int i = 1; i < N; i++) {
    char cur = C[i];
    cumulativePs.push_back(cumulativePs[i-1] + (cur == 'P' ? 1 : 0));
    cumulativeBs.push_back(cumulativeBs[i-1] + (cur == 'B' ? 1 : 0));
  }
  
  vector<long> cumulativeAPs = vector<long>();
  vector<long> cumulativeABs = vector<long>();
  cumulativeAPs.push_back(0);
  cumulativeABs.push_back(0);
  for (int i = 1; i < N - X; i++) {
    cumulativeAPs.push_back(cumulativeAPs[i-1]);
    cumulativeABs.push_back(cumulativeABs[i-1]);
    if (i >= X) {
      if (C[i] == 'A') {
        int start = min(i + X - 1, N - 1);
        int end = min(i + Y, N - 1);
        cumulativeAPs[i] += cumulativePs[end] - cumulativePs[start];
        cumulativeABs[i] += cumulativeBs[end] - cumulativeBs[start];
      }
    }
  }
  
  for (int i = 0; i < (N - 2 * X); i++) {
    char cur = C[i];
    if (cur == 'P' || cur == 'B') {
      char opposite = (cur == 'P') ? 'B' : 'P';
      int start = min(i + X - 1, N - X - 1);
      int end = min(i + Y, N - X - 1);
      count += (opposite == 'B') ? (cumulativeABs[end] - cumulativeABs[start]) : (cumulativeAPs[end] - cumulativeAPs[start]);
    }
  }
  return count;
}