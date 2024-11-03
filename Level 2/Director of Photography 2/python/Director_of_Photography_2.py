from typing import List

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Get the cumulative counts of distinct pairs of actors and photographers/backdrops within X and Y cells of the actor
    cumulativeArtisticActorCharacterCounts = {
        'P': getCumulativeArtisticActorCharacterCounts(N, C, X, Y, 'P'),
        'B': getCumulativeArtisticActorCharacterCounts(N, C, X, Y, 'B')
    }
    
    artisticPhotographCount = 0
    for i in range(N - 2 * X):
        curChar = C[i]
        if curChar == 'P' or curChar == 'B':
            artisticConfigurationCounts = cumulativeArtisticActorCharacterCounts['B' if curChar == 'P' else 'P']

            artisticIntervalStart = min(i + X - 1, N - X - 1)  # Just before the first index that the actor can be in
            artisticIntervalEnd = min(i + Y, N - X - 1)  # Last index that the actor can be in

            # Add the number of actor-opposite character pairs in the range (artisticIntervalStart, artisticIntervalEnd] to the count
            artisticPhotographCount += artisticConfigurationCounts[artisticIntervalEnd] - artisticConfigurationCounts[artisticIntervalStart]
    
    return artisticPhotographCount

# Creates a list of cumulative counts of distinct pairs of actors followed within X and Y cells by a given character char in a string C
def getCumulativeArtisticActorCharacterCounts(N: int, C: str, X: int, Y: int, char: str) -> List[int]:
    cumulativeCharCounts = getCumulativeCharCounts(N, C, char)

    cumulativeArtisticActorCharCounts = [0] * (N - X)
    for i in range(X, N - X):
        cumulativeArtisticActorCharCounts[i] = cumulativeArtisticActorCharCounts[i - 1]

        if C[i] == 'A':
            artisticIntervalStart = min(i + X - 1, N - 1)  # Just before the first index that the character can be in
            artisticIntervalEnd = min(i + Y, N - 1)  # Last index that the character can be in

            # Add the number of characters in the range (artisticIntervalStart, artisticIntervalEnd] to the cumulative count
            cumulativeArtisticActorCharCounts[i] += cumulativeCharCounts[artisticIntervalEnd] - cumulativeCharCounts[artisticIntervalStart]
    
    return cumulativeArtisticActorCharCounts

# Creates a list of cumulative counts of a given character char in a string C
def getCumulativeCharCounts(N: int, C: str, char: str) -> List[int]:
    cumulativeCharCounts = [1 if C[0] == char else 0] * N
    
    for i in range(1, N):
        # If the current character is the same as the given character, add 1 to the cumulative count
        cumulativeCharCounts[i] = cumulativeCharCounts[i - 1] + (C[i] == char)
    
    return cumulativeCharCounts