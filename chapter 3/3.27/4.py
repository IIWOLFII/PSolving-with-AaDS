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

class Calculator():
    def __init__(self):
        self.bruh = {"+":self.__sum,"-":self.__subtract,"*":self.__mul,"/":self.__div}
    def calc(self,a,b,operation):
        fun = self.bruh[operation]
        return fun(float(a),float(b))
    def __sum(self,a,b):
        return a + b
    def __subtract(self,a,b):
        return a - b
    def __mul(self,a,b):
        return a * b
    def __div(self,a,b):
        return a / b

def calcpostifx(expression):
    result = list()
    op_stack = Stack()
    prec = {"^": 4,"*": 3, "/": 3, "-": 2, "+": 2,"(": 1}
    for char in expression:

        if char not in "*/-+()^":
            result.append(char)
        elif char == "(":
            op_stack.push(char)
        elif char == ")":
            while not op_stack.is_empty():
                if op_stack.peek() == "(":
                    op_stack.pop()
                    break
                result.append(op_stack.pop())
        elif char in "*/-+^":
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[char]):
                result.append(op_stack.pop())
            op_stack.push(char)
    while not op_stack.is_empty():
        result.append(op_stack.pop())
    return postfxeval(" ".join(result))

def postfxeval(postfxexp):
    cal = Calculator()
    var2 = Stack()
    postfxexp = postfxexp.split(" ")
    for i in postfxexp:
        if i in "+*-/":
            b = var2.pop()
            a = var2.pop()
            res = cal.calc(a,b,i)
            var2.push(res)
        else:
            var2.push(i)
    return var2.pop()

entering_numbers = True
a = ""
print("******||Calculator||******")
print("******||Enter numbers||******")
while entering_numbers:
    inp = input()
    if inp in ["Stop",""," "]:
        entering_numbers = False
    else:
        a += inp

print(calcpostifx(a))
