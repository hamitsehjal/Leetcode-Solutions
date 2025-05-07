class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """
        BFS visits a state in the minimum distance possible
        State is not always (r,c)
        """
        m, n = len(grid), len(grid[0])

        queue = collections.deque([(0, 0, 0, k)])
        visited = {(0, 0, k)}

        while queue:
            row, col, steps, removals = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps

            for dr, dc in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                r, c = row + dr, col + dc

                if r >= 0 and r < m and c >= 0 and c < n:
                    # in bounds
                    if grid[r][c] == 1:
                        if removals > 0 and (r, c, removals - 1) not in visited:
                            visited.add((r, c, removals - 1))
                            queue.append((r, c, steps + 1, removals - 1))
                    else:
                        # not an obstacle
                        if (r, c, removals) not in visited:
                            visited.add((r, c, removals))
                            queue.append((r, c, steps + 1, removals))

        return -1
