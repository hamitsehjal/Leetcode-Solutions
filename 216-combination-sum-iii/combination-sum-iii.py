class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def backtrack(idx, comb, curSum):
            if len(comb) == k and curSum == n:
                ans.append(comb[:])
                return

            if curSum > n or len(comb) > k:
                return

            for num in range(idx, 10):
                if curSum+num <= n:
                    comb.append(num)
                    backtrack(num + 1, comb, curSum + num)
                    comb.pop()

        backtrack(1, [], 0)
        return ans
        