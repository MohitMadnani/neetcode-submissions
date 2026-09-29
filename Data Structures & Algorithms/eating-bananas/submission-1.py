import math

def isValidEatingRate(k,piles,h):
    thrs = 0
    for bananacount in piles:
        thrs += math.ceil(bananacount / k)
    return thrs <= h


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        k = 0

        while left <= right:
            mid = (left+right) // 2
            if isValidEatingRate(mid,piles,h):
                k = mid
                right = mid - 1
            else:
                left = mid + 1


        return k

        
        