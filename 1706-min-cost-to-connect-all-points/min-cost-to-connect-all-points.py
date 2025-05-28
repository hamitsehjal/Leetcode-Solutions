import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        """
        # Prim's Algorithm
        1. Instantiate a priority Queue with an aribitrary node as starting point
        2. Instantiate a set/array to track the visited nodes
        """
        visited = [False] * len(points)
        pq = [(0, 0)]  # weight,node,parent
        min_cost = 0

        while pq:
            weight, u = heapq.heappop(pq)

            if visited[u]:
                continue

            visited[u] = True
            min_cost += weight

            
            for v in range(len(points)):
                if not visited[v]:
                    dist = abs(points[u][0]-points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(pq,(dist,v))

        return min_cost
