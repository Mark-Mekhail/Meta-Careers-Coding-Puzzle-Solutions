from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
  curPair = [0, 1]
  curDamage = calculateDamage(H, D, 0, 1)
  damageIsSame = False
  while not damageIsSame:
    damageIsSame = True
    for order in range(2):
      for i in range(N):
        if i != curPair[order]:
          damage = calculateDamage(H, D, curPair[0], i) if order == 0 else calculateDamage(H, D, i, curPair[1])
          if damage > curDamage:
            damageIsSame = False
            curDamage = damage
            curPair[1-order] = i
            
    if damageIsSame:
      tmp = curPair[0]
      curPair[0] = curPair[1]
      curPair[1] = tmp
      for order in range(2):
        for i in range(N):
          if i != curPair[order]:
            damage = calculateDamage(H, D, curPair[0], i) if order == 0 else calculateDamage(H, D, i, curPair[1])
            if damage > curDamage:
              damageIsSame = False
              curDamage = damage
              curPair[1-order] = i
      
  return curDamage / B
  
  
def calculateDamage(H, D, first, second):
  return H[first] * D[first] + H[second] * D[second] + H[first] * D[second]