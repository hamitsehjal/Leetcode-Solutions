class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                cache[(r, c)] = 0

                if matrix[r][c] == "1":
                    right = helper(r, c + 1)
                    down = helper(r + 1, c)
                    diag = helper(r + 1, c + 1)

                    cache[(r, c)] = 1 + min(right, down, diag)

            return cache[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                helper(r, c)

        return max(cache.values()) ** 2
