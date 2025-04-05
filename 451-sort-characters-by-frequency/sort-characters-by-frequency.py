class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        counter = sorted(counter.items(),key=lambda x: (-x[1],x[0]))

        ans = []
        for ch,cnt in counter:
            for _ in range(cnt):
                ans.append(ch)

        return "".join(ans)