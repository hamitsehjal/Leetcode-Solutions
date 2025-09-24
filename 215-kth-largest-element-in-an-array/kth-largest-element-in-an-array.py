import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Convert into max-heap - O(N)
        Iterate k times
            - remove the root (max element) - O(log n)
        """

        heap = []

        for num in nums:
            heapq.heappush(heap,num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]