class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []  # monotonic strictly increasing
        ans = [0] * n

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                stack_top = stack.pop()
                ans[stack_top] = i-stack_top

            stack.append(i)

        return ans
