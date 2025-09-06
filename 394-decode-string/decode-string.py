class Solution:
    def decodeString(self, s: str) -> str:
        cur_string = ""
        cur_digit = ""
        stack = []

        for ch in s:
            if ch == "[":
                stack.append(cur_string)
                stack.append(int(cur_digit))
                cur_string = ""
                cur_digit = ""

            elif ch == "]":
                count = stack.pop()
                val = stack.pop()
                cur_string = cur_string * count
                cur_string = val + cur_string

            elif ch.isdigit():
                cur_digit += ch
            else:
                cur_string += ch
        
        return cur_string
