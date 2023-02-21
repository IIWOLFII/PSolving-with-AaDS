import timeit
import random
import matplotlib.pyplot as plt

def drawplot(a,b):
    fig, ax = plt.subplots()
    ax.set_xlabel("n - sample size")
    ax.set_ylabel("time")
    ax.plot(a, b)
    plt.show()

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

class Queue5():
    def __init__(self):
        self.l=list()
        self._size = 0

    def size(self):
        return self._size

    def enqueue(self,item):
        self._size = self._size + 1
        self.l.insert(0,item)

    def dequeue(self):
        if self._size > 0:
            self._size = self._size - 1
            return self.l.pop()

    def is_empty(self):
        return self._size == 0

a = []
b = []

wtf = Queue5()

for i in range(10000, 1000001, 20000):
    a.append(i)

    x = wtf.enqueue

    t = timeit.Timer(f"x({i})", "from __main__ import random, x")

    time = t.timeit(number=1000)
    b.append(f"{time:.3f}")
    print(f"n: {i}, time: {time:.3f} miliseconds")

drawplot(a,b)

a = []
b = []

wtf = Queue()

for i in range(10000, 1000001, 20000):
    a.append(i)

    x = wtf.enqueue

    t = timeit.Timer(f"x({i})", "from __main__ import random, x")

    time = t.timeit(number=1000)
    b.append(f"{time:.3f}")
    print(f"n: {i}, time: {time:.3f} miliseconds")

drawplot(a, b)