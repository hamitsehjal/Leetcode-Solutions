class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the starting and ending positions of a given target value in a sorted array.
        """

        def find_first(nums, target):
            """
            Finds the first occurrence of the target using the minimization template.
            """
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid
            if lo < len(nums) and nums[lo] == target:
                return lo
            return -1

        def find_last(nums, target):
            """
            Finds the last occurrence of the target using the maximization template.
            """
            lo = 0
            hi = len(nums) - 1
            while lo < hi:
                mid = lo + (hi - lo + 1) // 2  # Bias towards right
                if nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid
            if lo < len(nums) and nums[lo] == target:
                return lo
            return -1

        first = find_first(nums, target)
        if first == -1:
            return [-1, -1]
        last = find_last(nums, target)
        return [first, last]
