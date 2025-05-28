import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = {i: [] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(y2 - y1) + abs(x2 - x1)
                graph[i].append([j, d])  # edge, distance
                graph[j].append([i, d])

        """
        # Prim's Algorithm
        1. Instantiate a priority Queue with an aribitrary node as starting point
        2. Instantiate a set/array to track the visited nodes
        """
        visited = [False] * len(points)
        minHeap = [(0, 0, -1)]  # weight,node,parent
        mst = []  # edges of minimum spanning tree
        total_weight = 0

        while minHeap and len(mst) < len(points) - 1:
            weight, node, parent = heapq.heappop(minHeap)

            if visited[node]:
                continue

            visited[node] = True
            if parent != -1:
                mst.append((parent, node, weight))  # parent,node,weight
                total_weight += weight

            for nei, wei in graph[node]:
                if visited[nei]:
                    continue
                heapq.heappush(minHeap, (wei, nei, node))

        return total_weight
