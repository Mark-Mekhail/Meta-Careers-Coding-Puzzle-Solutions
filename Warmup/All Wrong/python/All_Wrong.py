def getWrongAnswers(N: int, C: str) -> str:
  wrongAnswers = []
  for answer in C:
    if answer == 'A':
      wrongAnswers.append('B')
    else:
      wrongAnswers.append('A')
      
  
  return ''.join(wrongAnswers)