class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            return []
            
        lettersMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        ans = []
        def backtrack(i,comb):
            if len(comb) == len(digits):
                ans.append("".join(comb.copy()))
                return
            
            digit = digits[i]
            for letter in lettersMap[digit]:
                comb.append(letter)
                backtrack(i+1,comb)
                comb.pop()
        
        backtrack(0,[])
        return ans

            

