class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []  # non-increasing stack
        area = 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                stack_top = stack.pop()
                if stack:
                    # stack[-1] is previous greater element
                    # height[1] is next greater
                    # stack_top is the gap
                    h = min(height[stack[-1]], height[i]) - height[stack_top]
                    w = i - (stack[-1] + 1)
                    area += h * w

            stack.append(i)

        return area
