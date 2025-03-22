# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur_start = dummy

        while True:
            end = self.getKthGroup(cur_start,k)

            if not end:
                break
            
            cur_group_start = cur_start.next
            nxt_group_start = end.next

            cur = cur_start.next
            prev = None

            # reverse k nodes
            for _ in range(k):
                nxt_node = cur.next
                cur.next = prev
                prev = cur
                cur = nxt_node
                
            cur_group_start.next = nxt_group_start
            
            cur_start.next = end
            cur_start = cur_group_start

        return dummy.next
    
    def getKthGroup(self, cur: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        while cur and k > 0:
            cur = cur.next
            k -= 1

        return cur