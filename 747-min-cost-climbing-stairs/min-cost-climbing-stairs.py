class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(i):
            """
            return the minimum cost to reach step i
            """
            if i == 0:
                return 0
            if i == 1:
                return 0
            
            res = min(dp(i-1) + cost[i-1],dp(i-2) + cost[i-2])
            return res

        return dp(len(cost))
        
       