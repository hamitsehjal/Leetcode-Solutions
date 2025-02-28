class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if target > nums[hi]:
            return hi + 1
        if target < nums[lo]:
            return lo
        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        return lo
