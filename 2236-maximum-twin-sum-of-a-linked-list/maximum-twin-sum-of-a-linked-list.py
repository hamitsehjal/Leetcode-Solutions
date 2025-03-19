# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        prev = None
        cur = slow.next
        slow.next = None # break off the ties

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        first = head
        second = prev

        ans = 0
        while second:
            ans = max(ans,first.val + second.val)
            first = first.next
            second = second.next
        
        return ans
