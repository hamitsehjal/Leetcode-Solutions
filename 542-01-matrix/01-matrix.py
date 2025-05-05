class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        ans = [[0 for _ in range(n)] for _ in range(m)]

        queue = collections.deque()
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited[r][c] = True

        while queue:
            r, c, steps = queue.popleft()
            ans[r][c] = steps

            for dr, dc in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nxt_r, nxt_c = r + dr, c + dc
                if (
                    nxt_r < 0
                    or nxt_r > m - 1
                    or nxt_c < 0
                    or nxt_c > n - 1
                    or visited[nxt_r][nxt_c]
                ):
                    continue

                visited[nxt_r][nxt_c] = True
                queue.append((nxt_r, nxt_c, steps + 1))

        return ans
