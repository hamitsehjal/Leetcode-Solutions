class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(r, cols, diagonals, antiDiagonals):
            if r == n:
                return 1

            solutions = 0
            for c in range(n):
                if c in cols or (r - c) in diagonals or (r + c) in antiDiagonals:
                    continue

                cols.add(c)
                diagonals.add(r - c)
                antiDiagonals.add(r + c)

                solutions += backtrack(r + 1, cols, diagonals, antiDiagonals)

                cols.remove(c)
                diagonals.remove(r - c)
                antiDiagonals.remove(r + c)

            return solutions

        return backtrack(0, set(), set(), set())
