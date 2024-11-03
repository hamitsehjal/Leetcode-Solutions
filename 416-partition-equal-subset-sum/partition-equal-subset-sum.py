class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Tabulation(Bottoms-Up Approach) - Space Optimized
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        n = len(nums)
        prev = [[False]*(target+1) for _ in range(n)]
        prev = [False]*(target+1)

        prev[0] = True # Base case, sum of 0 can always be achieved
        
        if nums[0] <= target:
            prev[nums[0]] = True
        
        for i in range(1,n):
            cur = [False]*(target+1)
            for cur_target in range(1,target+1):
                notTaken = prev[cur_target]

                taken = False
                if nums[i] <= cur_target:
                    taken = prev[cur_target-nums[i]]

                cur[cur_target] = taken or notTaken

            prev = cur

        return prev[target]

        # # Tabulation(Bottoms-Up Approach)
        # total = sum(nums)
        # if total % 2 == 1:
        #     return False
        
        # target = total // 2
        # n = len(nums)
        # dp = [[False]*(target+1) for _ in range(n)]

        # for i in range(n):
        #     dp[i][0] = True
        
        # if nums[0] <= target:
        #     dp[0][nums[0]] = True
        
        # for i in range(1,n):
        #     for cur_target in range(1,target+1):
        #         # is it possible to build (target) using any elements before ith element?
        #         not_taken = dp[i-1][cur_target]
        #         # is it possible to build (target-nums[i]) using any elements before ith element?
        #         taken = False
        #         if nums[i] <= cur_target:
        #             taken = dp[i-1][cur_target-nums[i]]

        #         dp[i][cur_target] = taken or not_taken

        # return dp[n-1][target]

        # # Memoization (Top-Down Approach)
        # n = len(nums)
        # def dp(i,target):
        #     if target == 0:
        #         return True
        #     if i < 0 or target < 0:
        #         return False
            
        #     if memo[i][target] != -1:
        #         return memo[i][target]
        #     # is it possible to build (target) using any elements before ith element?
        #     not_taken = dp(i-1,target)
        #     # is it possible to build (target-nums[i]) using any elements before ith element?
        #     taken = dp(i-1,target-nums[i]) 

        #     memo[i][target] = taken or not_taken
        #     return memo[i][target]
    
        # total = sum(nums)
        # if total % 2 == 1:
        #     return False
        
        # target = total // 2
        # n = len(nums)
        # memo = [[-1]*(target+1) for _ in range(n)]

        # return dp(n-1,target)