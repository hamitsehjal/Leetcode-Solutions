class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans,cur = [],[]

        def backtrack(openn, close):
            if len(cur) == n * 2:
                ans.append("".join(cur))
                return

            if openn < n:
                cur.append("(")
                backtrack(openn + 1, close)
                cur.pop()

            if openn > close:
                cur.append(")")
                backtrack(openn, close + 1)
                cur.pop()

        backtrack(0, 0)
        return ans
