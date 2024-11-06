class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(i,comb,target):
            if target == 0:
                ans.append(comb.copy())
                return
            
            if i >= len(candidates):
                return
            
            for j in range(i,len(candidates)):
                elem = candidates[j]
                if elem <= target:
                    comb.append(elem)
                    dfs(j,comb,target-elem)
                    comb.pop()
                   
        ans = []
        dfs(0,[],target)

        return ans
        