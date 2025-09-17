class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        [1,2,3,4,5]
        [5,1,3]

        spell = 5

        """
        potions.sort()
        pairs = [0] * len(spells)

        for idx,spell in enumerate(spells):
            left = 0
            right = len(potions) - 1

            while left <= right:
                mid = (left + right) // 2

                if potions[mid] * spell >= success:
                    right = mid - 1
                else:
                    left = mid + 1
                
            
            pairs[idx] = len(potions) - left
        
        return pairs
    

                