class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def isPalindrome(s: str):
            l,r = 0,len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def backtrack(i,part):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i+1,len(s)+1):
                substring = s[i:j]
                if isPalindrome(substring):
                    part.append(substring)
                    backtrack(j,part)
                    part.pop()

        backtrack(0,[])
        return res
