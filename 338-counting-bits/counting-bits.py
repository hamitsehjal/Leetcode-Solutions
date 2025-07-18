class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(n + 1):
            ans[i] = self.countOnes(bin(i)[2:])

        return ans

    def countOnes(self, num: str):
        count = 0
        for char in num:
            if char == "1":
                count += 1

        return count
