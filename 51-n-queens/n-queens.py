class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        def backtrack(r, comb):
            if r == n:
                ans.append(["".join(col) for col in comb])
                return 

            for c in range(n):
                if (
                    c not in cols
                    and (r - c) not in diagonals
                    and (r + c) not in antiDiagonals
                ):
                    cols.add(c)
                    diagonals.add(r - c)
                    antiDiagonals.add(r + c)
                    comb[r][c] = "Q"

                    backtrack(r + 1, comb)

                    comb[r][c] = "."
                    cols.remove(c)
                    diagonals.remove(r - c)
                    antiDiagonals.remove(r + c)

        cols = set()
        diagonals = set()
        antiDiagonals = set()
        ans = []
        comb = [["." for _ in range(n)] for _ in range(n)]

        backtrack(0, comb)

        return ans
