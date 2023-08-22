from things import HeapDrawer

class BinaryMaxHeapTopx():
    def __init__(self, heapsize, heap=None):
        self.heapsize = heapsize
        if heap is None:
            self.heap = []
        else:
            self.heap = heap
            self.heapify()


    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)
        self.limitheap()

    def bubble_up(self, index):
        while self.heap[index] > self.heap[(index - 1) // 2] and index > 0:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def bubble_down(self, index):
        while True:
            maxchild_idx = self.get_max_child_idx(index)
            if maxchild_idx is None:
                break

            if self.heap[maxchild_idx] < self.heap[index]:
                break

            self.heap[index], self.heap[maxchild_idx] = self.heap[maxchild_idx], self.heap[index]
            index = maxchild_idx

    def get_max_child_idx(self, index):
        left_idx = index * 2 + 1
        right_idx = index * 2 + 2
        max_idx = len(self.heap) - 1
        if left_idx > max_idx:  # if left does not exist, right doesnt exist either
            return None
        assert left_idx <= max_idx  # left exists
        if right_idx > max_idx:  # if right doesnt exist, but left exists, return left
            return left_idx
        if self.heap[left_idx] < self.heap[right_idx]:
            return right_idx
        else:
            return left_idx

    def peek(self):
        return self.heap[0]

    def limitheap(self):
        self.heap = self.heap[:self.heapsize]

    def heapify(self,heap = None):
        if heap is None:
            self.heap = self.heap[:]  # [:] to avoid pointing at the list
        else:
            self.heap = heap[:]

        i = len(self.heap) // 2 - 1
        while i >= 0:
            self.bubble_down(i)
            i -= 1
        self.limitheap()


    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        oldmin = self.heap.pop()
        self.bubble_down(0)
        return oldmin


lissst = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

heap = BinaryMaxHeapTopx(5, lissst)

print('popped:', heap.pop())
print('peeked:', heap.peek())

heap.insert(500)
heap.insert(5)
heap.insert(2)


notheap = [9, 6, 5, 0, 1, 2, 3]
notheap.reverse()
heap.heap = notheap
heap.heapify()

draw = HeapDrawer(heap)
draw.drawtree()


