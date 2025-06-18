class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2

        n = len(nums)
        dp = [False for _ in range(target + 1)]
        dp[0] = True

        for idx in range(1, n + 1):
            new_dp = dp[:]
            for remaining_sum in range(1, target + 1):
                # skip it
                not_pick = dp[remaining_sum]

                # pick it
                pick = False
                if remaining_sum >= nums[idx - 1]:
                    pick = dp[remaining_sum - nums[idx-1]]

                new_dp[remaining_sum] = pick or not_pick
            
            dp = new_dp[:]

        return dp[target]
