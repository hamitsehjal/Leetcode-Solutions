from collections import Counter
from heapq import heappush,heappop

class Node:
    def __init__(self,count,word):
        self.count = count
        self.word = word
    
    def __lt__(self,other):
        if self.count != other.count:
            return self.count < other.count
        
        return self.word > other.word
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = [] # min-heap

        for word,count in counter.items():
            heappush(heap,Node(count,word))

            if len(heap) > k:
                heappop(heap)
        
        ans = []
        while heap:
            node = heappop(heap)
            ans.append(node.word)
        
        return ans[::-1]

        