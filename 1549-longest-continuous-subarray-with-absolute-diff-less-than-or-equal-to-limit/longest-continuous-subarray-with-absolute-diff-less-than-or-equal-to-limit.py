class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_queue = collections.deque()  # monotonically decreasing
        min_queue = collections.deque()  # monotonically increasing
        ans = 0

        l, r = 0, 0

        while r < len(nums):

            # update max queue
            while max_queue and nums[max_queue[-1]] < nums[r]:
                max_queue.pop()
            max_queue.append(r)

            # update min queue
            while min_queue and nums[min_queue[-1]] > nums[r]:
                min_queue.pop()
            min_queue.append(r)

            while (
                max_queue
                and min_queue
                and abs(nums[max_queue[0]] - nums[min_queue[0]]) > limit
            ):
                if l == max_queue[0]:
                    max_queue.popleft()
                if l == min_queue[0]:
                    min_queue.popleft()

                l += 1

            ans = max(ans, r - l + 1)
            r += 1

        return ans
