class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        group = collections.defaultdict(list)

        for word in strs:
            key = str(sorted(word))
            group[key].append(word)
        
        ans = []
        for key,val in group.items():
            ans.append(val)
        
        return ans

        