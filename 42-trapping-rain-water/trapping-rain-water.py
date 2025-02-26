class Solution:
    def trap(self, height: List[int]) -> int:
        """
        We compute the max height on left and right for each bar
        Then, we can simply do min(maxLeft,maxRight) - bar's height
        If it's more than zero, that means water can by trapped othewise water cannot be trapped at that location
        """
        
        n = len(height)

        max_left = [0] * n
        max_right = [0] * n

        max_right[n-1] = 0

        for i in range(1,n):
            max_left[i] = max(max_left[i-1],height[i-1])
        
        for i in range(n-2,-1,-1):
            max_right[i] = max(max_right[i+1],height[i+1])
        
        res = 0
        for i in range(n):
            area = min(max_left[i],max_right[i]) - height[i]
            if area > 0:
                res += area
        
        return res

