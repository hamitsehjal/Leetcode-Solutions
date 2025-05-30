class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        indegrees = {u : 0 for u in range(n)}
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegrees[u] += 1
            indegrees[v] += 1
        
        leaves = deque([u for u in indegrees if indegrees[u] == 1])

        while leaves and n > 2:

            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in graph[node]:
                    indegrees[nei] -= 1
                    if indegrees[nei] == 1:
                        leaves.append(nei)
        
        return list(leaves)