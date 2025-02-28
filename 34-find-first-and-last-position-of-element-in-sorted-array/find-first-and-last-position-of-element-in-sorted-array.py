class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)
        print(first,last)
        return [first, last]

    def findFirst(self, nums: List[int], target: int) -> int:
        lo, hi = -1, len(nums)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid

        return -1 if hi == len(nums) or nums[hi] != target else hi

    def findLast(self, nums: List[int], target: int) -> int:
        lo, hi = -1, len(nums)

        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] <= target:
                lo = mid
            else:
                hi = mid

        return -1 if lo == -1 or nums[lo] != target else lo
