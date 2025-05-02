class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = {}
        for i in range(n):
            indegree[i] = 0

        for x, y in edges:
            indegree[y] += 1

        return [node for node, count in indegree.items() if count == 0]
