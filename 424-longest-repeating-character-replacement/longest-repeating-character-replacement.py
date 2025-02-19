class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = ans = 0
        freq = {}
        max_f = 0

        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r],0)
            max_f = max(max_f,freq[s[r]])

            while (r-l+1) - max_f > k:
                # window is invalid
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans,r-l+1)
        
        return ans

        