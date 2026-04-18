# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        trailer = dummy
        leader = head
        for _ in range(n):
            leader = leader.next
        while leader:
            trailer = trailer.next
            leader = leader.next
        trailer.next = trailer.next.next
        return dummy.next