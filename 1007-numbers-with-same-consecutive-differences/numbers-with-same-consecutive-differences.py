class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        ans = []

        def backtrack(cur):
            if len(cur) == n:
                digit = int("".join(map(str, cur)))
                ans.append(digit)
                return

            y1 = -k + cur[-1]
            if y1 >= 0 and y1 < 10:
                cur.append(y1)
                backtrack(cur)
                cur.pop()

            y2 = k + cur[-1]
            if y2 >= 0 and y2 < 10 and y2 != y1:
                cur.append(y2)
                backtrack(cur)
                cur.pop()

        for num in range(1,10):
            backtrack([num])

        return ans
