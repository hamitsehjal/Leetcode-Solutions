class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        n = len(heights)

        # Find the next smaller
        next_smaller = [n] * n
        stack = [] # non-decreasing
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                stack_top = stack.pop()
                next_smaller[stack_top] = i
            
            stack.append(i)
        

        # Find the previous smaller
        prev_smaller = [-1] * n
        stack = [] # strictly increasing
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            
            if stack:
                prev_smaller[i] = stack[-1]
            
            stack.append(i)

        area = 0

        for i in range(len(heights)):
            next_s = next_smaller[i]
            prev_s = prev_smaller[i]


            next_s = next_s - 1
            prev_s = prev_s + 1

            width = next_s - prev_s + 1
            height = heights[i]

            area = max(area,height * width)
        
        return area