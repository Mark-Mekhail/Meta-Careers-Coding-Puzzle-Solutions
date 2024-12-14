package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getMinProblemCount(N int32, S []int32) int32 {
  maxScore := int32(0);
  containsOdd := false;

	for i := int32(0); i < N; i++ {
		if S[i] > maxScore {
			maxScore = S[i];
		}

		containsOdd = containsOdd || S[i] % 2 == 1;
	}

	minProblemCount := maxScore / 2;
	if containsOdd {
		minProblemCount++;
	}

  return minProblemCount;
}
