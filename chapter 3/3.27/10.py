# Another example of the parentheses matching problem comes from HyperText Markup Language (HTML).
# In HTML, tags exist in both opening and closing forms and must be balanced to properly describe a web document.
# This very simple HTML document
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

def checkHTML(html):
    stack = LLStack()
    for line in html.readlines():
        for i in line:
            if i in "<":
                stack.push(i)
            elif i in ">":
                if stack.is_empty():
                    return False
                else:
                    stack.pop()
    return stack.is_empty()


with open(file = "./html page.html") as file:
    print(checkHTML(file))

