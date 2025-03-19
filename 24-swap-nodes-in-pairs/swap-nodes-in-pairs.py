# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev,cur = dummy,head

        while cur and cur.next:

            # save the ptrs
            nxt_pair = cur.next.next
            second = cur.next

            # reverse the current pair
            second.next = cur
            cur.next = nxt_pair
            prev.next = second

            # update the ptrs
            prev = cur
            cur = nxt_pair
            
        return dummy.next