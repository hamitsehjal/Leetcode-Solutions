class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        We can solve this problem by keeping a pointer i that iterates through the array and another pointer nextNonZero that points to the position where the next non-zero element should be placed. We can then swap the elements at i and nextNonZero if the element at i is non-zero. This way, we can maintain the relative order of the non-zero elements while moving all the zeroes to the end of the array.
        
        """
        nextNonZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nextNonZero],nums[i] = nums[i],nums[nextNonZero]
                nextNonZero += 1
        

