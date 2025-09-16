# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second part
        cur = slow.next
        slow.next = None # severe the ties

        prev = None

        while cur:
            nxtNode = cur.next
            cur.next = prev
            prev = cur
            cur = nxtNode
        

        # merge the parts
        cur1 = head
        cur2 = prev

        while cur1 and cur2:
            nxtNodeCur1 = cur1.next
            nxtNodeCur2 = cur2.next

            cur1.next = cur2
            cur2.next = nxtNodeCur1

            cur1 = nxtNodeCur1
            cur2 = nxtNodeCur2
        

        return head



        

        