class ListNode:
    def __init__(self,key=-1,val=-1,next=None,prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.count = 0
        self.head = ListNode(-1,-1) # LRU
        self.tail = ListNode(-1,-1) # MRU
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node:ListNode)->None:
        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self,node:ListNode)->None:
        prev = self.tail.prev

        node.next = self.tail
        node.prev = prev

        prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # remove node from list
            self.remove(node)

            # add node to the end of the list
            self.add(node)

            return node.val
        
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update the value in cache
            node = self.cache[key]
            self.remove(node)
            node = ListNode(key,value)
            self.add(node)
            self.cache[key] = node
        else:
            node = ListNode(key,value)
            self.add(node)
            self.cache[key] = node
            self.count += 1

            if self.count > self.cap:
                # remove the LRU
                lru = self.head.next
                self.remove(lru) # remove from linked list
                del self.cache[lru.key] # remove from hashmap
                self.count -= 1 # reduce the count




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)