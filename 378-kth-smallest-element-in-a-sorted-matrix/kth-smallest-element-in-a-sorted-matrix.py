class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        for the kth smallest element, there needs to be k number of elements that less than or equal to kth element
        """
        heap = [] # max-heap
        n = len(matrix)

        for r in range(n):
            for c in range(n):
                heapq.heappush(heap,-(matrix[r][c]))

                if len(heap) > k:
                    heapq.heappop(heap)
        

        return -heap[0]
