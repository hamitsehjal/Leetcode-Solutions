from collections import Counter
from heapq import heappush, heappop


class WordNode:
    def __init__(self, freq: int, word: str):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        heap = []  # min-heap(pop off the ones with less freq)
        for word, cnt in freq.items():
            heappush(heap, WordNode(cnt, word))

            if len(heap) > k:
                heappop(heap)

        ans = []

        print(heap)

        while heap:
            node = heappop(heap)
            ans.append(node.word)

        return ans[::-1]
