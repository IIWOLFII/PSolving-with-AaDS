from hashhh import Map

#  https://www.youtube.com/watch?v=z0lJ2k0sl1g todo watch this later

class PerfectHash(Map):
    def __init__(self, size):
        super().__init__(size)

    def hash_function(self, value):
        if isinstance(value,int):
            return self.hash_int(value)
        elif isinstance(value,str):
            return self.hash_str(value)
        else:
            raise Exception('Type not handled')

    def hash_str(self,value):
        position = sum([ord(i) for i in value])
        if position > self.size:
            self.extend(position)
        return position

    def hash_int(self,value):
        position = value
        if position > self.size:
            self.extend(position)
        return position

    def extend(self,pos):
        difference = pos - self.size + 1
        self.size += difference
        self.slots += [None] * difference
        self.data += [None] * difference


test = PerfectHash(11)
test[54] = 12
test['cat'] = 14
test['boa'] = 16
test['newt'] = 18

test.info_debug()

for i in [54,'cat','boa','newt']:
    print(test[i])