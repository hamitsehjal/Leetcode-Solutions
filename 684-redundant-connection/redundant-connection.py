class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = {u + 1: u + 1 for u in range(n)}
        rank = {u + 1: 0 for u in range(n)}

        def find(u):
            if parent[u] == u:
                return u
            parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)

            if pu == pv:
                return False

            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
