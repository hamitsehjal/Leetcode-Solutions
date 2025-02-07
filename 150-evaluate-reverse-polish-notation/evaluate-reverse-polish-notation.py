class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "/", "*"}

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                res = self.calculate(token, int(num1), int(num2))
                stack.append(res)
            else:
                stack.append(int(token))

        return stack[0]

    def calculate(self, operator: str, num1: int, num2: int) -> int:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "/":
            return math.trunc(num1 / num2)
        elif operator == "*":
            return num1 * num2
