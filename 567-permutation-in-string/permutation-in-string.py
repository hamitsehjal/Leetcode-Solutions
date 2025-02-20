class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Comparing all permutations ❌ O(N!)
        hashmap of the s1 ✅ O(N^2)

        Fixed window question ✅

        Fair solution - comparing hashmpas - O(26 * N)
        - 26 since hash map cannot outgrow this based on question constraints

        Optimal Sliding window question
        - a really good trick (Coding)
        """

        if len(s1) > len(s2):
            # there is no way we could find a permutation that is lareger than the size of s2
            return False

        s1_count, s2_count = [0] * 26, [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1

        matches = sum([1 if s1_count[i] == s2_count[i] else 0 for i in range(26)])

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            s2_count[index] += 1

            if s1_count[index] == s2_count[index]:
                matches += 1

            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            s2_count[index] -= 1

            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1

            l += 1

        return matches == 26
