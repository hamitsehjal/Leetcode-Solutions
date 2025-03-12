class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the pivot index first
        l,r = 0,len(nums)-1

        while l < r:
            mid = l + (r-l) // 2

            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid + 1
        
        pivot = l

        # decide on range based on pivot
        if nums[0] <= target <= nums[pivot-1]:
            # left range
            l,r = 0,pivot-1

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        if nums[pivot] <= target <= nums[-1]:
            # right range
            l,r = pivot,len(nums)-1

            while l <= r:
                mid = l + (r-l)//2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
        