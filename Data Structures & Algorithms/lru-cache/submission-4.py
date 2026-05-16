class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # store key to node 
        self.left = Node(0, 0) # left dummy for LRU 
        self.right = Node(0, 0) # right dummy for MRU 
        self.left.next = self.right 
        self.right.prev = self.left

    # remove a node from list
    def remove(self, node):
        prev, nxt = node.prev,node.next 
        prev.next = nxt 
        nxt.prev = prev

    # insert next to right dummy 
    def insert(self, node):
        prev, nxt = self.right.prev, self.right 
        prev.next  = nxt.prev = node
        node.next = nxt 
        node.prev = prev 

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            LRU = self.left.next 
            self.remove(LRU)
            del self.cache[LRU.key]
