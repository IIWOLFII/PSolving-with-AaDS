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

        # if slots[hashed_key] == key:
        #     return data[hashed_key]
        # elif slots[hashed_key] != key:
        #     while True:
        #         if slots[hashed_key] == key:
        #             return data[hashed_key]
        #         hashed_key = self.rehash(hashed_key)
        #         if hashed_key == starting_key:
        #             return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, item):
        return self.put(key, item)

    # def __del__(self):
    #     pass
    #
    # def size(self):
    #     return len(self.keymap)
    #
    # def __contains__(self, item):
    #     pass


# test = Map(11)
# test.info()
#
# print(test.hash_function(25))
# print(test.hash_function(36))
#
# test.put(25,'value')
# test.info()
#
# test.put(36,'probed value')
# test.info()
#
# val = test.get(25)
# print(val)
#
# val = test.get(36)
# print(val)


# test = Map(11)
#
# test[25] = 'value'
# test[36] = 'probed value'
#
# print(test[25])
# print(test[36])
#
# test[36] = 'updated probed value'
#
# print(test[36])


test = Map(11)

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
