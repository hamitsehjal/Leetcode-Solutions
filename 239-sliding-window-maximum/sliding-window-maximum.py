class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # monotonic non-increasing queue
        ans = []

        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()
            
            # only add to answer if the window has reached the size k
            if i >= k-1:
                ans.append(nums[queue[0]])
            
        return ans