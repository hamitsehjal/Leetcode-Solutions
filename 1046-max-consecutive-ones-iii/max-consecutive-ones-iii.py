class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ans = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1

            while k < 0:
                # utilized all the flips
                if nums[l] == 0:
                    k += 1
                l += 1

            ans = max(ans,r - l + 1)

        print(ans)
        return ans
