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

        def bfs(node):
            stack = [node]

            while stack:
                node = stack.pop()
                if node == destination:
                    return True
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

            return False

        visited = [False] * n
        visited[source] = True
        return bfs(source)
