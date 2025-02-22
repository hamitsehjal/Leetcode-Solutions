class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        """
        Confusion??
        1. when does the window becomes invalid?
        2. How to make the work inside the for loop - O(1)
        """

        freq_t, freq_s = {}, {}
        for ch in t:
            freq_t[ch] = 1 + freq_t.get(ch, 0)

        need, have = len(freq_t), 0

        l = 0
        res, res_len = "", float("inf")

        for r in range(len(s)):
            ch = s[r]
            freq_s[ch] = 1 + freq_s.get(ch, 0)

            if ch in freq_t and freq_t[ch] == freq_s[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res_len = r - l + 1
                    res = s[l : r + 1]
                ch = s[l]
                freq_s[ch] -= 1
                if ch in freq_t and freq_t[ch] > freq_s[ch]:
                    have -= 1
                l += 1

        return res
