# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dumb = ListNode(0)
        temp1 = list1
        temp2 = list2
        tail = dumb

        while temp1 is not None and temp2 is not None:

            if temp1.val <= temp2.val:
                tail.next = temp1
                temp1 = temp1.next
            else:
                tail.next = temp2
                temp2 = temp2.next

            tail = tail.next


        if temp1:
            tail.next = temp1
        if temp2:
            tail.next = temp2

        return dumb.next
        