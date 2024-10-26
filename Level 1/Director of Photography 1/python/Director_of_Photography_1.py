def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    for i in range(N - 2 * X):
        cur = C[i]
        if cur == 'P' or cur == 'B':
            opposite = 'B' if cur == 'P' else 'P'
            for j in range(i + X, min(i + Y + 1, N - X)):
                if C[j] == 'A':
                    for k in range(j + X, min(j + Y + 1, N)):
                        if C[k] == opposite:
                            count += 1
    return count