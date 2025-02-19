class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [7,1,5,3,6,4]

        We start at 7,
        - if we come across larger value, that means we can make profit
        - if we come across smaller value, this would be the new buying point
        """
        if len(prices) == 1:
            return 0
        buying = profit = 0

        for selling in range(1, len(prices)):
            if prices[selling] < prices[buying]:
                buying = selling
            else:
                profit = max(profit, prices[selling] - prices[buying])

        return profit
