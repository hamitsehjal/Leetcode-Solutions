class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2

            prev_nei = float("-inf") if mid == 0 else nums[mid - 1]
            next_nei = float("-inf") if mid == n - 1 else nums[mid + 1]

            print(f"left - {l} | right - {r} | mid - {mid}")
            print(f"{prev_nei} | {nums[mid]} | {next_nei}")
            if nums[mid] > prev_nei and nums[mid] > next_nei:
                print("found answer")
                return mid
            elif next_nei > nums[mid]:
                l = mid + 1
                print("left incremented by 1")
            else:
                r = mid - 1
                print("right decrement by 1")

        """
        [-2147483648,-2147483647]
        l = 0 
        r = 1

        while 0 <= 1:
            mid = (0+1)//2 = 0
            prev_nei = float('-inf')
            next_nei = -2147483647

            if -2147483648 > float('-inf') and -2147483648 > -2147483647
        """
