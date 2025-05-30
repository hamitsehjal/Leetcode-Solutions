
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(u):
            if parent[u] == u:
                return u
            
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u,v):
            pu,pv = find(u),find(v)

            if pu == pv:
                return
            
            if rank[pu] > rank[pv]:
                parent[pv] = pu
            elif rank[pu] < rank[pv]:
                parent[pu] = pv
            else:
                parent[pv] = pu
                rank[pu] += 1
        

        for u,v in edges:
            union(u,v)
        
        return len(set([find(i) for i in range(n)]))

            
