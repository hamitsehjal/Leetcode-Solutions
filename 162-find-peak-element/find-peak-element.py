class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r = -1,len(nums)-1

        def isGreater(i):
            if i == len(nums)-1:
                return True
            else:
                return nums[i] > nums[i+1]

        while l+1 < r:
            mid = (l+r) // 2

            if isGreater(mid):
                r = mid
            else:
                l = mid
        
        return r
        