class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # non-increasing queue
        ans = []

        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            if i-k >= queue[0]:
                queue.popleft()

            if i >= k-1:
                # valid window
                ans.append(nums[queue[0]])
        
        return ans