class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        number of continuous subarrays - count
        What makes a valid subarray?
        - product of all elements in the subarray is strictly < k

        Example test case
        nums = [10,5,2,6], k = 100

        """
        if k <= 1:
            return 0

        l = 0
        cur = 1
        ans = 0
        for r in range(len(nums)):
            cur = cur * nums[r]

            while cur >= k:
                cur = cur // nums[l]
                l += 1
            
            ans = ans + (r-l+1)
        
        return ans
