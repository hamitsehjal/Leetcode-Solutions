class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        pairs = [0] * len(spells)

        for idx,spell in enumerate(spells):
            left = 0
            right = len(potions)

            while left < right:
                mid = (left + right) // 2

                if potions[mid] * spell >= success:
                    right = mid
                else:
                    left = mid + 1
                    
            pairs[idx] = len(potions) - left

        return pairs 