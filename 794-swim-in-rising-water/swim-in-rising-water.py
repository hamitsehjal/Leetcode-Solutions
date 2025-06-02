class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        pq = [[grid[0][0], 0, 0]]
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        visit = {(0,0)}

        while pq:
            height, row, col = heapq.heappop(pq)

            if row == N - 1 and col == N - 1:
                return height

            for dx, dy in directions:
                r, c = row + dx, col + dy
                if r < 0 or c < 0 or r > N - 1 or c > N - 1 or (r, c) in visit:
                    continue
                visit.add((r, c))
                heapq.heappush(pq, [max(height, grid[r][c]), r, c])
