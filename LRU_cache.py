import collections 
class LRUCache:
    def __init__(self,capacity :int):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def put(self,key:int,value:int):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
                # //first in first out
        self.cache[key] = value   
    
    def get(self,key:int): 
        try:
            value = self.cache.pop(key)   
            self.cache[key] = value
            val = value
            # print(value)
            return value
        except KeyError:
            # print(-1)
            return -1
 
    def get_cache(self):
        return self.cache