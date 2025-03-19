# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        step = 1
        cur = dummy
        
        while step != left:
            cur = cur.next
            step += 1
        
        prev_left = cur # for future use
        
        cur = cur.next
        prev = None
        
        while step <= right:
            nxt_node = cur.next
            cur.next = prev
            prev = cur
            cur = nxt_node
            step += 1
        left = prev_left.next
        left.next = cur
        prev_left.next = prev
        
        return dummy.next