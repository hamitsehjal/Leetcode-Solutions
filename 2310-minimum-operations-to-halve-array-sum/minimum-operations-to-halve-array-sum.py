from heapq import *


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        cur = total

        nums = [-num for num in nums]
        heapq.heapify(nums)
        operations = 0

        while cur > total / 2:
            max_num = abs(heappop(nums))
            cur = cur - max_num
            heappush(nums, -(max_num / 2))
            cur = cur + max_num / 2
            operations += 1

        return operations
