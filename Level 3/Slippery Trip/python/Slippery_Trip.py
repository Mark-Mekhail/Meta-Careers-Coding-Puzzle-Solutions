from typing import List

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
    maxEndingRowCoinCount = 0  # The maximum number of coins you can collect if your trip ends on a given row (by lasting forever on that row)
    runningCoinCount = 0  # The maximum number of coins that you can collect without ending on a row
    for row in G:
        if "v" in row:
            rowMaxCollectableCoinCount = 1 if "*" in row else 0

            # Find the maximum number of coins that can be collected in a row before leaving it
            start = row.index("v") - 1  # Start from the cell before a "v" and move left
            curCoinCount = 0
            for j in range(C):
                index = (C + start - j) % C
                cur = row[index]

                if cur == "*":
                    curCoinCount += 1
                elif cur == ">":
                    # If you enter a ">" cell on a row, you will end on the row and collect all coins between the ">" and the last "v" cell
                    rowMaxCollectableCoinCount = max(rowMaxCollectableCoinCount, curCoinCount)
                elif cur == "v":
                    # A "v" cell will move you on to the next row so no uncollected coins to the right of it will be collected
                    curCoinCount = 0

            runningCoinCount += rowMaxCollectableCoinCount
        else:
            if ">" in row:
                # If there is no "v" in the row and you enter it on a ">" you will end on the row and collect all coins on it
                maxEndingRowCoinCount = max(runningCoinCount + row.count("*"), maxEndingRowCoinCount)

            if "*" in row:
                # You can always collect a coin from a row as long as there is a coin in it
                runningCoinCount += 1
            elif "." not in row:
                # The row only has ">" cells so you cannot proceed further down
                break

    return max(maxEndingRowCoinCount, runningCoinCount)