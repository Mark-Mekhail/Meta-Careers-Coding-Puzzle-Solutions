def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    count = 0
    
    cumulative_ps = [1 if C[0] == 'P' else 0]
    cumulative_bs = [1 if C[0] == 'B' else 0]
    
    for i in range(1, N):
        cur = C[i]
        cumulative_ps.append(cumulative_ps[i - 1] + (1 if cur == 'P' else 0))
        cumulative_bs.append(cumulative_bs[i - 1] + (1 if cur == 'B' else 0))
    
    cumulative_aps = [0]
    cumulative_abs = [0]
    
    for i in range(1, N - X):
        cumulative_aps.append(cumulative_aps[i - 1])
        cumulative_abs.append(cumulative_abs[i - 1])
        
        if i >= X and C[i] == 'A':
            start = min(i + X - 1, N - 1)
            end = min(i + Y, N - 1)
            cumulative_aps[i] += cumulative_ps[end] - cumulative_ps[start]
            cumulative_abs[i] += cumulative_bs[end] - cumulative_bs[start]
    
    for i in range(N - 2 * X):
        cur = C[i]
        if cur == 'P' or cur == 'B':
            opposite = 'B' if cur == 'P' else 'P'
            start = min(i + X - 1, N - X - 1)
            end = min(i + Y, N - X - 1)
            if opposite == 'B':
                count += cumulative_abs[end] - cumulative_abs[start]
            else:
                count += cumulative_aps[end] - cumulative_aps[start]
    
    return count