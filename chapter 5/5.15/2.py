from hashhh import Map

class StrMap(Map):  # s OL id
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
        return sum([ord(i) for i in value])%self.size

    def hash_int(self,value):
        return value % self.size

test = StrMap(11)

test[54] = 12
test['cat'] = 14
test['boa'] = 16
test['newt'] = 18

test.info_debug()

print(test['cat'])
print(test['boa'])
print(test['newt'])

