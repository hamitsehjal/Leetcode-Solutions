class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # Given string
        # return - longest substring without duplicates
        
        # s = "abcabcbb"
        
        
        # s1 = "adebcbefgh"
        # s = " ", output: 0, expcted: 1
        
        """
        1. Try to pin the whole p
        Approach:
        charHash = {}
        
        two-pointers
        while ...
            if val in hashmap:
                # duplicate
            else:
            
        return ans
        
         - Time complexit
         - space complextiy 
        """
        
        """
        s = "a"; expected 1
        s1 = "abcd"
        
        # sliding window
        
        l=0
        for r in range(..):
            # add whatever is at r index to our curr window
            
            # while window is invalid:
                remove at l index
                increment l
            
            # update the anser
        
        return ans
        """
        # hash map -> {a:0, b: 1, c: 2}, set {}
        # charHash = {}
        seen = set()
        l, max_len = 0, 0
        """
        space -> O(len(s))
        time -> 
        abc
        2-0 + 1
        """
        # for r in range(len(s)):
        #     if s[r] in charHash and charHash[s[r]] != -1:
        #         # Duplicate
        #         fi = charHash[s[r]]
        #         while l <= fi:
        #             charHash[s[l]] = -1
        #             l += 1
        #     charHash[s[r]] = r
        #     max_len = max(max_len, r - l + 1)
        
        for r in range(len(s)):

            while s[r] in seen:
                # l <--> r
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            max_len = max(max_len,r-l+1)    
        
        return max_len
        
        