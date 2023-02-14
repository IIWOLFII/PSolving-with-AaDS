class Stack():
    def __init__(self):
        self.stack = []

    def push(self,z):
        return self.stack.append(z)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


def convert(num,base,alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S']):
    s = Stack()
    while num > 0:
        s.push(num % base)
        num = num // base
    res = ""
    while not s.is_empty():
        res = res + (alphabet[s.pop()])
    return res

print(convert(10011000,10))
