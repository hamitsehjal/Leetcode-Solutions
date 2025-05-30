class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(start, cur):
            if len(cur) == len(digits):
                ans.append("".join(cur))
                return

            for i in range(start, len(digits)):
                digit = digits[i]
                for letter in letterMap[digit]:
                    cur.append(letter)
                    backtrack(i + 1, cur)
                    cur.pop()

        ans = []
        backtrack(0, [])
        return ans
