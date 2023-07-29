def shell_sort(a_list):
    big_step = len(a_list) // 2
    while big_step > 0:
        for steps in range(big_step):  # this makes it move every steps'th while not colliding with past results
            insertion_sort(a_list,steps,big_step)
        big_step //= 2

def insertion_sort(alist,steps,big_step):
    for i in range(steps+big_step, len(alist),big_step):  # steps + big_step is here so we skip comparing 0 and -4 - its like that 1 in range(1,len(list)) in insertion sort
        saved_value = alist[i]
        pos = i
        while pos >= big_step:  # curpos >= gap is so we dont address -1 index, other condition is that we dont do anything if cur val is bigger than prev val
            if alist[pos-big_step] < saved_value:
                break
            alist[pos] = alist[pos-big_step]
            pos -= big_step
        alist[pos] = saved_value

# def insertion_sort(alist,steps,big_step):
#     for i in range(1, len(alist)):
#         saved_value = alist[i]
#
#         pos = i
#         while pos > 0:
#             if alist[pos-1] < saved_value:
#                 break
#
#             alist[pos] = alist[pos-1]
#             pos -= 1
#
#         alist[pos] = saved_value


#a_list = [0,  1,  2,  3,  4,  5,  6,  7,  8]
a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

shell_sort(a_list)
print(a_list)



# def insertion_sort(val):
#     for i in range(1,len(val)):
#         temp = val[i]
#         cur_idx = i
#         while cur_idx > 0:
#             if val[cur_idx-1] < temp:
#                 break
#             val[cur_idx] = val[cur_idx-1]
#             cur_idx -= 1
#         val[cur_idx] = temp
#
# def shell_sort(alist):
#     gap = 3
#     for j in range(gap):
#         for i in range(1,gap):
#             curidx = i*gap+j
#             previdx = curidx - gap
#             if alist[curidx] < alist[previdx]:
#                 alist[curidx], alist[previdx] = alist[previdx], alist[curidx]
#     insertion_sort(alist)
#
# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(a_list)
# print(a_list)