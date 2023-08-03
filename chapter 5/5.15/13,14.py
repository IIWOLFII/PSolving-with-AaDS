from hashhh import Map

class HashLength(Map):
    def __init__(self, size):
        super().__init__(size)

    def __len__(self):
        return sum([1 for i in self.slots if i is not None])

    def __contains__(self, item):
        return item in self.data

test = HashLength(11)

test[54] = "cat"
test[26] = "dog"
test[93] = "lion"
test[17] = "tiger"
test[77] = "bird"
test[31] = "cow"
test[44] = "goat"
test[55] = "pig"
test[20] = "chicken"


print(test[20])
print(test[17])
test[20] = "duck"
print(test[20])
print(test[99])

if 'duck' in test:
    print('duck is in')


print(len(test))
test.info_debug()
