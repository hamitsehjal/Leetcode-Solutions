class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n // 2
        removed, count = 0, 0

        counter = collections.Counter(arr)
        heap = []
        for val in counter.values():
            heapq.heappush(heap, -val)

        while heap and removed < half:
            removed += -heapq.heappop(heap)
            count += 1

        return count
