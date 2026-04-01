class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # store key to node 
        # left and right are two dummy nodes at left most and right most position
        self.left, self.right = Node(0,0), Node(0, 0)
        self.left.next = self.right 
        self.right.prev = self.left 
    
    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev 

    # insert node at right before right dummy
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        # insert node between right dummy and its prev 
        prev.next = nxt.prev = node 
        # point node's next to right dummy and prev to right dummy's prev
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # if key exists
        if key in self.cache:
            # remove it from cache first
            self.remove(self.cache[key])
            # then insert it to the right to make it most recent
            self.insert(self.cache[key])
            return self.cache[key].val
        # it no key return -1 
        return -1

    def put(self, key: int, value: int) -> None:
        # if the key exists, delete it first 
        if key in self.cache:
            self.remove(self.cache[key])
        # then create a new node to store in cache
        self.cache[key] = Node(key, value)
        # and insert it to the right to make it most recent
        self.insert(self.cache[key])

        # if len exceed capacity
        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from cache
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]