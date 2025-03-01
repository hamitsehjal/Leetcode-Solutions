class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = -1, len(nums) - 1

        while lo + 1 < hi:
            mid = (lo + hi) // 2

            if nums[mid] <= nums[-1]:
                hi = mid
            else:
                lo = mid

        return nums[hi]
    