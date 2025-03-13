class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        while l < r:
            mid = l + (r-l) // 2

            if self.canEat(piles,h,mid):
                r = mid
            else:
                l = mid + 1

        return l

    def canEat(self, piles: List[int], h: int, k: int) -> int:
        count = 0
        for pile in piles:
            count += math.ceil(pile / k)
        
        print(f"Speed - {k} | Count - {count} | hours - {h}")
        return count <= h
