import copy

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

        # print(f"result list: {result}")
        # print(f"op_stack: ", end="")
        # bruhstack = copy.deepcopy(op_stack)
        # while not bruhstack.is_empty():
        #     try:
        #         print(bruhstack.pop(), end="")
        #     except IndexError:
        #         continue
        #     finally:
        #         continue
        # print("\n")

        if char not in "*/-+()^":
            result.append(char)
        elif char == "(":
            op_stack.push(char)
        elif char == ")":
            while True and not op_stack.is_empty():
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
    return "".join(result)

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

# print(calcpostifx("1*(2+3)*4")) # ABC+*D*
# print(calcpostifx("A * B + C * D")) # ABC+*D*
# print(calcpostifx("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(calcpostifx("( A + B ) * ( C + D )"))
# print(postfxeval("4 5 6 * +"))
# print(postfxeval("7 8 + 3 2 + /"))
# print(postfxeval("17 10 + 3 * 9 /"))

print(calcpostifx("5*3^(4-2)"))