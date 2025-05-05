class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return -1

        queue = collections.deque([(0, 0, 1)])

        while queue:
            r, c, steps = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                # reached the end
                return steps

            for dr, dc in [
                [0, 1],
                [0, -1],
                [1, 0],
                [-1, 0],
                [-1, 1],
                [1, -1],
                [1, 1],
                [-1, -1],
            ]:
                nxt_r, nxt_c = r + dr, c + dc
                if self.inBounds(nxt_r, nxt_c, ROWS, COLS, grid):
                    grid[nxt_r][nxt_c] = 1
                    queue.append([nxt_r, nxt_c, steps + 1])

        return -1

    def inBounds(self, r, c, ROWS, COLS, grid):
        return r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == 0
