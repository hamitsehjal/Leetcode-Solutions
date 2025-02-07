class Solution:
    def isValid(self, s: str) -> bool:
        braces = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for ch in s:
            if ch in braces:
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch != braces[stack.pop()]:
                    return False

        return True if not stack else False
