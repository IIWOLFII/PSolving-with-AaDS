
def bubble_sort_short(value):
    for i in range(len(value)-1,0,-1):
        issorted = True
        for j in range(i):
            if a[j] > a[j+1]:
                issorted = False
                a[j], a[j+1]  = a[j+1],  a[j]
        if issorted:
            return



a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#a = [20, 17, 26, 31, 44, 54, 55, 77, 93]

#a = [3,2,1]
bubble_sort_short(a)

print(a)


# def bubble_sort(value):
#
#     for i in range(len(value)-1,0,-1):
#         for j in range(i):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1]  = a[j+1],  a[j]
#
#
#
# a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
#
# #a = [3,2,1]
#
# bubble_sort(a)
#
# print(a)