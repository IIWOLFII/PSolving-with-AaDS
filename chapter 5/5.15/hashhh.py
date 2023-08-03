class Map():
    def __init__(self, size):
        self.size = size
        self.slots = [None] * size
        self.data = [None] * size

    def info_debug(self):
        print('=' * 10)
        print(f"{self.slots=}\n  {self.data=}")
        print('=' * 10)

    def hash_function(self, value):
        return value % self.size

    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, val, hashed=None):
        hashed_key = hashed
        if hashed is None:
            hashed_key = self.hash_function(key)
        assert hashed_key is not None
        if self.slots[hashed_key] is None:
            self.slots[hashed_key] = key
            self.data[hashed_key] = val
        elif self.slots[hashed_key] == key:
            self.data[hashed_key] = val
        elif self.slots[hashed_key] != key:
            next_hashed_key = self.rehash(hashed_key)
            self.put(key, val, hashed=next_hashed_key)  # wtf recursion actually useful

    def get(self, key):
        data = self.data
        slots = self.slots
        starting_key = self.hash_function(key)
        hashed_key = starting_key
        while self.slots[hashed_key] is not None:
            if slots[hashed_key] == key:
                return data[hashed_key]
            hashed_key = self.rehash(hashed_key)
            if hashed_key == starting_key:
                return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        return self.put(key, item)