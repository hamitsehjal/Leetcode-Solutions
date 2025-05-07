class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        redGraph = collections.defaultdict(list)
        blueGraph = collections.defaultdict(list)

        for a, b in redEdges:
            redGraph[a].append(b)

        for a, b in blueEdges:
            blueGraph[a].append(b)

        ans = [-1] * n
        queue = collections.deque([(0, 0, "RED"), (0, 0, "BLUE")])
        visited = {(0, "RED"), (0, "BLUE")}

        while queue:
            node, steps, color = queue.popleft()
            if ans[node] == -1:
                ans[node] = steps

            if color == "RED":
                # use blue-graph
                for nei in blueGraph[node]:
                    if (nei, "BLUE") not in visited:
                        visited.add((nei, "BLUE"))
                        queue.append((nei, steps + 1, "BLUE"))
            else:
                # use red-graph
                for nei in redGraph[node]:
                    if (nei, "RED") not in visited:
                        visited.add((nei, "RED"))
                        queue.append((nei, steps + 1, "RED"))

        return ans
