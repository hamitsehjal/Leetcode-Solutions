class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = collections.Counter(s)
        heap = [(-val, key) for key, val in counter.items()]
        heapq.heapify(heap)  # max-heap

        ans = ""
        prev_char = None
        prev_char_count = 0

        while heap:
            count, ch = heapq.heappop(heap)
            ans += ch

            if prev_char_count < 0:
                heapq.heappush(heap, (prev_char_count, prev_char))

            if count + 1 != 0:
                prev_char_count = count + 1
                prev_char = ch
            else:
                prev_char_count = 0
                prev_char = None

        if len(ans) == len(s):
            return ans

        return ""
