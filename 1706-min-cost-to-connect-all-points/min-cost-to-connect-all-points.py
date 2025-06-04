class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pq = [(0,0)] # (weight,node)
        n = len(points)
        visited = [False] * n
        total_cost = 0
        mst = []

        while pq:
            weight,u = heapq.heappop(pq)

            if not visited[u]:
                visited[u] = True
                total_cost += weight
                mst.append(u)
            
                for v,point in enumerate(points):
                    if not visited[v]:
                        distance = abs(point[0] - points[u][0]) + abs(point[1] - points[u][1])
                        heapq.heappush(pq,(distance,v))
        
        return total_cost
