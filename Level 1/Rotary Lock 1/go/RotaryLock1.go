package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getMinCodeEntryTime(N int32, M int32, C []int32) int64 {
  minCodeEntryTime := int64(minRotationTime(N, int32(1), C[0]));

	for i := int32(0); i < M - 1; i++ {
		minCodeEntryTime += int64(minRotationTime(N, C[i], C[i + 1]));
	}

	return minCodeEntryTime;
}

func minRotationTime(N int32, start int32, end int32) int32 {
	return min(abs(start - end), N - abs(start - end));
}

func min(a, b int32) int32 {
	if a < b {
		return a;
	}
	return b;
}

func abs(a int32) int32 {
	if a < 0 {
		return -a;
	}
	return a;
}