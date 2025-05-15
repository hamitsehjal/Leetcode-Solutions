class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        # creat a mapping course -> list of prerequisites
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        def dfs(crs):
            if visited[crs] == 1:
                # visiting again in the same dfs recursive chain
                return False

            if visited[crs] == 2:
                return True

            visited[crs] = 1

            for pre in graph[crs]:
                if not dfs(pre):
                    return False

            visited[crs] = 2
            return True

        visited = [0] * numCourses
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
