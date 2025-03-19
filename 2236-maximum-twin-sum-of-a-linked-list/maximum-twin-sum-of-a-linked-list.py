# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast = head,head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            nxt_node = slow.next
            slow.next = prev
            prev = slow
            slow = nxt_node
        
        ans = 0
        while slow:
            ans = max(ans,prev.val + slow.val)
            slow = slow.next
            prev = prev.next
        
        return ans