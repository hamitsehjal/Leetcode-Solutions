class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        3 main tasks
        - nums[i] + nums[j] + nums[k] == 0
        - i != j, i != k, j !=k
        - no duplicate triplets
        """

        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -num
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total > target:
                    r -= 1
                else:
                    l += 1
        

        return res





