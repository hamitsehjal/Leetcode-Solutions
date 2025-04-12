class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        """
        [1,2,3,5,6]
        """
        nums.sort()
        count = 1
        start = 0

        for i, num in enumerate(nums):
            if num > nums[start] + k:
                start = i
                count += 1

        return count
