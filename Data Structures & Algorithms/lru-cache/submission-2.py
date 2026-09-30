class Node:
     def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> node

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node: Node) -> None:
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        #remove from the DLL
        self._remove(node)
        #append to the end of the DLL as MRU
        self._append(node)
        # return key
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value) # create the node
        self.cache[key] = node
        self._append(node)

        if len(self.cache) > self.cap:
            lru = self.head.next # get the lru
            self._remove(lru) # remove the lru
            del self.cache[lru.key] # delet efrom cache



        



    
        
