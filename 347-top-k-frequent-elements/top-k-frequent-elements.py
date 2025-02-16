class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        [1,1,1,2,2,3], k = 2

        1. Build a hashmap mapping element to its frequency
            O(N)
            {
                1 -> 3
                2 -> 2
                3 -> 1
            }

        2. Convert the hashmap into a list of pairs (integer,frequency)
        [(1,3),(2,2),(3,1)] - O(n)

        3. Sort the above array based on the frequency in reverse order
        [(1,3),(2,2),(3,1)] - O(n logn)

        4. Build up the resultant array - O(k)
        """

        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        pairs = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

        ans = []
        for i in range(k):
            ans.append(pairs[i][0])
        
        return ans

