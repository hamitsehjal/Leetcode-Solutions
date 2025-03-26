class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # strictly decreasing monotonic stack
        minimum = [-1] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                minimum[0] = nums[0]
            else:
                if nums[i] < minimum[i-1]:
                    minimum[i] = nums[i]
                else:
                    minimum[i] = minimum[i-1]
            
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                if minimum[stack[-1]] < nums[i]:
                    return True

            stack.append(i)
        
        return False