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

def is_balanced(string):
    left_symbols = ["(","{","["]
    right_symbols = [")","}","]"]
    s = Stack()
    for i in string:
        if i in left_symbols:
            s.push(i)
        else:
            if s.is_empty():
                return False
            if i != right_symbols[left_symbols.index(s.peek())]:
                return False
            s.pop()
    return s.is_empty()

print(is_balanced('{({([][])}())}')) # expected True
print(is_balanced('[{()]')) # expected False

print("all True below ======")
print(is_balanced('{{([][])}()}')) # expected True
print(is_balanced('[[{{(())}}]]')) # expected True
print(is_balanced('[][][](){}')) # expected True

print("all False below ======")
print(is_balanced('([)]')) # expected False
print(is_balanced('((()]))')) # expected False
print(is_balanced('[{()]')) # expected False


