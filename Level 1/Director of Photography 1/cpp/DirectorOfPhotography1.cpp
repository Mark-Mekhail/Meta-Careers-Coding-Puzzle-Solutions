#include <string>

using namespace std;

int getArtisticPhotographCount(int N, string C, int X, int Y) {
  int count = 0;
  for (int i = 0; i < (N - 2 * X); i++) {
    char cur = C[i];
    if (cur == 'P' || cur == 'B') {
      char opposite = (cur == 'P') ? 'B' : 'P';
      for (int j = i + X; j <= (i + Y); j++) {
        if (j < (N - X) && C[j] == 'A') {
          for (int k = j + X; k <= (j + Y); k++) {
            if (k < N && C[k] == opposite) {
              count++;
            }
          }
        }
      }
    }
  }
  return count;
}