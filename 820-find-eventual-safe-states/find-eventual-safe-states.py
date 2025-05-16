class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        reversedGraph = collections.defaultdict(list)
        indegree = {}
        for i in range(len(graph)):
            indegree[i] = 0

        for idx,pair in enumerate(graph):
            for nei in pair:
                reversedGraph[nei].append(idx)
                indegree[idx] += 1
        

        queue = collections.deque([node for node in indegree if indegree[node] == 0])

        topo_order = []

        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for nei in reversedGraph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        

        return sorted(topo_order)
        


