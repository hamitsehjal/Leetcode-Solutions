class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,comb,total):
            if total == target:
                ans.append(comb.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            elem = candidates[i]
            comb.append(elem)
            dfs(i,comb,total+elem)
            comb.pop()
            dfs(i+1,comb,total)

        ans = []
        dfs(0,[],0)
        return ans