class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            h1, h2 = height[l], height[r]
            res = max(res, (r - l) * min(h1, h2))

            if h1 < h2:
                l += 1
            else:
                r -= 1

        return res
