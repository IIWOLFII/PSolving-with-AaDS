def bubble_sort_bidir(value, start = None, end = None, dir = -1):
    if start is None:
        start = 0
    if end is None:
        end = len(value)-1

    # for i in range(end,start,dir):
    #     issorted = False
    #
    #     for j in range(i):
            if value[j] > value[j+dir]:
                value[j], value[j+dir]  = value[+dir],  value[j]
        #     else:
        #         issorted = True
        #
        # if issorted:
        #     return

    bubble_sort_bidir(value,end,start,dir * -1)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort_bidir(a_list)
print(a_list)