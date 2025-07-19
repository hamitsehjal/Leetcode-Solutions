class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dp(i):
            """
            return the number of ways to decode a string starting at index i and of length n
            """
            if i in memo:
                return memo[i]

            if i == n:
                return 1
            
            ways = 0
            if s[i] != "0":
                ways += dp(i+1)

                if i+1 < n and 1 <= int(s[i:i+2]) <= 26:
                    ways += dp(i+2)

            memo[i] = ways
            return ways
        
        n = len(s)
        memo = {}
        return dp(0)