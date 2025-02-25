class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_area = 0

        while l < r:
            max_area = max(max_area,(r-l)*min(height[l],height[r]))

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
            
        
        return max_area