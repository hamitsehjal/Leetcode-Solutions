class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:

        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node):
            if node == destination:
                return True

            ans = False
            for nei in graph[node]:
                if not visited[nei]:
                    visited[nei] = True
                    if dfs(nei):
                        ans = True

            return ans

        visited = [False] * n
        return dfs(source)
