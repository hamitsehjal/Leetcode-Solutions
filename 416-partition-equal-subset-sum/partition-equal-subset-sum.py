class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        dp(0,target) -> Can we make target sum using elements from index i to end
        '''
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        dp = [[False]*(target+1) for _ in range(n+1)]

        # when sum is 0, we can always make it 
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(n-1,-1,-1):
            for cur_target in range(1,target+1):
                dp[i][cur_target] = dp[i+1][cur_target]

                if nums[i] <= target:
                    dp[i][cur_target] = dp[i][cur_target] or dp[i+1][cur_target-nums[i]]
        
        return dp[0][target]

        

        