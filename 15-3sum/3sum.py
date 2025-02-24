class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n logn)
        res = []
        
        for i,num in enumerate(nums):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -(num)

            l = i+1
            r = len(nums)-1

            while l < r:
                total = nums[l] + nums[r]

                if total == target:
                    print(f"i - {i} | l - {l} | r - {r}")
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        print(res)
        return res


        