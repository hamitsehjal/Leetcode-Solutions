class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix = [1] * n

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]

        ans = [1] * n
        prefix = 1

        for i in range(n):
            ans[i] = prefix * postfix[i]
            prefix = prefix * nums[i]

        return ans
