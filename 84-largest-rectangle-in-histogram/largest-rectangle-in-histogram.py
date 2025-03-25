class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        
        # left boundary : previous smaller element's index
        stack = [] # strictly increasing stack
        left_most = [-1]*len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                left_most[i] = stack[-1]
            
            stack.append(i)
        

        # right boundary: next smaller element's index
        stack = [] # non-decreasing stack
        right_most =[len(heights)]*len(heights)

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                stack_top = stack.pop()
                right_most[stack_top] = i
            
            stack.append(i)
        
        for i in range(len(heights)):
            left_most[i] += 1
            right_most[i] -= 1

            max_area = max(max_area,heights[i] * (right_most[i] - left_most[i] + 1))
        
        return max_area