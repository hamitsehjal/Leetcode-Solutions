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

        def backtrack(start: int, path: list):
            if start == len(s):
                res.append(path.copy())
                return

            for end in range(start + 1, len(s)+1):
                substring = s[start:end]
                if isPalindrome(substring):
                    path.append(substring)
                    backtrack(end,path)
                    path.pop()
        
        backtrack(0,[])
        return res
