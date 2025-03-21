# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        for i in range(1, n):
            list1 = lists[i - 1]
            list2 = lists[i]

            lists[i] = self.mergeTwoLists(list1, list2)

        return lists[n - 1]

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = node = ListNode(-1)

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 or list2

        return dummy.next
