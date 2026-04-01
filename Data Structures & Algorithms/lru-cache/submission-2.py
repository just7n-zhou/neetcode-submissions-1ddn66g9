class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # store key to node 
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right 
        self.right.prev = self.left 

    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev

    # insert to the right
    def insert(self, node):
        # get the prev and next of the right dummy 
        prev, nxt = self.right.prev, self.right
        # insert current node between the prev and nxt 
        prev.next = nxt.prev = node 
        # update node pointer 
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        # if key exists
        if key in self.cache:
            # remove it first 
            self.remove(self.cache[key])
            # insert to the right to update most recent
            self.insert(self.cache[key])
            return self.cache[key].val
        # return -1 if not exist
        return -1 

    def put(self, key: int, value: int) -> None:
        # first if key exists, remove it first 
        if key in self.cache:
            self.remove(self.cache[key])
        # create a new node to the cache and update most recent
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
