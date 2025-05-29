class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        [ai, bi]
        bi(dependency) -> ai(dependant)
        """
        indegrees = {i: 0 for i in range(numCourses)}
        graph = defaultdict(list)

        for u,v in prerequisites:
            # v(dependency|preqrequiste) -> u(dependant|course)
            indegrees[u] += 1
            graph[v].append(u)

        queue = deque([u for u in indegrees if indegrees[u] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)

            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        if len(topo_order) == numCourses:
            return True
        
        return False