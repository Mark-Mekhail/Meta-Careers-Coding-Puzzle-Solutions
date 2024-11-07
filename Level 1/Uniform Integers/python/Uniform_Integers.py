def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    uniformIntegerCount = 0
    nextUniformInteger = getNextUniformInteger(A)
    
    while (nextUniformInteger <= B):
        uniformIntegerCount += 1
        nextUniformInteger = getNextUniformInteger(nextUniformInteger + 1)
      
    return uniformIntegerCount
  
# Get the smallest uniform integer greater than or equal a given value
def getNextUniformInteger(floor: int) -> int:
    numDigits = len(str(floor))
    firstDigit = floor // (10 ** (numDigits - 1))
    
    uniformOnes = 1  # An integer of all 1's with numDigits digits
    nextUniformInteger = firstDigit
    
    for _ in range(numDigits - 1):
        nextUniformInteger *= 10
        uniformOnes *= 10
        
        nextUniformInteger += firstDigit
        uniformOnes += 1
      
    if nextUniformInteger < floor:
        # If val is greater than its first digit repeated numDigits times, increment all digits by 1
        nextUniformInteger += uniformOnes
      
    return nextUniformInteger