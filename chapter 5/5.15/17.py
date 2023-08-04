from hashhh import Map

class MapQuadratic(Map):  # Quadratic probing does not work with load pct > ~0.72
    def __init__(self,size):
        super().__init__(size)
        self.resize_threshold_pct = 0.55

    def hash_function(self, value):
        return value % self.size

    def loadpct(self):
        filled = sum([1 for i in self.slots if i is not None])
        loadfac = (filled/self.size)
        return loadfac

    def rehash(self, oldhash, quad):
        return (oldhash + quad*quad) % self.size

    def put(self, key, val, hashed=None, quad = 0):
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
            next_hashed_key = self.rehash(hashed_key, quad + 1)
            #print(f"{self.loadpct()=}")
            #print(f'putting rehashed {key=} as {next_hashed_key=}')
            self.put(key, val, hashed=next_hashed_key, quad = quad + 1)  # wtf recursion actually useful

    def get(self, key):
        data = self.data
        slots = self.slots
        starting_key = self.hash_function(key)
        hashed_key = starting_key
        quad = 0
        while self.slots[hashed_key] is not None:
            if slots[hashed_key] == key:
                return data[hashed_key]
            quad += 1
            hashed_key = self.rehash(hashed_key, quad)
            #print(f"{self.loadpct()=}")
            #print(f'getting rehashed {key=} as {hashed_key=}')
            if hashed_key == starting_key:
                #print(f'gave up at {self.loadpct()=}')
                break

        hashed_key = starting_key  # if we dont find with quadratic then we launch regular one until we find it or reach starting key

        while True:
            if slots[hashed_key] == key:
                return data[hashed_key]
            hashed_key = self.rehash(hashed_key, 1)
            if hashed_key == starting_key:
                return None



test = MapQuadratic(11)
test[54] = "cat"
test[26] = "dog"
test[93] = "lion"
test[17] = "tiger"
test[77] = "bird"
test[31] = "cow"
test[44] = "goat"
test[55] = "pig"
test[20] = "chicken"
test.info_debug()
print(test[20])
print(test[17])
test[20] = "duck"
print(test[20])
test.info_debug()
print(test[99])

