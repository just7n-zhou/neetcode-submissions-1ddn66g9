class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val 
        self.prev = self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity 
        self.cache = {} # store key to node
        self.left = Node(0, 0) # left dummy point to LRU 
        self.right = Node(0, 0) # right dummy point to most recent used
        self.left.next = self.right 
        self.right.prev = self.left 

    # remove node from linked list 
    def remove(self, node):
        prev, nxt = node.prev, node.next 
        prev.next = nxt 
        nxt.prev = prev 

    # insert node after the right dummy to track most recent used
    def insert(self, node):
        # node is to be inserted between prev of right pointer and right pointer 
        prev, nxt = self.right.prev, self.right 
        # insert node in between
        prev.next = nxt.prev = node
        # update the node pointer 
        node.next = nxt
        node.prev = prev 

    def get(self, key: int) -> int:
        # if key exists in cache 
        if key in self.cache:
            # remove this node first 
            self.remove(self.cache[key])
            # then insert it again to make it most recent used 
            self.insert(self.cache[key])
            # then return the node's value
            return self.cache[key].val
        # if key does not exist, return -1
        return -1 

    def put(self, key: int, value: int) -> None:
        # if the key exists in cache, update it the same way as get
        if key in self.cache:
            # remove this node first 
            self.remove(self.cache[key])
        # if key not exist, create a new node and insert 
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key]) 

        # if size exceeds capacity, remove the LRU
        if len(self.cache) > self.cap:  
            # node of LRU(key, value)
            LRU = self.left.next 
            # remove the LRU from list 
            self.remove(LRU)
            # delete the key from the cache
            del self.cache[LRU.key]