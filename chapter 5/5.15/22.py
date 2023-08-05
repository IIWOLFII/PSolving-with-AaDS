def quick_sort_part(alist, start=0, end=None, partitionlim=4):
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



a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort_part(a_list)
print(a_list)