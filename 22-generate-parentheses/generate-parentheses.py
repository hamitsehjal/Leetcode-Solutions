class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(cur, openn, close):
            if len(cur) == n * 2:
                ans.append("".join(cur))
                return

            if openn < n:
                cur.append("(")
                backtrack(cur, openn + 1, close)
                cur.pop()

            if openn > close:
                cur.append(")")
                backtrack(cur, openn, close + 1)
                cur.pop()

        backtrack([], 0, 0)
        return ans
