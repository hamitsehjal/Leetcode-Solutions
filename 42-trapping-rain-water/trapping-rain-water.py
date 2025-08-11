class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        water_trapped = 0
        
        while left < right:
            if height[left] < height[right]:
                # Process left side
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Water can be trapped here
                    water_trapped += left_max - height[left]
                left += 1
            else:
                # Process right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Water can be trapped here
                    water_trapped += right_max - height[right]
                right -= 1
        
        return water_trapped