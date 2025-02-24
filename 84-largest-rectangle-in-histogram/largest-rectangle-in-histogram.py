class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [] # monotonic increasing stack
        max_area = 0

        for i,height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > heights[i]:
                idx,h = stack.pop()
                max_area = max(max_area,h * (i-idx))
                start = idx
            

            stack.append((start,height))
        
        return max_area