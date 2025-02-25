class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        area = [0] * len(height)
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i - 1], height[i-1])

        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i + 1], height[i+1])
        

        for i in range(len(height)):
            area[i] = math.floor(min(maxLeft[i],maxRight[i]) - height[i])
            if area[i] < 0:
                area[i] = 0
            
        print(height)
        print(maxLeft)
        print(maxRight)
        print(area)
        return sum(area)
