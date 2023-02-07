#Printing tasks

# Consider the following situation in a computer science laboratory.
# On any average day about 10 students are working in the lab at any given hour.
# These students typically print up to twice during that time, and the length of these tasks ranges from 1 to 20 pages.
# The printer in the lab is older, capable of processing 10 pages per minute of draft quality.
# The printer could be switched to give better quality, but then it would produce only five pages per minute.
# The slower printing speed could make students wait too long. What page rate should be used?
import random as rng

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

pageperminute = 10 # 4- 8 min
pageperminute = 25 # 2 min

pagetimeseconds = 60 / pageperminute
students = []

for i in range(10):
    students.append(rng.randint(1,20))



printque = Queue()

for i in students:
    printque.enqueue(i)



time = 0
timeaverages = []
lasttime = Stack()
fuckthisshit = printque.dequeue()*pagetimeseconds
lasttime.push(fuckthisshit)
timeaverages.append(fuckthisshit)
while not printque.is_empty():
    bruh = lasttime.pop()+printque.dequeue()*pagetimeseconds
    lasttime.push(bruh)
    timeaverages.append(bruh)

print(timeaverages)
print(f"average time: {(sum(timeaverages)/len(timeaverages))/60} minutes")