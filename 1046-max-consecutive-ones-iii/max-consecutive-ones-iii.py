class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, ans = 0, 0
        flips = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flips += 1

            while flips > k:
                # utilized all the flips
                if nums[l] == 0:
                    flips -= 1
                l += 1

            ans = max(ans,r - l + 1)

        print(ans)
        return ans
