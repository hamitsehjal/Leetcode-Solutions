class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(node):
            if node in safe:
                return safe[node]

            safe[node] = False

            for nei in graph[node]:
                if not dfs(nei):
                    return False

            safe[node] = True
            return True

        safe = {}
        ans = []

        for node in range(len(graph)):
            if dfs(node):
                ans.append(node)

        return ans
