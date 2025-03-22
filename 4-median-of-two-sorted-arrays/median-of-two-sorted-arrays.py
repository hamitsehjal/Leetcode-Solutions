class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res,n1,n2 = self.sortedArray(nums1,nums2)
        n = n1 + n2
        mid = n // 2
        if n%2 == 0:
            # even
            return (res[mid] + res[mid-1]) / 2
        else:
            return res[mid]


    
    def sortedArray(self, arr1: List[int], arr2: List[int]):
        n1,n2 = len(arr1),len(arr2)

        l1,l2,i = 0,0,0
        arr = [0] * (n1+n2)

        while l1 < n1 and l2 < n2:
            if arr1[l1] <= arr2[l2]:
                arr[i] = arr1[l1]
                l1 += 1
                i += 1
                
            else:
                arr[i] = arr2[l2]
                l2 += 1
                i += 1

        while l1 < n1:
            arr[i] = arr1[l1]
            l1 += 1
            i += 1

        while l2 < n2:
            arr[i] = arr2[l2]
            l2 += 1
            i += 1

        return (arr,n1,n2)