from heapq import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) > 1:
            y = abs(heappop(heap))
            x = abs(heappop(heap))

            if y == x:
                continue
            else:
                heappush(heap, -(y - x))

        return abs(heap[0]) if len(heap) == 1 else 0
