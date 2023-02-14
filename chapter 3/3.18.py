class Deque:
    def __init__(self):
        self.deque = list()

    def is_empty(self):
        return self.deque == []

    def size(self):
        return len(self.deque)

    def pop_front(self):
        return self.deque.pop()

    def pop_rear(self):
        return self.deque.pop(0)

    def add_front(self,thing):
        self.deque.append(thing)

    def add_rear(self,thing):
        self.deque.insert(0,thing)

