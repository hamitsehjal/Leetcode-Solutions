class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Length -> count
        of longest substring without duplicate characters
        s = "abcabcbb"

        l = 0
        r = 0
        seen = {b,c,a}
        ans = 3
        """
        l = 0
        ans = 0
        seen = set()

        for r in range(len(s)):
            ch = s[r]

            while ch in seen:
                seen.remove(s[l])
                l += 1

            seen.add(ch)
            ans = max(ans, r - l + 1)

        return ans
