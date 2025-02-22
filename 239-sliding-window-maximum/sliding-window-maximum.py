class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        queue = collections.deque() # monotonically decreasing queue
        res = []

        # for i in range(k):
        #     while queue and nums[queue[-1]] < nums[i]:
        #         queue.pop()
            
        #     queue.append(i)
        
        # res.append(nums[queue[0]]) # first entry

        l = 0
        for r in range(len(nums)):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            if r >= k:
                if l == queue[0]:
                    # maximum value
                    queue.popleft()
                l += 1

            if (r-l+1) == k:
                res.append(nums[queue[0]])
        
        print(res)
        return res
            
        