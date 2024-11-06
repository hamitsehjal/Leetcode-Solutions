class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[::])
                return

            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)
                    backtrack(curr)
                    seen.remove(curr.pop())

        ans = []
        seen = set()
        backtrack([])
        return ans
        