class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo,hi = -1,len(nums)

        while lo+1 < hi:
            mid = lo + (hi - lo)//2

            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid
        
        return hi