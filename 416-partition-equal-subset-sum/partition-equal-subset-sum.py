class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        def dp(i,target):
            if target == 0:
                return True
            if i < 0 or target < 0:
                return False
            
            if memo[i][target] != -1:
                return memo[i][target]
            # is it possible to build (target) using any elements before ith element?
            not_taken = dp(i-1,target)
            # is it possible to build (target-nums[i]) using any elements before ith element?
            taken = dp(i-1,target-nums[i]) 

            memo[i][target] = taken or not_taken
            return memo[i][target]
    
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        n = len(nums)
        memo = [[-1]*(target+1) for _ in range(n)]

        return dp(n-1,target)