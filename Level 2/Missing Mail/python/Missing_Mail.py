from typing import List

def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    max_expected_profits_from_start = [0] * (N + 1)
    
    for i in range(N - 1, -1, -1):
        expected_mail_value = 0
        for j in range(i, N):
            expected_mail_value = (1 - S) * expected_mail_value + V[j]
            max_expected_profit_if_sold_today = expected_mail_value - C + max_expected_profits_from_start[j + 1]
            if max_expected_profit_if_sold_today > max_expected_profits_from_start[i]:
                max_expected_profits_from_start[i] = max_expected_profit_if_sold_today
    
    return max_expected_profits_from_start[0]
