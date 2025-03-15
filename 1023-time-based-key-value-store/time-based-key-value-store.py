class TimeMap:

    def __init__(self):
        self.store = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        l,r = 0,len(pairs)-1

        while l < r:
            mid = l + (r-l+1)//2

            t = pairs[mid][0]

            if t <= timestamp:
                l = mid
            else:
                r = mid - 1
        
        if not pairs or pairs[l][0] > timestamp:
            return ""
        else:
            return pairs[l][1]
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# a -> [(1,bar)]
# x -> [(2,b)]
# get(b,3) 
#     pairs = [(2,b)]
#     l,r = 0,0
#     pairs[0][0] > timestamp
#     2 > 3
# foo -> []