from hashhh import Map

class MapDynamic(Map):
    def __init__(self,size):
        super().__init__(size)
        self.resize_threshold_pct = 0.55

    def info_debug(self):
        print('=' * 10)
        print(f"{self.slots=}\n  {self.data=}\n {self.loadpct()=}")
        print('=' * 10)

    def put(self, key, val, hashed=None):
        if self.loadpct() > self.resize_threshold_pct:
            self.resize()
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
            self.put(key, val, hashed=next_hashed_key)

    def loadpct(self):
        filled = sum([1 for i in self.slots if i is not None])
        loadfac = (filled/self.size)
        return loadfac

    def resize(self):
        expandby = self.size//2
        self.size += expandby
        self.slots += [None] * expandby
        self.data += [None] * expandby



test = MapDynamic(11)
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

