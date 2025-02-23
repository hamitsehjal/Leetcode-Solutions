class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # non-increasing stack
        area = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                stack_top = stack.pop()
                if stack:
                    h = min(height[i], height[stack[-1]]) - height[stack_top]
                    w = i - (stack[-1] + 1)

                    area = area + (w*h)
                
            
            stack.append(i)
        

        return area
