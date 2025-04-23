class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for num in nums:
                if num not in seen:
                    seen.add(num)
                    cur.append(num)
                    backtrack(cur)
                    seen.remove(cur.pop())

        res = []
        seen = set()
        backtrack([])

        return res
