# bin heaps

class BinaryMinHeap():
    def __init__(self, heap=None):
        self.heap = heap
        if heap is None:
            self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self.bubble_up(len(self.heap) - 1)

    def bubble_up(self, index):
        while self.heap[index] < self.heap[(index - 1) // 2] and index > 0:
            self.heap[index], self.heap[(index - 1) // 2] = self.heap[(index - 1) // 2], self.heap[index]
            index = (index - 1) // 2

    def bubble_down(self, index):
        while True:
            minchild_idx = self.get_min_child_idx(index)
            if minchild_idx is None:
                break
            self.heap[index], self.heap[minchild_idx] = self.heap[minchild_idx], self.heap[index]
            index = minchild_idx

    def get_min_child_idx(self, index):
        left_idx = index * 2 + 1
        right_idx = index * 2 + 2
        max_idx = len(self.heap) - 1
        if left_idx > max_idx:  # if left does not exist, right doesnt exist either
            return None
        assert left_idx <= max_idx  # left exists
        if right_idx > max_idx:  # if right doesnt exist, but left exists, return left
            return left_idx
        if self.heap[left_idx] > self.heap[right_idx]:
            return right_idx
        else:
            return left_idx

    def peek(self):
        return self.heap[0]

    def heapify(self,notheap):
        self.heap = notheap[:]  # [:] to avoid pointing at the list
        i = len(self.heap) // 2 - 1
        while i >= 0:
            self.bubble_down(i)
            i -= 1

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        oldmin = self.heap.pop()
        self.bubble_down(0)
        return oldmin


lissst = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

heap = BinaryMinHeap(lissst)


print('popped:', heap.pop())
print('peeked:', heap.peek())

heap.insert(500)
heap.insert(5)
heap.insert(2)


print(heap.heap)


notheap = [9, 6, 5, 0, 1, 2, 3]

heap.heapify(notheap)

print(heap.heap)