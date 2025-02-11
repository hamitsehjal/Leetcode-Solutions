class Solution:
    def trap(self, height: List[int]) -> int:
        """
        We need to find area of section that can trap water
        - area = width X height

        """

        area = 0
        stack = []  # strictly decreasing stack

        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                stack_top = stack.pop()

                if stack:
                    h = min(height[stack[-1]], height[i]) - height[stack_top]
                    w = i - (stack[-1] + 1)

                    area += w * h

            stack.append(i)

        return area
