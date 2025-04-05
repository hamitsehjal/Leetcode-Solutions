from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)

        freq_sorted = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

        return [freq_sorted[i][0] for i in range(k)]
