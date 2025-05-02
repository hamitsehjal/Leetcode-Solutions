class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        roads = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
            roads.add((a, b))

        def dfs(city):
            roadsChanged = 0
            for neighbor in graph[city]:
                if neighbor not in visited:
                    if (neighbor, city) not in roads:
                        roadsChanged += 1

                    visited.add(neighbor)
                    roadsChanged += dfs(neighbor)

            return roadsChanged

        visited = {0}
        return dfs(0)
