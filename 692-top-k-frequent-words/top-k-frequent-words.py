from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        
        # Push all words with negated frequency
        for word, cnt in freq.items():
            heappush(heap, (-cnt, word))
        
        # Pop the top k elements
        ans = []
        for _ in range(k):
            _, word = heappop(heap)
            ans.append(word)
        
        return ans