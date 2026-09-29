class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hmap = OrderedDict()
                

    def get(self, key: int) -> int:

        if key not in self.hmap:
            return -1
        val = self.hmap.get(key)

        self.hmap.move_to_end(key)

        return val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            del self.hmap[key]

        self.hmap[key] = value

        if len(self.hmap) > self.capacity:
            self.hmap.popitem(last=False)
        
        
