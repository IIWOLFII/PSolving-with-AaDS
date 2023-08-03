# Quick sort middle pivot
import timeit
import random as rng

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

a_list = [54, 54, 93, 17, 77, 31, 44, 55, 20]
quick_sort_mid(a_list)
print(a_list)

qsmid = []
qs = []

for test in range(1,8):
    randlist = [rng.randint(0,1000) for i in range(test*4202)]

    quickmid = timeit.timeit(f'quick_sort_mid({randlist})', number=10, globals= globals())
    quicksor = timeit.timeit(f'quick_sort({randlist})', number=10, globals=globals())
    print(f'For data size of {test*4202}, quicksortmid took {quickmid} seconds, quicksort took {quicksor} seconds, quickmid is = {(1-(quickmid/quicksor))*100}% faster')
    qsmid.append(quickmid)
    qs.append(quicksor)


print(f'{qsmid=}, average is {sum(qsmid)}')
print(f'{qs=}, average is {sum(qs)}')