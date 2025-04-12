class Solution:
    def maximum69Number(self, num: int) -> int:
        number = str(num)
        cur = num
        for i in range(len(number)):
            if number[i] == "6":
                new_version = number[:i] + "9" + number[i + 1 :]
                cur = max(cur, int(new_version))
        return cur
