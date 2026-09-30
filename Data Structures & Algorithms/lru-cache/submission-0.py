class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = []
        
    def get(self, key: int) -> int:
        for idx in range(len(self.cache)):
            if self.cache[idx][0] == key:
                item = self.cache.pop(idx)
                self.cache.append(item)
                return item[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for idx in range(len(self.cache)):
            if self.cache[idx][0] == key:
                self.cache.pop(idx)
                self.cache.append([key, value])
                return

        if len(self.cache) == self.cap:
            self.cache.pop(0)
        self.cache.append([key, value])
    
        
