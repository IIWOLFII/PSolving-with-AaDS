class Node():
    def __init__(self, item = None):
        self.value = item
        self.next = None
        self.back = None

class LLDeQueue():
    def __init__(self):
        self.__size = 0
        self.head = None
        self.tail = None

    def pop_head(self):
        if self.head is None:
            self.__size = 0
            return None

        self.__size -= 1

        if self.head.next is not None:
            self.head.next.back = None

        front = self.head
        self.head = front.next

        if self.head is None:
            self.tail = None

        return front.value

    def pop_rear(self):
        if self.tail is None:
            self.__size = 0
            return None

        self.__size -= 1

        tail = self.tail
        self.tail = tail.back

        if self.tail is None:
            self.head = None
            return tail.value
        else:
            self.tail.next = None

        return tail.value

    def is_empty(self):
        return self.__size == 0

    def add_rear(self, item):
        item = Node(item)
        self.__size += 1

        if self.head is None:
            self.head = item
            self.tail = item
            return

        item.back = self.tail
        self.tail.next = item
        self.tail = item

    def add_head(self, item):
        item = Node(item)
        self.__size += 1

        if self.head is None:
            self.head = item
            self.tail = item
            return

        self.head.back = item
        item.next = self.head
        self.head = item


    def size(self):
        return self.__size

    def __str__(self):
        li = ""
        item = self.head
        while item is not None:
            li = li + str(item.value) + ","
            item = item.next
        return "[" + li[:-1] + "]"

    def reversed(self):
        li = ""
        item = self.tail
        while item is not None:
            li = li + str(item.value) + ","
            item = item.back
        return "[" + li[:-1] + "]"

    def printHeads(self):
        print("=======")
        print("==Head==")
        for i in [self.head,self.tail]:
            if i is None:
                print(None)
            else:
                print(i.value)
        print("==Tail==")
        print("=======")




d = LLDeQueue()
print(d.is_empty())
d.add_rear("dog")
print(d)
d.add_head("cat")
print(d)
d.add_head(True)
print(d)
d.add_head("dog")
print(d)
d.add_rear("dong")
print(d)
print(d.size())
print(d.is_empty())

print(d.pop_head())
print(d)

print(d.pop_rear())
d.printHeads()
print(d.pop_rear())
d.printHeads()
print(d.pop_rear())
d.printHeads()
print(d.pop_rear())
d.printHeads()
print(d.pop_rear())
d.printHeads()
print(d)
#print(d.reversed())
