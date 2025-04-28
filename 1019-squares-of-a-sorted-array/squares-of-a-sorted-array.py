class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        idx = len(nums) - 1
        i, j = 0, len(nums) - 1

        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                res[idx] = nums[j] * nums[j]
                j -= 1
            else:
                res[idx] = nums[i] * nums[i]
                i += 1

            idx -= 1

        return res
