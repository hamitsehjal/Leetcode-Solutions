class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        stack = []
        n = len(nums)
        nextGreater = [-1] * n

        # for j in range(2 * n):
        #     i = j % n
        #     while stack and nums[stack[-1]] < nums[i]:
        #         stack_pop = stack.pop()
        #         nextGreater[stack_pop] = nums[i]

        #     stack.append(i)
        
        for _ in range(2):
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    stack_pop = stack.pop()
                    nextGreater[stack_pop] = nums[i]

                stack.append(i)


        return nextGreater
