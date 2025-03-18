# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(0,next=head)
        # Find the middle node
        slow,fast = dummy.next,dummy.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second part
        
        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # merge the two lists
        start = dummy.next
        end = prev

        while end:
            next_start = start.next
            next_end = end.next

            start.next = end
            end.next = next_start

            start = next_start
            end = next_end
        
        