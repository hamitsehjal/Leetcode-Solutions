class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # monotonic non-increasing stack
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack_top = stack.pop()
                ans[stack_top] = i - stack_top
            
            stack.append(i)
        
        return ans
