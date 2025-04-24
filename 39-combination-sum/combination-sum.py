class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(index, cur, curSum):
            if curSum == target:
                ans.append(cur[:])
                return

            if curSum > target:
                return

            for i in range(index, len(candidates)):
                elem = candidates[i]
                if elem + curSum <= target:
                    cur.append(elem)
                    backtrack(i, cur, curSum + elem)
                    cur.pop()

        ans = []
        backtrack(0, [], 0)
        return ans
