class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set() # c
        posDiags = set() # r+c
        negDiags = set() # r-c
        
        ans = []
        board = [['.']*n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return
            
            for c in range(n):
                if (c in cols or 
                    r+c in posDiags or
                    r-c in negDiags):
                    continue
                
                cols.add(c)
                posDiags.add(r+c)
                negDiags.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                cols.remove(c)
                posDiags.remove(r+c)
                negDiags.remove(r-c)
                board[r][c] = "."
            
        backtrack(0)
        return ans
