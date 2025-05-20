class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph,indegrees = {},{}

        for i in range(numCourses):
            graph[i] = []
            indegrees[i] = 0
        
        for dep,pre in prerequisites:
            graph[pre].append(dep) # node -> list of nodes that depend on it
            indegrees[dep] += 1
        
        queue = collections.deque([key for key,val in indegrees.items() if val == 0])
        topoOrder = []
        
        while queue:
            course = queue.popleft()
            topoOrder.append(course)

            for dependant in graph[course]:
                indegrees[dependant] -= 1
                if indegrees[dependant] == 0:
                    queue.append(dependant)
            
        
        if len(topoOrder) != numCourses:
            return []
        
        return topoOrder