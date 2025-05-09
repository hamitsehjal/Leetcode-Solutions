class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph = collections.defaultdict(list)

        def dfs(node, target, cost, visited):
            if node == target:
                return cost

            visited.add(node)
            for nei, val in graph[node]:
                if nei not in visited:
                    result = dfs(nei, target, cost * val, visited)

                    if result is not None:
                        return result

            return None

        for i in range(len(equations)):
            node1, node2 = equations[i]
            value = values[i]

            graph[node1].append((node2, value))
            graph[node2].append((node1, 1 / value))

        ans = [-1.00000] * len(queries)

        print(graph)
        for i, query in enumerate(queries):
            n1, n2 = query[0], query[1]
            if n1 not in graph or n2 not in graph:
                continue
            res = dfs(n1, n2, 1, set())
            if res is not None:
                ans[i] = res

        return ans
