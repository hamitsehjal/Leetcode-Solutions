class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            breath = r - l
            length = min(height[l], height[r])

            max_area = max(max_area, (breath * length))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
