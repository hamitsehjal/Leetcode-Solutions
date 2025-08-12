class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        s = "abccbcbb"
        {a}
        l = 0
        r = 0
        ans = 1

        ch = b
        {a,b}
        l=0,r = 1
        ans = max(1,1-0+1) = max(1,2) = 2

        ch = c
        {a,b,c}
        l=0,r=2
        ans = max(2,2-0+1) = max(2,3) = 3

        ch = c
        while ch in seen: true
            - seen.remove(s[0]) = seen.remove(a) = {b,c}
            - l = 1

            - seen.remove(s[1]) = seen.remove(b) = {c}
            - l = 2

            - seen.remove(s[2]) = seen.remove(c) = {}
            - l = 3
        
        {c}
        l = 3
        r = 3
        ans = max(3,1) = 3


        """
        l = 0
        seen = set()
        ans = 0

        for r in range(len(s)):
            ch = s[r]

            while ch in seen:
                # got a duplicate
                seen.remove(s[l])
                l += 1

            seen.add(ch)
            ans = max(ans, r - l + 1)

        return ans
