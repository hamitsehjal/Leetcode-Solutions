class Solution:
    def numDecodings(self, s: str) -> int:
        def dp(i):
            if i in memo:
                return memo[i]

            if i == n:
                return 1
            ways = 0
            if s[i] != "0":
                # process the single digit i.e., s[i]
                ways += dp(i+1)

                if i + 1 < n and 1 <= int(s[i:i+2]) <= 26:
                    # process the double digit i.e., s[i:i+2] - eg 10,11, etc
                    ways += dp(i+2)
            
            memo[i] = ways
            return ways

        
        n = len(s)
        memo = {}

        return dp(0)
