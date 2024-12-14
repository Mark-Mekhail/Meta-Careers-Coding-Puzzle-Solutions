package main
import "bufio"
import "fmt"
import "os"
import "strconv"
import "strings"

func getUniformIntegerCountInInterval(A int64, B int64) int32 {
  var uniformIntegerCount int32 = 0;
  var first, last int64 = 1, 10;
  
  // Ensure first, last overlap A, B
  for last <= A {
    first *= 10;
    last *= 10;
  }
  
  // Count the uniform integers with the same number of digits as A
  uniform := last - 1;
  for i := int64(8); i >= 0; i-- {
    if uniform >= A && uniform <= B {
      uniformIntegerCount++;
    }
    
    uniform = uniform * i / (i + 1);
  }
  first *= 10;
  last *= 10;
  
  // Count uniform integers with a number of digits between that of A and B
  for first >= A && last <=B {
    uniformIntegerCount += 9;
    first *= 10;
    last *= 10;
  }
  
  // Count the uniform integers with the same number of digits at B
  uniform = last - 1;
  for i := int64(8); i >= 0; i-- {
    if uniform >= A && uniform <= B {
      uniformIntegerCount++;
    }
    
    uniform = uniform * i / (i + 1);
  }
  
  return uniformIntegerCount;
}
