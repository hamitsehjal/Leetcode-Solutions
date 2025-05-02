class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def dfs(node):
            for neighbor in range(len(isConnected)):
                if isConnected[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set()
        numOfProvinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                dfs(city)
                numOfProvinces += 1

        return numOfProvinces
