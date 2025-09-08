class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [73,74,75,71,69,72,76,73]
        [0, 1, 2, 3, 4, 5, 6, 7]

        strictly decreasing
        """
        ans = [0] * len(temperatures)
        stack = [] # strictly decreasing stack

        for idx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                stack_top = stack.pop()
                ans[stack_top] = idx-stack_top
            
            stack.append(idx)
        

        return ans
