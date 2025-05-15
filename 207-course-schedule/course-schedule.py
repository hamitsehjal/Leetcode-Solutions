class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)

        indegree = {u: 0 for u in graph}

        for node in graph:
            for nei in graph[node]:
                indegree[nei] = indegree.get(nei, 0) + 1

        queue = collections.deque([node for node in indegree if indegree[node] == 0])

        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

        if len(topo_order) == len(indegree):
            return True

        return False
