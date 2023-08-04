import timeit
import random as rng

import matplotlib.pyplot as plt

def quick_sort(alist, start=0, end=None):
    if end is None:
        end = len(alist) - 1
    if start < end:
        split = sort_quickly(alist, start, end)
        quick_sort(alist, start, split - 1)  # we leave the pivot point alone hence the -1
        quick_sort(alist, split + 1, end)  # we leave the pivot point alone hence the +1

def sort_quickly(alist, pivot_idx=0, rp=None):
    if len(alist) <= 1:
        return
    if rp is None:
        rp = len(alist) - 1

    lp = pivot_idx + 1

    done = False
    while not done:
        while lp <= rp:
            if alist[lp] >= alist[pivot_idx]:
                break
            lp += 1
        while lp <= rp:
            if alist[rp] <= alist[pivot_idx]:
                break
            rp -= 1
        if lp > rp:
            done = True  # done to avoid infinite loop
        else:
            alist[lp], alist[rp] = alist[rp], alist[lp]
            rp -= 1
    alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]
    return rp  # return the split point which we should not include in next calls

def quick_sort_mid(alist, start=0, end=None):
    if end is None:
        end = len(alist) - 1
    if start < end:
        split = sort_quickly_mid(alist, start, end)
        quick_sort_mid(alist, start, split - 1)  # we leave the pivot point alone hence the -1
        quick_sort_mid(alist, split + 1, end)  # we leave the pivot point alone hence the +1

def sort_quickly_mid(alist, pivot_idx=0, rp=None):
    if len(alist) <= 1:
        return
    if rp is None:
        rp = len(alist) - 1

    alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]

    lp = pivot_idx + 1

    done = False
    while not done:
        while lp <= rp:
            if alist[lp] >= alist[pivot_idx]:
                break
            lp += 1
        while lp <= rp:
            if alist[rp] <= alist[pivot_idx]:
                break
            rp -= 1
        if lp > rp:
            done = True  # done to avoid infinite loop
        else:
            alist[lp], alist[rp] = alist[rp], alist[lp]
            rp -= 1  # if we dont include this then infinite swaps happen when two numbers are equal
    alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]
    return rp  # return the split point which we should not include in next calls

def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    mid = len(alist)//2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    l = 0
    r = 0

    k = 0

    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            alist[k]= left[l]  # i don't get why we can just overwrite stuff from 0 to len(alist) just like this
            l += 1
        else:
            alist[k] = right[r]
            r += 1
        k += 1

    if l == len(left):
        while r < len(right):
            alist[k] = right[r]
            r += 1
            k += 1
    elif r == len(right):
        while l < len(left):
            alist[k] = left[l]
            l += 1
            k += 1

    return alist

def shell_sort(a_list):
    big_step = len(a_list) // 2
    while big_step > 0:
        for steps in range(big_step):  # this makes it move every steps'th while not colliding with past results
            shell_insertion_sort(a_list, steps, big_step)
        big_step //= 2

def shell_insertion_sort(alist, steps, big_step):
    for i in range(steps+big_step, len(alist),big_step):  # steps + big_step is here so we skip comparing 0 and -4 - its like that 1 in range(1,len(list)) in insertion sort
        saved_value = alist[i]
        pos = i
        while pos >= big_step:  # curpos >= gap is so we dont address -1 index, other condition is that we dont do anything if cur val is bigger than prev val
            if alist[pos-big_step] < saved_value:
                break
            alist[pos] = alist[pos-big_step]
            pos -= big_step
        alist[pos] = saved_value

def insertion_sort(val):
    for i in range(1,len(val)):
        temp = val[i]

        j = 0

        for j in range(i,-1,-1):
            if val[j-1] < temp:
                break
            val[j] = val[j-1]

        val[j] = temp

def selection_sort(value):
    for i in range(len(value)-1,0,-1):
        biggest = 0
        for j in range(i+1):
            if value[j] > value[biggest]:
                biggest = j
        value[i],value[biggest] = value[biggest], value[i]

def bubble_sort_short(value):
    for i in range(len(value)-1,0,-1):
        issorted = True
        for j in range(i):
            if value[j] > value[j+1]:
                issorted = False
                value[j], value[j+1]  = value[j+1],  value[j]
        if issorted:
            return





sort_history = dict()
sort_history['quick_sort_mid'] = []
sort_history['quick_sort'] = []
sort_history['merge_sort'] = []
sort_history['shell_sort'] = []
sort_history['insertion_sort'] = []
sort_history['selection_sort'] = []
sort_history['bubble_sort_short'] = []

sizes = [500,2750,5000]#,8750,12500] #takes a while if uncomment

for sort in sort_history.keys():
    for size in sizes:
        randlist = [rng.randint(0,400) for i in range(size)]
        sort_history[sort].append(timeit.timeit(f'{sort}({randlist})', number=2, globals= globals()))

colors = ['b','g','r','c','m','y','k']

for key,color in zip(sort_history,colors):
    values = sort_history[key]
    print(f'Average for {key} is {round(sum(values)/len(values),4)} sec')
    plt.plot(sizes, sort_history[key], color=color, label=f'{key}')


# Naming the x-axis, y-axis and the whole graph
plt.xlabel("datasize")
plt.ylabel("time")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()