class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        deadends = set(deadends)
        deadends.add("0000")

        queue = collections.deque([("0000", 0)])

        while queue:
            comb, turns = queue.popleft()
            if comb == target:
                return turns

            for i in range(4):
                digit = int(comb[i])
                increment = (digit + 1) % 10
                decrement = (digit - 1) % 10

                increment_state = comb[:i] + str(increment) + comb[i + 1 :]
                decrement_state = comb[:i] + str(decrement) + comb[i + 1 :]

                if increment_state not in deadends:
                    deadends.add(increment_state)
                    queue.append((increment_state, turns + 1))

                if decrement_state not in deadends:
                    deadends.add(decrement_state)
                    queue.append((decrement_state, turns + 1))

        return -1
