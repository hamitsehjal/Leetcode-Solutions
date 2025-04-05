from collections import Counter,defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        buckets = defaultdict(list)

        for ch,cnt in counter.items():
            buckets[cnt].append(ch)

        ans = []

        for i in range(len(s),0,-1):
            for ch in buckets[i]:
                ans.append(ch*i)
        
        return "".join(ans)