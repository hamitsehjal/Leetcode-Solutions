class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,comb,total):
            if total == target:
                ans.append(comb.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            for j in range(i,len(candidates)):
                elem = candidates[j]
                comb.append(elem)
                dfs(j,comb,total+elem)
                comb.pop()

        ans = []
        dfs(0,[],0)
        return ans