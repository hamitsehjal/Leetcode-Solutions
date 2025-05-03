class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):

            ans = 1
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                r, c = row + dx, col + dy
                if r < 0 or r > ROWS - 1 or c < 0 or c > COLS - 1 or grid[r][c] == 0:
                    continue

                grid[r][c] = 0
                ans += dfs(r, c)

            return ans

        maxArea = float("-inf")
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    grid[row][col] = 0
                    maxArea = max(maxArea, dfs(row, col))

        return maxArea if maxArea != float("-inf") else 0
