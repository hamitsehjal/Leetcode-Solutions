class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i,num in enumerate(numbers):
            num2 = target - num
            if num2 in seen:
                return [seen[num2]+1,i+1]
            seen[num] = i
        
        
        