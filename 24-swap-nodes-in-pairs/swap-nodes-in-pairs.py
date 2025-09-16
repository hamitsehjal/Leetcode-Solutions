# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        Swap every two adjacent nodes
        1 -> 2 -> 3 -> 4
        prev = None

        Edges-cases
        - Odd number of nodes
        - 0 nodes
        - 1 node
        """
        prev = ListNode()
        dummy = prev
        cur = head
        if cur and cur.next is None:
            return cur
            
        while cur and cur.next:
            nxtNode = cur.next
            secondNxtNode = cur.next.next

            prev.next = nxtNode
            nxtNode.next = cur
            cur.next = secondNxtNode

            prev = cur
            cur = secondNxtNode
        
        return dummy.next
            
