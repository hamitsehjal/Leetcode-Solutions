class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ 
        num1 + num2 = target
        num2 = target - num1

        2 -> 0
        7 -> 1
        """
        seen = {}

        for idx,num in enumerate(nums):
            if (target-num) in seen:
                return [idx,seen[target-num]]
            seen[num] = idx
        
