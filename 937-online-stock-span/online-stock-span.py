class StockSpanner:

    def __init__(self):
        self.stack = []  # [idx,price]
        self.index = -1

    def next(self, price: int) -> int:
        self.index += 1
        if self.stack:
            while self.stack and self.stack[-1][1] <= price:
                self.stack.pop()

            if self.stack:
                previous_greater = self.stack[-1][0]
            else:
                previous_greater = -1

            self.stack.append([self.index, price])
            return self.index - previous_greater
        else:
            self.stack.append([self.index, price])
            return 1


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
