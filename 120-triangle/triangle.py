class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        dp = [0] * ROWS
        for i, row in enumerate(triangle):
            dp[i] = [0] * len(row)

        dp[0][0] = triangle[0][0]

        for r in range(1, ROWS):
            cols = len(triangle[r])
            for c in range(cols):
                if 0 <= c - 1 < cols - 1 and 0 <= c < cols - 1:
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c])
                elif 0 <= c - 1 < cols - 1:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = dp[r - 1][c]

                dp[r][c] += triangle[r][c]

        return min(dp[ROWS - 1])
