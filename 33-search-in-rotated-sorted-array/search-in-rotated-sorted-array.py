class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                # l -> mid is sorted
                if target < nums[l] or target > nums[mid]:
                    # not in this set
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # mid + 1 -> r is sorted
                if target < nums[mid+1] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1
