class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, u):
        if self.parent[u] == u:
            return self.parent[u]

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv:
            return False

        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pu] < self.rank[pv]:
            self.parent[pu] = pv
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges = []  # u,v,weight

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                distance = abs(x2 - x1) + abs(y2 - y1)
                edges.append([i, j, distance])

        edges = sorted(edges, key=lambda x: x[2])
        uf = UnionFind(len(points))
        minCost = 0

        for u, v, w in edges:
            if uf.union(u, v):
                minCost += w
            else:
                continue

        return minCost
