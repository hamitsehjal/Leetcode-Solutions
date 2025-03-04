class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo,hi = 0,max(piles)
        while lo+1 < hi:
            mid = (lo + hi) // 2
            if self.canFinish(mid,piles,h):
                hi = mid
            else:
                lo = mid
        
        return hi
    
    def canFinish(self,speed,piles,maxHours):
        time = 0
        for pile in piles:
            time += math.ceil(pile/speed)

            if time > maxHours:
                return False
        
        return True