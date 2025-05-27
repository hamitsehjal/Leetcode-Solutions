import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # Calculate Manhattan distance between two points
        def manhattan_distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        
        # Prim's algorithm
        visited = [False] * n
        min_heap = [(0, 0)]  # (cost, node_index)
        total_cost = 0
        
        while min_heap:
            cost, u = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            
            # Add node to MST
            visited[u] = True
            total_cost += cost
            
            # Add all edges from current node to unvisited nodes
            for v in range(n):
                if not visited[v]:
                    distance = manhattan_distance(u, v)
                    heapq.heappush(min_heap, (distance, v))
        
        return total_cost