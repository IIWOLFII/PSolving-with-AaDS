#https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf page 16

def insertion_sort(val):
    for i in range(1,len(val)):
        temp = val[i]

        j = 0

        for j in range(i,-1,-1):
            if val[j-1] < temp:
                break
            val[j] = val[j-1]

        val[j] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

#a_list = [2,4,1]

insertion_sort(a_list)
print(a_list)


# a = [2,4,1]
#
# i = 2
#
# val = a[2]
# a[2] = a[1]
#
# if val > a[0]:
#     a[1] = val
#
# a[1] = a[0]
#
# if val > a[-1]:
#    a[0] = val



# def insertion_sort(val):
#     for i in range(1,len(val)):
#         temp = val[i]
#         for j in range(i,0,-1):
#             if val[j-1] > temp or j > 0:
#                 val[j] = val[j-1]
#             val[j] = temp



# def insertion_sort(val):
#     for i in range(1,len(val)):
#         fuck = val[i]
#         this = val[i-1]
#         debugger = val[i] > val[i-1]
#
#         data = val[i]
#         iterator = i
#         while True:
#             if iterator == 0:
#                 val[iterator] = data
#                 break
#
#             if val[iterator] > val[iterator - 1]:
#                 break
#
#             val[iterator] = val[iterator-1]
#             iterator -= 1



# def insertion_sort(value):
#
#     for i in range(1,len(value)):
#         if value[i] > value[i-1]:
#             continue
#
#         newval = value[i]
#         for j in range(i-1,-1,-1):
#             if value[j-1] < newval:
#                 value[j] = newval
#
#             value[j],value[j-1] = value[j-1],value[j]



# def insertion_sort(value):
#     cur_idx = 0
#
#     for i in range(1,len(value)):
#         if value[i] >= value[cur_idx]:
#             cur_idx += 1
#             continue
#         elif value[i] < value[cur_idx]:
#             for j in range(i):
#                 if i-j > 0:
#                     value[i-j] = value[i]
#                 else:
#                     value[0] == 1



# def insertion_sort(value):
#     cur_pos = 0
#     i_offset = 0
#     for i in range(1,len(value)):
#         i = i - i_offset
#         if value[i] < value[cur_pos]:
#             j = i-1
#             while j > 0:
#                 if value[i] < value[j]:
#                     j -= 1
#                 else:
#
#                     break
#             i_offset += 1
#             hand = value.pop(i)
#             value.insert(j+1, hand)
#         else:
#             cur_pos += 1


