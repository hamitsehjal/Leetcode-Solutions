# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallerDummy = ListNode(-101)
        greaterThanOrEqualDummy = ListNode(101)

        smaller = smallerDummy
        greaterEqual = greaterThanOrEqualDummy
        cur = head

        while cur:
            if cur.val < x:
                smaller.next = cur
                smaller = smaller.next
            else:
                greaterEqual.next = cur
                greaterEqual = greaterEqual.next
            
            cur = cur.next
        
        greaterEqual.next = None
        smaller.next = greaterThanOrEqualDummy.next # connecting end of smaller to start of greaterEqual

        return smallerDummy.next