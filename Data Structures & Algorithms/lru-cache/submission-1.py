class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.hashmap = {}

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_tail(self, Node):
        prev_node = self.tail.prev
        Node.prev = prev_node
        Node.next = self.tail
        prev_node.next = Node
        self.tail.prev = Node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.add_to_tail(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
        node = Node(key, value)
        self.hashmap[key] = node
        self.add_to_tail(node)
        if len(self.hashmap) > self.capacity:
            del self.hashmap[self.head.next.key]
            self.remove(self.head.next)
        
