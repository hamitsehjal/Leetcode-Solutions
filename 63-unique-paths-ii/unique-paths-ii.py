class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r - 1 >= 0 and r - 1 < m and obstacleGrid[r][c] != 1:
                    dp[r][c] += dp[r - 1][c]
                if c - 1 >= 0 and c - 1 < n and obstacleGrid[r][c] != 1:
                    dp[r][c] += dp[r][c - 1]

        return dp[m - 1][n - 1]