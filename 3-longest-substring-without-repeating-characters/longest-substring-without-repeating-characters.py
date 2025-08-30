class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Given string
        # return - longest substring without duplicates
        
        # s = "abcabcbb"
        
        
        # s1 = "adebcbefgh"
        # s = " ", output: 0, expcted: 1
        
        """
        s = "a"; expected 1
        s1 = "abcd"
        """
        # hash map -> {a:0, b: 1, c: 2}
        charHash = {}
        l, max_len = 0, 0
        
        for r in range(len(s)):
            if s[r] in charHash and charHash[s[r]] != -1:
                # Duplicate
                fi = charHash[s[r]]
                while l <= fi:
                    charHash[s[l]] = -1
                    l += 1
            charHash[s[r]] = r
            max_len = max(max_len, r - l + 1)
        
        return max_len
        
        