import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        speed = 1
        while True:
            totaltime = 0
            for pile in piles:
                totaltime+= math.ceil(pile/speed)
            if totaltime<= h:
                return speed
            speed+=1
        return speed

        
piles = [3, 6, 7, 11]
h = 8
sol = Solution()
print(sol.minEatingSpeed(piles, h))

        