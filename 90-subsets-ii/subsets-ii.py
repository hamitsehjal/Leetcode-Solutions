class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(i,subset):
            if i == len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i+1,subset)

            subset.pop()

            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1

            backtrack(i+1,subset)

        ans = []
        nums.sort()
        backtrack(0,[])
        return ans


        