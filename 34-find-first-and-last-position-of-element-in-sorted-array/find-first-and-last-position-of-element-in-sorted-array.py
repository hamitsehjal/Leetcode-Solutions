class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.findFirstOccurence(nums, target)
        last = self.findLastOccurence(nums, target)

        print([first, last])
        return [first, last]

    def findFirstOccurence(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) // 2
            if nums[mid] >= target:  # Condition is True
                right = mid  # Look for an earlier True
            else:
                left = mid + 1  # Condition is False, look to the right
        if len(nums) == 0 or nums[left] != target:
            return -1
        return left

    def findLastOccurence(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        while left < right:
            # mid = left + (right - left + 1) // 2  # Bias towards the right
            mid = (left + right + 1) // 2  # Bias towards the right
            if nums[mid] <= target:  # Condition is True
                left = mid  # Look for a later True
            else:
                right = mid - 1  # Condition is False, look to the left
        if len(nums) == 0 or nums[left] != target:
            return -1
        return left
