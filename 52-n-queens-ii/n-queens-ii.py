class Solution:
    def totalNQueens(self, n: int) -> int:
        

        def backtrack(r):
            if r == n:
                return 1

            ans = 0
            for c in range(n):
                if c not in cols and (r-c) not in diagonals and (r+c) not in antiDiagonals:
                    cols.add(c)
                    diagonals.add(r-c)
                    antiDiagonals.add(r+c)
                    ans += backtrack(r+1)
                    cols.remove(c)
                    diagonals.remove(r-c)
                    antiDiagonals.remove(r+c)
            
            return ans

        cols = set()
        diagonals = set()
        antiDiagonals = set()

        return backtrack(0)



            

