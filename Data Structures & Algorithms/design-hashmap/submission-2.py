# Hash map using an array of linked lists, 
# with collisions resolved by separate chaining (bucket index = key % array length)
class ListNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for i in range(1000)]
        

    def put(self, key: int, value: int) -> None:
        index = hash(key) % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)


    def remove(self, key: int) -> None:
        index = hash(key) % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

    def get(self, key: int) -> int:
        index = hash(key) % len(self.map)
        cur = self.map[index]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)