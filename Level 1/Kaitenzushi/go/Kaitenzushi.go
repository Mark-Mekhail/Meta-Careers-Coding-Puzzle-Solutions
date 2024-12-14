package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"
import "container/list"

type Set map[int32]struct{};

func (s Set) Add(e int32) {
  s[e] = struct{}{}
}

func (s Set) Remove(e int32) {
	delete(s, e)
}

func (s Set) Contains(e int32) bool {
	_, ok := s[e]
	return ok
}

func getMaximumEatenDishCount(N int32, D []int32, K int32) int32 {
  var eatenDishCount int32 = 0;
	var prevKEatenDishesSet Set = make(Set);
	var prevKEatenDishesQueue = list.New();

	for i := int32(0); i < N; i++ {
		curDish := D[i];

		if !prevKEatenDishesSet.Contains(curDish) {
			prevKEatenDishesSet.Add(curDish);
			prevKEatenDishesQueue.PushBack(D[i]);
			eatenDishCount++;

			if len(prevKEatenDishesSet) > int(K) {
				prevKEatenDishesSet.Remove(prevKEatenDishesQueue.Front().Value.(int32));
				prevKEatenDishesQueue.Remove(prevKEatenDishesQueue.Front());
			}
		}
	}
	
	return eatenDishCount;
}
