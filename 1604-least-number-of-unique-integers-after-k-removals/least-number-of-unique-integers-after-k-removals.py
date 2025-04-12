class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = []

        for num, count in counter.items():
            heapq.heappush(heap, [count, num])

        while k > 0 and len(heap) > 0:
            if heap[0][0] <= k:
                c, _ = heapq.heappop(heap)
                k -= c
            else:
                c, num = heapq.heappop(heap)
                heapq.heappush(heap, [c - k, num])
                k = 0

        return len(heap)
