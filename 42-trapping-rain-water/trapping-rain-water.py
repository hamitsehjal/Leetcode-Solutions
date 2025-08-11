class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        leftMax, rightMax = height[left], height[right]
        ans = 0
        
        while left < right:
            if leftMax < rightMax:
                # max(leftMax,rightMax) = leftMax, so we don't need to worry about right Max
                left += 1
                if height[left] < leftMax:
                    # water can be trapped
                    ans += leftMax - height[left]
                else:
                    leftMax = height[left]
            else:
                right -= 1
                if height[right] < rightMax:
                    # water can be trapped
                    ans += rightMax - height[right]
                else:
                    rightMax = height[right]
        
        return ans
