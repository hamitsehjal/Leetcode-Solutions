class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(permutation):
            if len(permutation) == len(nums):
                ans.append(permutation[:])
                return
            
            for num in nums:
                if num not in permutation:
                    permutation.append(num)
                    dfs(permutation)
                    permutation.pop()
            
            
        
        ans = []
        dfs([])
        return ans