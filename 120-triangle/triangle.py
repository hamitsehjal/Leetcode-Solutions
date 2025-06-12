class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ROWS = len(triangle)
        dp = [0] * ROWS
        dp[0] = triangle[0][0]


        for r in range(1,ROWS):
            cols = len(triangle[r])
            new_dp = [0] * cols

            for c in range(cols):
                """
                For each position, we can come from:
                1. dp[c-1]: from upper left
                2. dp[c]: direct above
                """
                if c == 0:
                    # leftmost position, can only come from direct obove
                    new_dp[c] = dp[c]
                elif c == cols-1:
                    # rightmost position, can only come from upper left
                    new_dp[c] = dp[c-1]
                else:
                    new_dp[c] = min(dp[c],dp[c-1])
                
                new_dp[c] += triangle[r][c]
            
            dp = new_dp
        

        return min(dp)
