class Solution:
    def trap(self, height: List[int]) -> int:
        """
        How much water can be trapped at each index
        - if we knew the hieght of the tallest bar on both left and right side of each index
        
        """
        n = len(height)
        left = [0] * len(height)
        right = [0] * len(height)

        max_h = height[0]
        for i in range(1,n):
            left[i] = max_h
            max_h = max(max_h,height[i])

        max_h = height[n-1]
        for i in range(n-2,-1,-1):
            right[i] = max_h
            max_h = max(max_h,height[i])
            

        ans = 0
        for i in range(n):
            l_max = left[i]
            h = height[i]
            r_max = right[i]
            if l_max > h and r_max > h:
                ans += min(r_max,l_max) - h

        return ans