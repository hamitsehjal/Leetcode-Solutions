class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,n-1

        while l < r:
            mid = l + (r-l)//2
            if self.isGreater(mid,n,nums):
                r = mid
            else:
                l = mid + 1
        
        return l
    
    def isGreater(self,i,n,nums):
        if i == n - 1:
            return true
        
        return nums[i] > nums[i+1]
        