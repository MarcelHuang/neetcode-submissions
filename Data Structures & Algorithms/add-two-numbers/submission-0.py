# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first = []
        second = []
        while l1:
            first.append(str(l1.val))
            l1 = l1.next
        while l2:
            second.append(str(l2.val))
            l2 = l2.next
        first = int("".join(reversed(first)))
        second = int("".join(reversed(second)))
        result = str(first + second)[::-1]
        print(result)
        dummy = ListNode(0)
        curr = dummy
        for char in result:
            curr.next = ListNode(int(char))
            curr = curr.next
        return dummy.next

