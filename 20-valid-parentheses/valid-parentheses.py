class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in brackets:
                # closing bracket
                if not stack or brackets[ch] != stack[-1]:
                    return False

                stack.pop()
            else:
                stack.append(ch)
        
        return True if not stack else False