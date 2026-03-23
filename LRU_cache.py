class LRUCache:
    def __init__(self, capacity: int):
        self.d={}
        self.l=[]
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.put(key,self.d[key])
            return self.d[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d and len(self.d) == self.capacity:
            del self.d[self.l[0]]
            self.l.pop(0)
        if key in self.l:
            self.l.remove(key)
        self.d[key]=value
        self.l.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
