class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index, cur):
            res.append(cur[:])

            for i in range(index, len(nums)):
                cur.append(nums[i])
                backtrack(i + 1, cur)
                cur.pop()

        res = []
        backtrack(0, [])

        return res
