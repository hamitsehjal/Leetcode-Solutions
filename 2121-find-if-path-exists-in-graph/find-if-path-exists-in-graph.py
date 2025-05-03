class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        if source == destination:
            return True
            
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True

            ans = False

            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    if dfs(neighbor):
                        ans = True

            return ans

        visited = set([source])
        return dfs(source)
