#stack using linked lists

class Node():
    def __init__(self, item = None):
        self.value = item
        self.next = None

class LLStack():
    def __init__(self):
        self.__size = 0
        self.head = None

    def pop(self):
        if self.head is None:
            self.__size = 0
            return None
        last = self.head
        self.head = last.next
        self.__size -= 1
        return last.value

    def is_empty(self):
        return self.__size == 0

    def push(self, item):
        item = Node(item)
        item.next = self.head
        self.head = item
        self.__size += 1
        return

    def peek(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.__size


# def is_balanced(string):
#     left_symbols = ["(","{","["]
#     right_symbols = [")","}","]"]
#     s = LLStack()
#     for i in string:
#         if i in left_symbols:
#             s.push(i)
#         else:
#             if s.is_empty():
#                 return False
#             if i != right_symbols[left_symbols.index(s.peek())]:
#                 return False
#             s.pop()
#     return s.is_empty()
#
# print(is_balanced('{({([][])}())}')) # expected True
# print(is_balanced('[{()]')) # expected False
#
# print("all True below ======")
# print(is_balanced('{{([][])}()}')) # expected True
# print(is_balanced('[[{{(())}}]]')) # expected True
# print(is_balanced('[][][](){}')) # expected True
#
# print("all False below ======")
# print(is_balanced('([)]')) # expected False
# print(is_balanced('((()]))')) # expected False
# print(is_balanced('[{()]')) # expected False




#
# def is_balanced(string):
#     s = LLStack()
#     for i in string:
#         if (i == "("):
#             s.push(i)
#         else:
#             if s.is_empty():
#                 return False
#             s.pop()
#     return s.is_empty()
#
# print(is_balanced("((())"))
# print(is_balanced("(())"))