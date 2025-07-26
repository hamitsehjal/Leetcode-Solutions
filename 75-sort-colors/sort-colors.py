class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        0 -> red
        1 -> white
        2 -> blue
        """

        n = len(nums)
        count = {}
        for num in nums:
            count[num] = count.get(num,0) + 1
        
        idx = 0
        for color in [0,1,2]:
            for val in range(count.get(color,0)):
                nums[idx] = color
                idx += 1

        



        