def getWrongAnswers(N: int, C: str) -> str:
    wrongAnswers = []
    for answer in C:
        # If the correct answer is 'A', append the wrong answer 'B', and vice versa
        if answer == 'A':
            wrongAnswers.append('B')
        else:
            wrongAnswers.append('A')
        
    return ''.join(wrongAnswers)