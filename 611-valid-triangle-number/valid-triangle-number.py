class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        [4,2,3,4]

        1. After Sorting
            - [2,2,3,4]
        
        2. We iterate over the input choosing each index as side a

        iteration 1:
        side a = 4

        side b = 3 (at index 1)
        side c = 2 (at index 3)

        Now, since a + b > c which is:
        3 + 2 > 4 -> true, so we found one triplet (3,2,4)
        but here's the thing we pick the smallest and the largest value in the remaining array we passed the check. 
        That means if we try with next smallest + largest, we would also pass the condition and so on

        so total number of combinations we would find would be :
        index of sice c - index of b
        i.e., in this case - 3 - 1 = 2

        Now,

        """
        nums.sort()
        res = 0

        for i in range(len(nums)-1,-1,-1):
            
            left = 0
            right = i - 1

            while left < right:

                c = nums[i]
                a = nums[left]
                b = nums[right]

                if a + b > c:
                    res += right - left
                    right -= 1
                else:
                    left += 1

        return res
