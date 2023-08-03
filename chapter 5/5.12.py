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
            rp -= 1  # if we dont include this then infinite swaps happen when two numbers are equal
    alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]
    return rp  # return the split point which we should not include in next calls

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)



# def quick_sort(alist,pivot_idx = 0,rp = None):
#     if rp is None:
#         rp = len(alist)-1
#     if pivot_idx < rp:
#         rp = sort_quickly(alist, 0, rp)
#         quick_sort(alist,0,rp-1)  # we leave the pivot point alone hence the -1
#         quick_sort(alist,rp+1)  # we leave the pivot point alone hence the +1
#
# def sort_quickly(alist,pivot_idx = 0,rp = None):  # idk
#     if len(alist) <= 1:
#         return
#     if rp is None:
#         rp = len(alist)-1
#     lp = pivot_idx + 1
#     done = False
#     while not done:
#         while lp <= rp:  # idk
#             if alist[lp] >= alist[pivot_idx]:
#                 break
#             lp += 1
#         while lp <= rp:  # idk
#             if alist[rp] <= alist[pivot_idx]:
#                 break
#             rp -= 1
#         if lp > rp:
#             done = True  # why is this required
#         else:
#             alist[lp], alist[rp] = alist[rp], alist[lp]
#     alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]
#     return rp  # return the split point which we should not include in next calls



# def quick_sort(alist,lp = 1,rp = None):  # i dont get it
#     if len(alist) <= 1:
#         return
#
#     if rp is None:
#         rp = len(alist)-1
#
#     pivot_idx = lp - 1
#
#     while True:
#         while lp < len(alist) and lp <= rp:  # idk
#             if alist[lp] <= alist[pivot_idx]:
#                 break
#             lp += 1
#
#         while rp > 0 and lp <= rp:  # idk
#             if alist[rp] >= alist[pivot_idx]:
#                 break
#             rp -= 1
#
#         if lp > rp:
#             break
#
#         alist[lp], alist[rp] = alist[rp], alist[lp]
#
#     alist[pivot_idx], alist[rp] = alist[rp], alist[pivot_idx]
#
#     quick_sort(alist,rp+1)
#     quick_sort(alist,1, rp)
