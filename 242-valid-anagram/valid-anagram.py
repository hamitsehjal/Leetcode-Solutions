class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = collections.defaultdict(int)

        for ch in t:
            letters[ch] += 1
        

        
        
        for ch in s:
            if ch in letters:
                letters[ch] -= 1
                if letters[ch] == 0:
                    del letters[ch]
            else:
                return False
        
        return True if not letters else False
