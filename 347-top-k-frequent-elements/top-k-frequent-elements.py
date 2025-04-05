from heapq import heappush,heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        
        heap = [] # min-heap (pop off the one's with lowest freq)

        for key,val in freq.items():
            heappush(heap,(val,key))

            if len(heap) > k:
                heappop(heap)
        
        ans = []

        while heap:
            _,num = heappop(heap)
            ans.append(num)
        
        return ans

