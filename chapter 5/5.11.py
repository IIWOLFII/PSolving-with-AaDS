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

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)



# def merge_sort(alist):  # i cant believe it works
#     if len(alist) <= 1:
#         return alist
#
#     mid = len(alist)//2
#     left = merge_sort(alist[:mid])
#     right = merge_sort(alist[mid:])
#
#     wtf = []
#
#     l = 0
#     r = 0
#
#     while l < len(left) and r < len(right):
#         if left[l] <= right[r]:
#             wtf.append(left[l])
#             l += 1
#         else:
#             wtf.append(right[r])
#             r += 1
#
#     if l == len(left):
#         wtf += right[r:]
#     elif r == len(right):
#         wtf += left[l:]
#
#     return wtf
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bruh = merge_sort(a_list)
# print(a_list)
# print(bruh)