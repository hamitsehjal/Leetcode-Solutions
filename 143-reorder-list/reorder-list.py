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
        slow,fast = dummy,dummy.next

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
        list1 = dummy.next
        list2 = prev

        while list1 and list1.next:
            node_to_add = ListNode(list2.val)
            node_to_add.next = list1.next
            list1.next = node_to_add

            list1 = list1.next.next
            list2 = list2.next
        
        if list1 and list2:
            list1.next = list2
        