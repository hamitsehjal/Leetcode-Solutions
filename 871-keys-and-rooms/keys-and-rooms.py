class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        def dfs(i):
            for neighbor in rooms[i]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        visited = set([0])
        dfs(0)

        return len(visited) == len(rooms)
