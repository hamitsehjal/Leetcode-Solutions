class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
         i < j < k
         where
         nums[i] < nums[k] < nums[j]
         1 3 2
        '''

        minimums = [-1]*len(nums)
        stack = [] # monotonic strictly decreasing

        for i in range(len(nums)):
            if i == 0:
                minimums[i] = 0
            else:
                if nums[i] < nums[minimums[i-1]]:
                    minimums[i] = i
                else:
                    minimums[i] = minimums[i-1]

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                if nums[minimums[stack[-1]]] < nums[i]:
                    return True
            
            stack.append(i)
        
        return False

        