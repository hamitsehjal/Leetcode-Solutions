class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] > nums[l]:
                # l .... mid (sorted)

                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # mid ... right(sorted)
                if mid+1 < len(nums) and nums[mid+1] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            

        return -1


