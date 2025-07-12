class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        L = len(word)

        def backtrack(r: int, c: int, idx: int, path: set) -> bool:
            """ """
            if idx == L:
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False

            if (r, c) in path:
                return False

            if board[r][c] != word[idx]:
                return False

            path.add((r, c))
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                nxt_r, nxt_c = r + dx, c + dy
                if backtrack(nxt_r, nxt_c, idx + 1,path):
                    return True
                
            path.remove((r,c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0, set()):
                        return True
        return False
