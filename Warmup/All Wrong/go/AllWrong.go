package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getWrongAnswers(N int32, C string) string {
  var wrongAnswers string
  
  for i := 0; i < len(C); i++ {
    cur := string(C[i])
    
    if cur == "A" {
      wrongAnswers += "B"
    } else {
      wrongAnswers += "A"
    }
  }
  
  return wrongAnswers
}
