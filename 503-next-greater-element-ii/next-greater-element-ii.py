class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = [] # monotonic non-increasing stack
        next_greater = [-1] * len(nums)

        for i in range(len(nums)*2):
            i = i % len(nums)
            while stack and nums[stack[-1]] < nums[i]:
                stack_top = stack.pop()
                next_greater[stack_top] = nums[i]
            
            stack.append(i)
        
        return next_greater