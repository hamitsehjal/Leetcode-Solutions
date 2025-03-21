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

        mid = n // 2
        left = lists[:mid]
        right = lists[mid:]

        left_list = self.mergeKLists(left)
        right_list = self.mergeKLists(right)

        return self.mergeTwoLists(left_list,right_list)

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
