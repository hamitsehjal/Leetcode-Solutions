class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        Safety as a relationship
        - a node is safe if all the nodes that it points to are safe
        - 0 is safe, if 1,2 are safe
            1 -> 0
            2 -> 0
        - 1 is safe, if 2,3 are safe
            2 -> 1
            3 -> 1
        - 2 is safe, if 5 is safe
            5 -> 2
        - 3 is safe, if 0 is safe
            0 -> 3
        - 4 is safe, if 5 is safe
            5 -> 4
        - 5 is safe, no prerequiste
        - 6 is safe, no prerequisite

        """
        indegrees = {u: 0 for u in range(len(graph))}
        neigbhours = defaultdict(list)

        for u,dependencies in enumerate(graph):
            for v in dependencies:
                # dependency(v) -> dependent(u)
                indegrees[u] += 1
                neigbhours[v].append(u)
        
        queue = deque([u for u in indegrees if indegrees[u] == 0])
        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for nei in neigbhours[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    queue.append(nei)
        
        return sorted(topo_order)



        
