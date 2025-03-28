class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        t_map, s_map = {}, {}

        for ch in t:
            t_map[ch] = 1 + t_map.get(ch, 0)

        need, have = len(t_map), 0
        l = 0

        res, res_len = "", float("inf")
        for r in range(len(s)):
            ch = s[r]
            s_map[ch] = 1 + s_map.get(ch, 0)

            if ch in t_map and t_map[ch] == s_map[ch]:
                have += 1

            while have == need:
                if (r - l + 1) < res_len:
                    res = s[l : r + 1]
                    res_len = r - l + 1

                ch = s[l]
                s_map[ch] = s_map[ch] - 1

                if ch in t_map and t_map[ch] > s_map[ch]:
                    have -= 1

                l += 1
                
        return res
