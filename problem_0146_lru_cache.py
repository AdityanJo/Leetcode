import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.buffer=collections.OrderedDict()
        self.capacity=capacity
    def get(self, key: int) -> int:
        if self.buffer.get(key) is not None:
            val=self.buffer[key]
            del(self.buffer[key])
            self.buffer[key]=val
            # print('==>',self.buffer[key])
            return self.buffer[key]
        else:
            # print('!!')
            return -1
    def put(self, key: int, value: int) -> None:
        if self.buffer.get(key) is not None:
            del(self.buffer[key])
            self.buffer[key]=value
            # print('===>',self.buffer)
        else:
            if len(list(self.buffer.keys()))>self.capacity-1:
                self.buffer.popitem(last=False)
                self.buffer[key]=value
            else:
                self.buffer[key]=value
                # print('++')
            # print(self.buffer)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
