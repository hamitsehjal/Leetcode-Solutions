class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l <= r:
            mid = l + (r-l)//2
            if mid == 0:
                prev = float('-inf')
            else:
                prev = nums[mid-1]
            
            if mid == n-1:
                next = float('-inf')
            else:
                next = nums[mid+1]
            
            if nums[mid] < next:
                l = mid + 1
            elif nums[mid] < prev:
                r = mid - 1
            else:
                return mid
        