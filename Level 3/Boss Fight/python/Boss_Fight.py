from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  curPair = [0, 1]
  curDamage = calculateDamage(H, D, 0, 1)
  damageIsSame = False
  while not damageIsSame:
    damageIsSame = True
    for i in range(N):
      if i != curPair[0]:
        damage = calculateDamage(H, D, curPair[0], i)
        if damage > curDamage:
          damageIsSame = False
          curDamage = damage
          curPair[1] = i
    curPair.reverse()
      
  return curDamage / B
  
def calculateDamage(H, D, warrior1, warrior2):
  return H[warrior1] * D[warrior1] + H[warrior2] * D[warrior2] + max(H[warrior1] * D[warrior2], H[warrior2] * D[warrior1])