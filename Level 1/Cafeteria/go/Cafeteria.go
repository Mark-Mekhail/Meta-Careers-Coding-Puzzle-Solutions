package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"
import "sort"

func getMaxAdditionalDinersCount(N int64, K int64, M int32, S []int64) int64 {
	sort.Slice(S, func(i, j int) bool {
		return S[i] < S[j];
	});

	prevOccupied := int64(-K);
	maxAdditionalDiners := int64(0);
	for _, s := range S {
		maxAdditionalDiners += max(0, (s - prevOccupied - K - 1) / (K + 1));
		prevOccupied = s;
	}

	maxAdditionalDiners += max(0, (N - prevOccupied) / (K + 1));
	return maxAdditionalDiners;
}

func max(a int64, b int64) int64 {
	if a > b {
		return a;
	}
	return b;
}