"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Key idea (From EPI):
# Use the next field for each node in the original list 
# to record the mapping from the orignal node to its copy
# To avoid losing the structure of the original list,
# we use the next field in each copied node to point to the
# SUCCESSOR of its original node
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Phase 1: Create interweaved list of original and copy nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Phase 2: Set random pointers for copied nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Phase 3: Separate the lists using a temp variable
        current = head
        new_list_head = current.next
        while current.next:
            # Store the next copy node before we change any pointers
            temp = current.next
            
            # Update original node's next pointer to skip the copy
            current.next = temp.next
            
            # Move current to next original node
            current = temp
            
        return new_list_head