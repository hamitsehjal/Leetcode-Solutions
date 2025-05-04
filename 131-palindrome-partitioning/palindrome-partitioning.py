class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        def dfs(comb, i):
            if i == len(s):
                ans.append(comb[:])
                return

            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    comb.append(s[i : j + 1])
                    dfs(comb, j + 1)
                    comb.pop()

        ans = []
        dfs([], 0)
        return ans

