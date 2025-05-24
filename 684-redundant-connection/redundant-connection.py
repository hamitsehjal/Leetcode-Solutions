class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.parent = {}
        self.rank = {}

        ans = []
        for u,v in edges:
            if not self.union(u,v):
                ans.append([u,v])
        
        return ans[-1]

    def find(self, u):
        if u not in self.parent:
            self.parent[u] = u
            self.rank[u] = 0

        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self,u,v):
        pu = self.find(u)
        pv = self.find(v)

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
    

        
