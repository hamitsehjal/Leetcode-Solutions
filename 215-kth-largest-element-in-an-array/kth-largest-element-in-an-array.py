import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Convert into max-heap - O(N)
        Iterate k times
            - remove the root (max element) - O(log n)
        """

        heap = [-num for num in nums]
        heapq.heapify(heap)

        ans = None
        for _ in range(k):
            ans = heapq.heappop(heap)

        return -ans