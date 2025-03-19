# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        cur,prev = head,dummy

        # we need atleast two pairs to reverse
        while cur and cur.next:

            # save ptrs
            nextPair = cur.next.next
            second = cur.next

            # reverse the pair
            second.next = cur
            cur.next = nextPair
            prev.next = second

            # update the pairs
            prev = cur
            cur = nextPair 

        return dummy.next
        
        