class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map, s2_map = {}, {}

        for ch in s1:
            s1_map[ch] = 1 + s1_map.get(ch, 0)

        for i in range(len(s1)):
            ch = s2[i]
            s2_map[ch] = 1 + s2_map.get(ch, 0)

        if s2_map == s1_map:
            return True

        print(s1_map)
        print(s2_map)
        l = 0
        for r in range(len(s1),len(s2)):
            ch = s2[r]
            s2_map[ch] = 1 + s2_map.get(ch, 0)

            ch = s2[l]
            s2_map[ch] -= 1
            if s2_map[ch] == 0:
                del s2_map[ch]

            l += 1
            print(f" {l} | {r} | {s1_map}")
            print(f" {l} | {r} | {s2_map}")
            if s2_map == s1_map:
                return True

        return False
