class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Observations
        - non-negative numbers
        - find a path with min total sum

        dp[2][2] = min(dp[1][2],dp[2][1]) + grid[2][2]
        """
        m, n = len(grid), len(grid[0])
        dp = [[0 for c in range(n)] for r in range(m)]
        dp[0][0] = grid[0][0]

        for r in range(m):
            for c in range(n):
                val_1, val_2 = float('inf'),float('inf')

                if 0 <= r - 1 < m:
                    val_1 = dp[r - 1][c]
                if 0 <= c - 1 < n:
                    val_2 = dp[r][c - 1]

                if val_1 == float('inf') and val_2 == float('inf'):
                    dp[r][c] = grid[r][c]
                else:
                    dp[r][c] = min(val_1, val_2) + grid[r][c]

        return dp[m - 1][n - 1]
