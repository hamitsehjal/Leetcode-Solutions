class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(capital):
            stack = [capital]
            visited = set([capital])
            roadChanged = 0

            while stack:
                city = stack.pop()
                for neighbor in graph[city]:
                    if neighbor not in visited:
                        if (neighbor, city) not in roads:
                            roadChanged += 1
                        visited.add(neighbor)
                        stack.append(neighbor)

            return roadChanged

        roads = set([(x, y) for x, y in connections])
        return dfs(0)
