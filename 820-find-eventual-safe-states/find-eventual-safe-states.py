class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(node):
            if states[node] == 1:
                # visiting in same dfs chain
                return False
            
            if states[node] == 2:
                # safe node
                return True
            
            states[node] = 1

            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            states[node] = 2
            return True
        
        states = [0] * len(graph)
        
        for idx,node in enumerate(graph):
            if len(node) == 0:
                states[idx] = 2 # safe node
        

        ans = [] # collection of safe nodes

        for i in range(len(graph)):
            if not dfs(i):
                states[i] = 1
            else:
                states[i] = 2
                ans.append(i)

        return ans
        