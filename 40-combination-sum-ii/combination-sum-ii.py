class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,comb,target):
            if target == 0:
                ans.append(comb[::])
                return

            for j in range(i,len(candidates)):
                elem = candidates[j]
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                if elem > target:
                    break
                
                comb.append(elem)
                dfs(j+1,comb,target-elem)
                comb.pop()
        
        candidates.sort()
        ans = []
        dfs(0,[],target)
        return ans