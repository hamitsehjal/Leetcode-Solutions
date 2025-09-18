class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        max-speed = max(piles)
        min-speed = 1 bananaa/hour = total(piles)
        """

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_taken = self.count_hours(piles,mid)
            if hours_taken <= h:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def count_hours(self, piles: List[int], speed: int) -> int:
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / speed)
        
        return hours