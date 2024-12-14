package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getMinimumDeflatedDiscCount(N int32, R []int32) int32 {
	var deflatedDiscCount int32 = 0;

  for i := N - 2; i >= 0; i-- {
		if R[i] >= R[i + 1] {
			deflatedDiscCount++;
			R[i] = R[i + 1] - 1;
		}
	}

	if R[0] <= 0 {
		return -1;
	}

	return deflatedDiscCount;
}
