from typing import List

def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    maxDamageWarriors = [0, 1]  # Keeps track of the warrior pair found to deal the most damage
    maxDamageDealt = calculatePairMaxDamage(H, D, 0, 1)  # The damage dealt by the warrior pair found to deal the most damage
    damageImproved = True
    while damageImproved:
        damageImproved = False
        # Find the warrior that deals the most damage with the first warrior in the pair
        for _ in range(2):
            for i in range(N):
                if i != maxDamageWarriors[0]:
                    damage = calculatePairMaxDamage(H, D, maxDamageWarriors[0], i)
                    if damage > maxDamageDealt:
                        damageImproved = True
                        maxDamageDealt = damage
                        maxDamageWarriors[1] = i
            # Swap the warriors in the pair so the next search finds the best warrior matched with the best warrior found to pair with the current first warrior
            maxDamageWarriors.reverse()
    
    # Max damage dealt was calculated assuming B = 1, so scale the damage dealt to the actual value of B
    return maxDamageDealt / B
  
# Calculate the maximum damage dealt by a pair of warriors
def calculatePairMaxDamage(H: List[int], D: List[int], warrior1, warrior2):
    # Max damage dealt by a pair is H1*D2 + H2*D1 + max(H1*D2, H2*D1)
    return H[warrior1] * D[warrior1] + H[warrior2] * D[warrior2] + max(H[warrior1] * D[warrior2], H[warrior2] * D[warrior1])