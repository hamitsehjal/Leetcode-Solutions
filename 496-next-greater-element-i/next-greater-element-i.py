class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Observations:
        1. nums1 is subset of nums2
        2. For each element of nums1
            - find the index j such that nums1[i] == nums2[j]
            - find th next greater element of nums2[j] in nums2
        
        for nums2, find the next greater element for each element - O(N)
        """
        ans = [-1] * len(nums1)
        next_greater_element = [-1] * len(nums2)
        stack = [] # monotonic non-increasing stack

        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                stack_top = stack.pop()
                next_greater_element[stack_top] = nums2[i]
            
            stack.append(i)
        
        indexMap = {}
        for idx,num in enumerate(nums2):
            indexMap[num] = idx
        
        for i in range(len(nums1)):
            j = indexMap[nums1[i]]
            ans[i] = next_greater_element[j]
        
        return ans