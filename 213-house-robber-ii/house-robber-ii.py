class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        # Edge case: only one house
        if n == 1:
            return nums[0]
        
        # Edge case: only two houses
        if n == 2:
            return max(nums[0], nums[1])
            
        # case 1: picking houses from 0 to n-2
        rob1 = self.helper(nums[: n - 1])
        # case 2: picking houses from 1 to n-1
        rob2 = self.helper(nums[1:])

        return max(rob1, rob2)

    def helper(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[n - 1]
