class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = [(0, 0, -1)]  # (weight,node,parent)
        n = len(points)
        visited = [False] * n
        total_cost = 0
        mst = []

        while pq and len(mst) < n - 1:
            weight, u, parent = heapq.heappop(pq)
            if not visited[u]:
                visited[u] = True
                if parent != -1:
                    total_cost += weight
                    mst.append((parent, u))

                for v, point in enumerate(points):
                    if not visited[v]:
                        distance = abs(point[0] - points[u][0]) + abs(
                            point[1] - points[u][1]
                        )
                        heapq.heappush(pq, (distance, v, u))

        return total_cost
