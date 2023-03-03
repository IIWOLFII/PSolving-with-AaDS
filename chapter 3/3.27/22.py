class Node():
    def __init__(self, item = None):
        self.value = item
        self.next = None

class LLQueue():
    def __init__(self):
        self.__size = 0
        self.head = None
        self.tail = None

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
        if self.head is None:
            self.head = item
            self.tail = item
            self.__size = 1
            return
        #TODO: make this thing work i guess


    def size(self):
        return self.__size