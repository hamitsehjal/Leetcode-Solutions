from heapq import *


class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap, -num)
        condition1 = abs(len(self.maxHeap) - len(self.minHeap)) > 1
        condition2 = (self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0])

        print(f"Condition 1 - {condition1} | Condition 2 - {condition2}")
        while abs(len(self.maxHeap) - len(self.minHeap)) > 1 or (self.maxHeap and self.minHeap and -self.maxHeap[0] > self.minHeap[0]):
            if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
                if len(self.maxHeap) > len(self.minHeap):
                    # remove from maxHeap
                    top = -heappop(self.maxHeap)
                    # add it to the minHeap
                    heappush(self.minHeap, top)
                else:
                    # remove from minHeap
                    top = heappop(self.minHeap)
                    # add it to the minHeap
                    heappush(self.maxHeap, -top)

            if -self.maxHeap[0] > self.minHeap[0]:
                # remove from maxHeap
                top = -heappop(self.maxHeap)
                # add to minHeap
                heappush(self.minHeap, top)

    def findMedian(self) -> float:
        # print(f"MaxHeap - {self.maxHeap}")
        # print(f"MinHeap - {self.minHeap}")
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        else:
            if len(self.maxHeap) > len(self.minHeap):
                return -self.maxHeap[0]
            else:
                return self.minHeap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
