import heapq as hq
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency = Counter(words)
        maxHeap = []

        for key,val in frequency.items():
            hq.heappush(maxHeap,(-val,key))
    
        
        ans = []
        for _ in range(k):
            ans.append(hq.heappop(maxHeap)[1])
        
        return ans
        