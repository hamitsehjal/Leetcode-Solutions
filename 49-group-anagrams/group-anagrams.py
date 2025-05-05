class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = collections.defaultdict(list)

        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord("a")] += 1

            group[tuple(key)].append(word)

        ans = []
        for key, val in group.items():
            ans.append(val)

        return ans
