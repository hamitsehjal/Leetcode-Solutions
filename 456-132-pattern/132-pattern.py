class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        '''
        subsequence: sequence derived by deleting some or no element from original sequence while keeping the order of remainaing elements intact

        i < j < k
        nums[i] < nums[k] < nums[k]


        For each element, find
        - Previous greater element of k
        - For this previous greater element, find its previous minimum eleement
        - If this previous minimum element is less than current element, we found 132 pattern
        '''

        minimums = [0] * len(nums)
        stack = []

        for i in range(len(nums)):
            if i == 0:
                minimums[0] = 0
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
        