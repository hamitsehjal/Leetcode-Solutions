class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # monotonic strictly decreasing stack
        maxArea = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                stack_top = stack.pop()

                if stack:
                    # stack[-1] represent the previous greater element for stack_top
                    # i represent the next greater element for stack_top
                    h = min(height[i], height[stack[-1]]) - height[stack_top]
                    w = i - (stack[-1] + 1)
                    maxArea = maxArea + (w*h)
                
            stack.append(i)
        
        return maxArea
