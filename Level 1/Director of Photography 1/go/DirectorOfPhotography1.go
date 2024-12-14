package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getArtisticPhotographCount(N int32, C string, X int32, Y int32) int32 {
  artisticPhotographCount := int32(0);
  
  for i := int32(0); i < N; i++ {
    curChar := string(C[i]);
    
    var opposite string;
    if curChar == "P" {
      opposite = "B";
    } else if curChar == "B" {
      opposite = "P";
    } else {
      continue;
    }
    
    for j := i+X; j <= min(N-1, i+Y); j++ {
      if middleChar := string(C[j]); middleChar == "A" {
        for k := j+X; k <= min(N-1, j+Y); k++ {
          if endChar := string(C[k]); endChar == opposite {
            artisticPhotographCount++;
          }
        }
      }
    }
  }
  
  return artisticPhotographCount;
}

func min(a, b int32) int32 {
    if a < b {
        return a
    }
    return b
}