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
            secondNxtNode = cur.next.next
            nxtNode = cur.next

            nxtNode.next = cur
            cur.next = secondNxtNode
            prev.next = nxtNode

            prev = cur
            cur = secondNxtNode
        
        return dummy.next
            
