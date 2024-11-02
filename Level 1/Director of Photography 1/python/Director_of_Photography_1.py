def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    artisticPhotoCount = 0
    for i in range(N - 2 * X):
        artisticPhotoCount += getArtisticPhotographsFromStartPos(N, C, X, Y, i)

    return artisticPhotoCount

# Count the number of artistic photographs that can be taken from a given starting position startPos
def getArtisticPhotographsFromStartPos(N: int, C: str, X: int, Y: int, startPos: int) -> int:
    cellChar = C[startPos]
    if cellChar not in ['P', 'B']:
        return 0

    # The character that must come after the actor for the photograph to be artistic
    cellComplement = 'B' if cellChar == 'P' else 'P'

    interval = (min(N, startPos + X), min(N, startPos + Y + 1))

    artisticPhotoCount = 0
    for i in range(*interval):
        # If an actor is found in the interval, add the occurences of cellComplement in the interval [i + X, i + Y + 1)
        if C[i] == 'A':
            artisticPhotoCount += countCharacterOccurenceInInterval(N, C, cellComplement, i + X, i + Y + 1)

    return artisticPhotoCount

# Count the number of occurrences of a character char in a given interval [start, end) of a string C
def countCharacterOccurenceInInterval(N: int, C: str, char: str, start: int, end: int) -> int:
    interval = (min(N, start), min(N, end))

    count = 0
    for i in range(*interval):
        if C[i] == char:
            count += 1

    return count