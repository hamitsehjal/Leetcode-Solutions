from heapq import heapify, heappush, heappop


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)  # min-heap
        cost = 0

        while len(sticks) > 1:
            x = heappop(sticks)
            y = heappop(sticks)
            cost += x + y
            heappush(sticks, x + y)

        return cost
