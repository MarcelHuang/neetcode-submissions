"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = { None : None }
        # 2 pass: first pass, copy the node
        # second pass: copy the random pointers
        current = head
        while current:
            new_node = Node(current.val)
            old_to_new[current] = new_node
            current = current.next

        current = head
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new[current.next]
            new_node.random = old_to_new[current.random]
            current = current.next
        return old_to_new[head]