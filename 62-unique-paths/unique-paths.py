class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Observations
        - The robot can only move either down or right at any point in time.
        """

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r - 1 >= 0 and r - 1 < m:
                    dp[r][c] += dp[r - 1][c]
                if c - 1 >= 0 and c - 1 < n:
                    dp[r][c] += dp[r][c - 1]

        return dp[m - 1][n - 1]
