import timeit
import random
import matplotlib.pyplot as plt

def drawplot(a,b):
    fig, ax = plt.subplots()
    ax.set_xlabel("n - sample size")
    ax.set_ylabel("time")
    ax.plot(a, b)
    plt.show()


#
#1) Devise an experiment to verify that the list index operator is O(1).
#

# a = []
# b = []
# for i in range(10000, 1000001, 20000):
#     a.append(i)
#     x = list(range(i + 1))
#     t = timeit.Timer(f"x[{i}]", "from __main__ import random, x")  # O(1)
#     # t = timeit.Timer(f"x.pop(0)","from __main__ import random, x") #linear example
#     time = t.timeit(number=1000)
#     b.append(f"{time:.3f}")
#     print(f"n: {i}, time: {time:.3f} miliseconds")
#
# drawplot(a,b)

#
#2) Devise an experiment to verify that get item and set item are O(1) for dictionaries.
#

# a = []
# b = []
#
# for i in range(10000, 1000001, 20000):
#     a.append(i)
#     valrange = (range(i + 1))
#     x = {i:k for (i,k) in zip(valrange,valrange)}
#     t = timeit.Timer(f"x.get(25)", "from __main__ import random, x") #get
#     #t = timeit.Timer(f"x[523]=25", "from __main__ import random, x") #set
#     time = t.timeit(number=1000)
#     b.append(f"{time:.3f}")
#     print(f"n: {i}, time: {time:.3f} miliseconds")
#
# drawplot(a,b)

#
#3) Devise an experiment that compares the performance of the del operator on lists and dictionaries.
#

# a = []
# b = []
# c = []
# for i in range(10000, 1000001, 20000):
#     a.append(i)
#     valrange = (range(i + 1))
#     x = {i:k for (i,k) in zip(valrange,valrange)}
#     y = list(range(i + 1))
#     t = timeit.Timer(f"del x[{2}]", "from __main__ import random, x") #dict
#     timet = t.timeit(number=1)
#     T = timeit.Timer(f"del y[:-25]", "from __main__ import random, y") #list
#     timeT = T.timeit(number=2000)
#     b.append(f"{timet:.3f}")
#     c.append(f"{timeT:.3f}")
#
# fig, ax = plt.subplots()
# ax.set_xlabel("n - sample size")
# ax.set_ylabel("time")
# ax.plot(a, b, label = "Dict del")
# ax.plot(a, c, label = "List del")
# ax.legend()
# plt.show()

#
#4) Given a list of numbers in random order, write an algorithm that works in O(n log (n)) to find the kth smallest number in the list.
#

a = 10
n = [random.randint(-50,50) for i in range(a)]

def task4(n,k):
    n.sort()
    return(n[k-1])

k = 5
smol = task4(n,k)
print(n)
print(f"{k}'th smallest is: {smol}")


#
#5) Can you improve the algorithm from the previous problem to be linear? Explain.
#

# no i can not look at all this bullshit i will not comprehend this in at least two years

#https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array-set-3-worst-case-linear-time/

#how am i supposed to read this
#Introduction to Algorithms by Clifford Stein, Thomas H. Cormen, Charles E. Leiserson, Ronald L.
#http://staff.ustc.edu.cn/~csli/graduate/algorithms/book6/toc.htm





