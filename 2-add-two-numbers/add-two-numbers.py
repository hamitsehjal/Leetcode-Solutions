# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        carry = 0

        cur = dummy
        while l1 or l2 or carry > 0:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            total = l1_val + l2_val + carry
            if total > 9:
                # 18, 1 should be carry over and 8 should be the val
                val = total % 10
                carry = total // 10
            else:
                val = total
                carry = 0
                
            node = ListNode(val)
            cur.next = node

            # update the pointers
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        
        return dummy.next
