import timeit
import random as rng

import matplotlib.pyplot as plt

def quick_sort_part(alist, start=0, end=None, partitionlim=2):
    if end is None:
        end = len(alist) - 1
    if start < end:
        split = sort_quickly_part(alist, start, end)
        quick_sort_part(alist, start, split - 1, partitionlim)  # we leave the pivot point alone hence the -1
        quick_sort_part(alist, split + 1, end, partitionlim)  # we leave the pivot point alone hence the +1

def sort_quickly_part(alist, pivot_idx=0, rp=None, partitionlim=4):
    if len(alist) <= 1:
        return
    if rp is None:
        rp = len(alist) - 1
    lp = pivot_idx + 1
    if rp-pivot_idx <= partitionlim:
        insertion_quicksort(alist, pivot_idx, rp)
        return rp
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

def insertion_quicksort(val, begin, end):
    for i in range(begin,end+1):
        temp = val[i]
        j = 0
        for j in range(i,-1,-1):
            if val[j-1] < temp:
                break
            val[j] = val[j-1]
        val[j] = temp

def quick_sort_median(alist, start=0, end=None):
    if end is None:
        end = len(alist) - 1
    if start < end:
        split = sort_quickly_median(alist, start, end)
        quick_sort_median(alist, start, split - 1)  # we leave the pivot point alone hence the -1
        quick_sort_median(alist, split + 1, end)  # we leave the pivot point alone hence the +1

def sort_quickly_median(alist, pivot_idx=0, rp=None):
    if len(alist) <= 1:
        return
    if rp is None:
        rp = len(alist) - 1
    lp = pivot_idx + 1

    med_ix = select_median(alist,lp,rp)
    alist[pivot_idx], alist[med_ix] = alist[med_ix], alist[pivot_idx]

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

def select_median(alist, beg, length):
    mid = (beg + length) // 2
    idx = [beg, mid, length]
    vals = [alist[beg], alist[mid], alist[length]]

    for i in range(len(vals)-1,0,-1):
        for j in range(i):
            if vals[j] > vals[j+1]:
                idx[j], idx[j+1] = idx[j+1], idx[j]
                vals[j], vals[j+1] = vals[j+1], vals[j]

    middleindex = idx[1]  # return the middle index of the three

    idx.sort()  # sort the indecies

    for i,val in zip(idx,vals):  # sort the values
        alist[i] = val

    return middleindex

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

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_median(a_list)
print(a_list)

sort_history = dict()
sort_history['quick_sort_median'] = []
sort_history['quick_sort'] = []
sort_history['quick_sort_mid'] = []
sort_history['quick_sort_part'] = []


sizes = [500,2750,5000,8750,20500] #takes a while if uncomment

for sort in sort_history.keys():
    for size in sizes:
        randlist = [rng.randint(0,400) for i in range(size)]
        sort_history[sort].append(timeit.timeit(f'{sort}({randlist})', number=10, globals= globals()))

colors = ['b','r','g','k']

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

