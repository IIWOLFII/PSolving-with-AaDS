def bubble_sort_bidir(value):
    for i in range(len(value)-1,0,-1):
        issorted = True
        for j in range(i):
            if value[j] > value[j+1]:
                issorted = False
                value[j], value[j+1]  = value[j+1],  value[j]
        for j in range(i,0,-1):
            if value[j] < value[j-1]:
                issorted = False
                value[j], value[j-1]  = value[j-1],  value[j]
        if issorted:
            return


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort_bidir(a_list)
print(a_list)