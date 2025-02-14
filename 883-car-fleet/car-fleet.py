class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []  # next smaller or equal -> monotonic strictly increasing stack
        for pos, spd in pair:
            arrival_time = (target - pos) / spd
            if stack and stack[-1] >= arrival_time:
                continue
            stack.append(arrival_time)

        return len(stack)
