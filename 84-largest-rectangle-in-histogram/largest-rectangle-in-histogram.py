class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # monotonic increasing stack
        max_area = 0

        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx,h = stack.pop()
                max_area = max(max_area,h * (i-idx))
                start = idx
            

            stack.append((start,height))
        
        while stack:
            idx,h = stack.pop()
            max_area = max(max_area,h*(len(heights)-idx))
        return max_area