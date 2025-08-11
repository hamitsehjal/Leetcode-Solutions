class Solution:
    def trap(self, height: List[int]) -> int:
        """
        - height of the highest bar on the left
        - height of the highest bar on the right

        Approach 1:
        - during first cycle, for each index, the find the height of highest bar on the left
        - druing second cycle, for each index, find the height of the highest bar on the right

        - for final result,
        max_left < current height < max_right ??
        - min(max_left,max_right) - current_height
        - repeat the above process for each index - O(N)

        - O(3N) = O(N) linear time complexity
        - O(2N) = O(N) space for storing those left and right maxiums
        """
        n = len(height)
        maxHeightsLeft = [0]*n
        maxHeightsRight = [0]*n

        cur_max = height[0]
        for i in range(1,n):
            maxHeightsLeft[i] = cur_max
            cur_max = max(cur_max,height[i])
            
        

        cur_max = height[n-1]
        for i in range(n-2,-1,-1):
            maxHeightsRight[i] = cur_max
            cur_max = max(cur_max,height[i])
        
        ans = 0
        for i in range(n):
            max_l = maxHeightsLeft[i]
            max_r = maxHeightsRight[i]
            cur_h = height[i]

            if cur_h < max_l and cur_h < max_r:
                area = min(max_l,max_r) - cur_h
                ans += area

        
        return ans
