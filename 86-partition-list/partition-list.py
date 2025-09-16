# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        [1,4,3,2,5,2], x = 3
        Two linked-lists
        1. Values that are less than  x
        2. Values greater than or equal to X



        Approach - 1

        Two linked-lists
        1. Values that are less than  x
        2. Values greater than or equal to X    

        Algorithm:
        - iterate over the linkedList
        - perform the comparison of val < x
            True: add to first list
            False: add to second list
        
        - add the head of second list to the next pointer of first list

        Time Complexity: O(N)
        Space Complexity: O(N)

        # Test-case
        head = 1 -> 4 -> 3 -> 2 -> 5 -> 2


        """

        smallerThan = ListNode()
        greaterThanOrEqual = ListNode()

        cur1 = smallerThan
        cur2 = greaterThanOrEqual
        while head:
            if head.val < x:
                cur1.next = head
                cur1 = cur1.next
            else:
                cur2.next = head
                cur2 = cur2.next
                
            head = head.next
        
        
        
        cur2.next = None
        cur1.next = greaterThanOrEqual.next

        return smallerThan.next
            