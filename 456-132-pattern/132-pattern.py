class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        nums = [3,1,4,2]

        i < j < k
        nums[i] < nums[k] < nums[j]

        for the current element (k)
        - find its previous greater element (j)
        - for this previous greater element, find the minimum element(i)
        - check if this minimum element (i) is < current elememnt(k)
        """

        stack = [] # monotonic strictly decreasing 
        minimums = [0]*len(nums) # index of minimum in the range(0-i)

        for i in range(len(nums)):
            if i == 0:
                minimums[0] == 0
            else:
                if nums[i] < nums[minimums[i-1]]:
                    minimums[i] = i
                else:
                    minimums[i] = minimums[i-1]

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                previous_greater_idx = stack[-1]
                minimum_element = nums[minimums[previous_greater_idx]]
                if minimum_element < nums[i]:
                    return True
                
            
            stack.append(i)
        
        return False


