# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        

        dummy = ListNode()
        res = dummy
        cur1,cur2 = list1,list2

        print(res)
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                res.next = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                res.next = ListNode(cur2.val)
                cur2 = cur2.next

            print(res)
            res = res.next

        while cur1:
            res.next = ListNode(cur1.val)
            cur1 = cur1.next
            res = res.next
        
        while cur2:
            res.next = ListNode(cur2.val)
            cur2 = cur2.next
            res = res.next
        
        return dummy.next
