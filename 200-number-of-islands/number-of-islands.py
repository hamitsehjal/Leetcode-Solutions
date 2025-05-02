class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if (
                row < 0
                or row > ROWS - 1
                or col < 0
                or col > COLS - 1
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nxt_r, nxt_c = row + dx, col + dy
                dfs(nxt_r, nxt_c)

        islands = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1

        return islands
