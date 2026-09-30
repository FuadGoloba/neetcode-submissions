class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.order = []
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)

        self.order.append(key)
        self.cache[key] = value

        if len(self.order) > self.cap:
            lru = self.order.pop(0)
            del self.cache[lru]


    
        
