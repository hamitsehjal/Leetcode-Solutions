class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = collections.defaultdict(list)  # node maps to list of its neighbors

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if i != j and isConnected[i][j] == 1:
                    graph[i].append(j)

        def dfs(city):

            if city in visited:
                return

            visited.add(city)

            for nei in graph[city]:
                dfs(nei)

        visited = set()
        numOfProvinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                dfs(city)
                numOfProvinces += 1

        return numOfProvinces
