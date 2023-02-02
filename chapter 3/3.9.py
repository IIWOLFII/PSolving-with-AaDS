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

def calcposfx(expression):
    nums = Stack()
    opes = Stack()
    for i in expression:
        if i not in "+*":
            opes.push(i)
        else:
            nums.push(i)
    while not opes.is_empty():
        nums.push(opes.pop())
    while not nums.is_empty():
        print(nums.pop(),end="")


calcposfx("a+b*c")

