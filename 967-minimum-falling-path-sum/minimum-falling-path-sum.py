class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [0] * n

        for c in range(n):
            dp[c] = matrix[0][c]
        
        for r in range(1,n):
            new_dp = [0] * n
            for c in range(n):
                if c == 0 and n == 1:
                    new_dp[c] = dp[c]
                if c == 0:
                    new_dp[c] = min(dp[c],dp[c+1])
                elif c == n-1:
                    new_dp[c] = min(dp[c],dp[c-1])
                else:
                    new_dp[c] = min(dp[c],dp[c+1],dp[c-1])
                
                new_dp[c] += matrix[r][c]
            
            dp = new_dp
        
        return min(dp)
