#radix sort
from random import randint
import matplotlib.pyplot as plt

def drawgraph(data):
    fig,ax = plt.subplots()
    x = range(len(data))
    y = data
    plt.bar(x,y)
    plt.xticks(x,x)
    plt.show()
    plt.cla()
    plt.clf()
    plt.close()
    #input("Continue?")

def radixsort(data):
    bins = [list() for i in range(10)]
    negative = []
    positives = []
    if data == []:
        return
    maxdigit = str(max(data,key=abs))
    maxdigitlen = len(maxdigit)
    for digit in reversed(range(-maxdigitlen,0)):

        for i in data:
            try:
                currdig = str(i)[digit]
            except IndexError:
                currdig = 0
            if currdig == "-":
                currdig = 0
            bins[int(currdig)].append(i)

        positives = []
        negative = []

        for curbin in bins:
            while not(curbin == []):
                item = curbin.pop(0)
                if item < 0:
                    negative.append(item)
                else:
                    positives.append(item)
        data = negative + positives

    if not (negative == []):
        data = negative[::-1] + positives
    return data


n = [randint(0,299) for i in range(5)]
print("Starting:", n)
#drawgraph(n)
bruh = [-46,-346,-23,-9,-650,0]
for i in bruh:
    n.append(i)

n = radixsort(n)
print(n)

# def radixsort(data):
#     bins = [list() for i in range(10)]
#     maxdigit = str(max(data))
#     maxdigitlen = len(maxdigit)
#     for digit in reversed(range(-maxdigitlen,0)):
#         for i in data:
#             try:
#                 currdig = str(i)[digit]
#             except IndexError:
#                 currdig = 0
#             bins[int(currdig)].append(i)
#         data = []
#         for curbin in bins:
#             while not(curbin == []):
#                 data.append(curbin.pop(0))
#         #drawgraph(data)
#     return data