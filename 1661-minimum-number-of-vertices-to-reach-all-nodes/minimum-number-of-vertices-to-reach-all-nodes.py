class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = collections.defaultdict(int)

        for _, y in edges:
            indegree[y] += 1

        return [i for i in range(n) if indegree[i] == 0]
