class Node():
    def __init__(self, item = None):
        self.value = item
        self.next = None

class LLQueue():
    def __init__(self):
        self.__size = 0
        self.head = None

    def dequeue(self):
        if self.head is None:
            self.__size = 0
            return None
        last = self.head
        self.head = last.next
        self.__size -= 1
        return last.value

    def is_empty(self):
        return self.__size == 0

    def enqueue(self, item):
        item = Node(item)
        self.__size += 1
        current = self.head
        if current is None:
            self.head = item
            return
        while current.next is not None:
            current = current.next
        current.next = item

    def size(self):
        return self.__size

    def __str__(self):
        li = ""
        item = self.head
        while item is not None:
            li = li + str(item.value) + ","
            item = item.next
        return "[" + li[:-1] + "]"


q = LLQueue()
print(q)
q.enqueue("hello")
print(q)
q.enqueue("dog")
print(q)
q.enqueue(3)
print(q)
q.dequeue()
print(q)
print(q.size())

q.dequeue()
print(q)
print(q.size())
