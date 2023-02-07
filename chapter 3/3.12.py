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

q = Queue()
print(q.l)
q.enqueue("hello")
print(q.l)
q.enqueue("dog")
print(q.l)
q.enqueue(3)
print(q.l)
q.dequeue()
print(q.l)
print(q.size())
