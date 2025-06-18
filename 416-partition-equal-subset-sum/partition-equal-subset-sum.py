class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        n = len(nums)
        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]

        for i in range(1, n):
            dp[i][0] = True

        for idx in range(1, n + 1):
            for remaining_sum in range(1, target + 1):
                # skip it
                not_pick = dp[idx - 1][remaining_sum]
                # pick it
                pick = False
                if remaining_sum >= nums[idx-1]:
                    pick = dp[idx - 1][remaining_sum - nums[idx-1]]

                dp[idx][remaining_sum] = pick or not_pick

        return dp[n][target]
