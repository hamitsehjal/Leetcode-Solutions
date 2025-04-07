# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        heap = [] # min-heap

        for lst in lists:
            cur = lst
            while cur:
                heapq.heappush(heap,cur.val)
                cur = cur.next
            
        
        dummy = ListNode()
        cur = dummy
        
        while heap:
            val = heapq.heappop(heap)
            node = ListNode(val)
            cur.next = node
            cur = cur.next
        
        return dummy.next
