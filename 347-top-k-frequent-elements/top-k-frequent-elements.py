import heapq as hq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums) # key(number) -> value(count)
        minHeap = []

        for key,val in frequency.items():
            hq.heappush(minHeap,(val,key))
            
            if len(minHeap) > k:
                hq.heappop(minHeap)
        
        return [key for val,key in minHeap]

            

        

        