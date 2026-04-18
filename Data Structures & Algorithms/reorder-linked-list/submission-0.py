# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the middle node of the Linked List
        # 2. detach first half and second half
        # 3. reverse second half
        # 4. merge back alternatively first half and second half
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # [0, 1, 2, 3, 4, 5, 6]
        #           s
        #                    f
        #                    0 1 2 3
        #                    6 5 4
        second_half = slow.next
        slow.next = None  # 0 -> 1 -> 2 -> 3
        prev = None
        curr = second_half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        # second_half new head = prev
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2