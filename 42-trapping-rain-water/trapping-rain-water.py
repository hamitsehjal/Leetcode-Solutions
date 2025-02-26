class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # non-decreasing stack
        area = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                stack_top = stack.pop()
                if stack:
                    # stack[-1] top of the stack is our left bounary
                    # stack_top (popped off value) is our gap
                    # height[i] current element is our right boundary
                    h = min(height[i], height[stack[-1]]) - height[stack_top]
                    w = i - (stack[-1] + 1)
                    area = area + (w * h)

            stack.append(i)

        return area
