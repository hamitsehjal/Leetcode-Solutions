class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        if nums[lo] < target:
            lo += 1
            
        return lo
