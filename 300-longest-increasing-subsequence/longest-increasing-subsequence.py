# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
        
#         n = len(nums)
#         dp = [1] * n
#         for i in range(n-2,-1,-1):
#             for j in range(i+1,n):
#                 if nums[j] > nums[i]:
#                     dp[i] = max(dp[i],dp[j]+1)
        
#         return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
