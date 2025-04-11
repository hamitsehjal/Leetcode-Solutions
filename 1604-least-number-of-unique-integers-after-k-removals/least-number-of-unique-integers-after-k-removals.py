class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = []

        for num, count in counter.items():
            heapq.heappush(heap, [count, num])

        while k > 0:
            count, num = heapq.heappop(heap)
            count -= 1
            if count > 0:
                heapq.heappush(heap, [count, num])
            k -= 1

        return len(heap)
