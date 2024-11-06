class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,comb,target):
            if target == 0:
                ans.append(comb.copy())
                return
            
            if target < 0 or i >= len(candidates):
                return
            
            elem = candidates[i]
            comb.append(elem)

            dfs(i,comb,target-elem)

            comb.pop()
            dfs(i+1,comb,target)
        
        ans = []
        dfs(0,[],target)
        return ans
