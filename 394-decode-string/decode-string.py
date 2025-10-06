class Solution:
    def decodeString(self, s: str) -> str:
        
        cur_string = ""
        cur_count = 0
        stack = []

        for ch in s:
            if ch == "[":
                stack.append(cur_string)
                stack.append(cur_count)

                cur_string = ""
                cur_count = 0

            elif ch == "]":
                count = stack.pop()
                val = stack.pop()

                cur_string = cur_string * count
                cur_string = val + cur_string

            elif ch.isdigit():
                cur_count = cur_count * 10 + int(ch)
            else:
                cur_string += ch
        
        return cur_string