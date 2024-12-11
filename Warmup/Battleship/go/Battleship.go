package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getHitProbability(R int32, C int32, G [][]int32) float64 {
  numShips := float64(0)
  for row := int32(0); row < R; row++ {
    for col := int32(0); col < C; col++ {
      if G[row][col] == 1 {
        numShips++
      }
    }
  }
  
  return numShips / float64(R * C)
}
