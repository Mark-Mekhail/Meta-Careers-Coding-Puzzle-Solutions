import math

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  count = 0
  nextUniform = getNextUniform(A)
  
  while (nextUniform <= B):
    print(nextUniform)
    nextUniform = getNextUniform(nextUniform + 1)
    count += 1
    
  return count
  

def getNextUniform(val: int):
  numDigits = len(str(val))
  firstDigit = val // (10 ** (numDigits - 1))
  
  jumpToNext = 1
  nextUniform = firstDigit
  
  for _ in range(numDigits - 1):
    nextUniform *= 10
    jumpToNext *= 10
    
    nextUniform += firstDigit
    jumpToNext += 1
    
  if nextUniform < val:
    nextUniform += jumpToNext
    
  return nextUniform