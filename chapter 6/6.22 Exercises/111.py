from things import BinaryMinHeap

class PriorityQueue(BinaryMinHeap):
    def __init__(self):
        super().__init__()

    def enqueue(self,val):
        super().insert(val)

    def dequeue(self):
        return super().pop()
