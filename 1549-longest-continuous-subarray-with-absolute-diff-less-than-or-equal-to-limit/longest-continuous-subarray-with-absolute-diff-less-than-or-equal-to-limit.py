class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decreasing = deque() # track maximum
        increasing = deque() # track minimum

        l = ans = 0

        for r in range(len(nums)):
            while decreasing and nums[r] > decreasing[-1]:
                decreasing.pop()
            
            while increasing and nums[r] < increasing[-1]:
                increasing.pop()
            
            decreasing.append(nums[r])
            increasing.append(nums[r])

            while decreasing[0] - increasing[0] > limit:
                if nums[l] == decreasing[0]:
                    decreasing.popleft()
                if nums[l] == increasing[0]:
                    increasing.popleft()
                l += 1
            
            ans = max(ans,r-l+1)

        return ans