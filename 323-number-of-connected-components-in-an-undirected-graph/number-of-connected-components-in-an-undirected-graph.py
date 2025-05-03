class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        connectedComponents = 0

        for i in range(n):
            if i not in visited:
                self.dfs(i, visited, graph)
                connectedComponents += 1

        return connectedComponents

    def dfs(self, node, visited, graph):

        stack = [node]
        visited.add(node)

        while stack:
            n = stack.pop()

            for neighbor in graph[n]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
