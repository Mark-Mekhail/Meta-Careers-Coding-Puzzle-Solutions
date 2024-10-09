from typing import List
# Write any import statements here

def getMaxCollectableCoins(R: int, C: int, G: List[List[str]]) -> int:
  maxEndCoinCount = 0
  coinCount = 0
  for i in range(R):
    row = G[i]

    if "v" in row:
      colCoinCount = 1 if "*" in row else 0

      start = row.index("v") - 1
      curCoinCount = 0
      for j in range(C):
        index = (C + start - j) % C
        cur = row[index]

        if cur == "*":
          curCoinCount += 1
        elif cur == ">":
          colCoinCount = max(colCoinCount, curCoinCount)
        elif cur == "v":
          curCoinCount = 0
      coinCount += colCoinCount
    else:
      if ">" in row:
        maxEndCoinCount = max(coinCount + row.count("*"), maxEndCoinCount)

      if "*" in row:
        coinCount += 1
      elif "." not in row:
        break

  return max(maxEndCoinCount, coinCount)