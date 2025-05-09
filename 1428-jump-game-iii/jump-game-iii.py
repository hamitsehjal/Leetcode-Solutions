class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)

        def neighbours(i):
            res = []
            jump1 = i + arr[i]
            jump2 = i - arr[i]

            if 0 <= jump1 < length:
                res.append(jump1)
            if 0 <= jump2 < length:
                res.append(jump2)

            return res

        queue = collections.deque([start])
        visited = set([start])

        while queue:
            node = queue.popleft()
            if arr[node] == 0:
                return True

            for nei in neighbours(node):
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False
