from random import randint

class Queue():
    def __init__(self):
        self.l=list()
        self._size = 0

    def size(self):
        return self._size

    def enqueue(self,item):
        self._size = self._size + 1
        self.l.append(item)

    def dequeue(self):
        if self._size > 0:
            self._size = self._size - 1
            return self.l.pop(0)

    def is_empty(self):
        return self._size == 0

printtasks = Queue()
currentsecond = 0

while currentsecond < 3600:
    currentsecond += 1
    if randint(1,180) == 1:
        print("printing...")
        #todo: do this thing