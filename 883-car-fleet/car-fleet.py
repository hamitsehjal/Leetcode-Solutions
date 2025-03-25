class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position,speed)]
        pairs = sorted(pairs,reverse=True)

        stack = [] # strictly increasing stack

        for i in range(len(pairs)):
            p,s = pairs[i]
            arrival_time = (target - p)/s

            # time = arrival_time
            while stack and stack[-1] >= arrival_time:
                arrival_time = stack.pop()

            stack.append(arrival_time)
        
        return len(stack)
            

        

    