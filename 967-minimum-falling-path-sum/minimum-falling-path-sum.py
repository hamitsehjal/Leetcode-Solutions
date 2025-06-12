class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for c in range(n):
            dp[0][c] = matrix[0][c]
        
        for r in range(1,n):
            for c in range(n):
                if c == 0 and n == 1:
                    dp[r][c] = dp[r-1][c]
                if c == 0:
                    dp[r][c] = min(dp[r-1][c],dp[r-1][c+1]) 
                elif c == n-1:
                    dp[r][c] = min(dp[r-1][c],dp[r-1][c-1])
                else:
                    dp[r][c] = min(dp[r-1][c],dp[r-1][c-1],dp[r-1][c+1])
                
                dp[r][c] += matrix[r][c]
        
        return min(dp[n-1])
