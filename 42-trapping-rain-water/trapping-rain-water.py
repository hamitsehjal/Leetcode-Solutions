class Solution:
    def trap(self, height: List[int]) -> int:
        """
        - How much water can be stored at each index?
        - For each index, we need to calculate the highest bar on left and right of each index
        """

        n = len(height)
        left = [0]*n
        right = [0]*n

        # each value corresponds to the height of the heighest bar to left of it
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
            cur_h = height[i]
            left_h = left[i]
            right_h = right[i]

            if left_h > cur_h and right_h > cur_h:
                ans += min(left_h,right_h) - cur_h
        
        return ans
