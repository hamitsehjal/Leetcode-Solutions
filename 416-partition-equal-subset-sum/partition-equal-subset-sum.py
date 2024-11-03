class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        def dp(i,target):
            if target == 0:
                return True
            if target < 0 or i >= len(nums):
                return False
            if memo[i][target] != -1:
                return memo[i][target]
            
            memo[i][target] = dp(i+1,target) or dp(i+1,target-nums[i])
            return memo[i][target]
        

        target = total // 2
        memo = [[-1]*(target+1) for _ in range(len(nums)+1)]
        return dp(0,target)

        