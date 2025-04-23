class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        n = len(graph) - 1

        def dfs(node, cur):
            if node == n:
                res.append(cur[:])
                return

            for nei in graph[node]:
                cur.append(nei)
                dfs(nei, cur)
                cur.pop()

        res = []
        dfs(0, [0])
        return res
