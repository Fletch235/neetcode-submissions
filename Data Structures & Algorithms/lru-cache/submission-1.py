class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.items:
            self.items.move_to_end(key)
            return self.items[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            self.items[key] = value
            self.items.move_to_end(key)
        else:
            if len(self.items) >= self.capacity:
                self.items.popitem(last=False)
            self.items[key] = value