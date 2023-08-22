from things import BinaryMinHeap, HeapDrawer
import random as rng

def heapsort(val):
    sorter = BinaryMinHeap(val)

    for i in range(len(val)):
        val[i] = sorter.pop()



test1 = [rng.randint(0,50) for i in range(21)]

print(test1)

heapsort(test1)

print(test1)

