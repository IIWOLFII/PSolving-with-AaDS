
def selection_sort(value):
    for i in range(len(value)-1,0,-1):
        biggest = 0
        for j in range(i+1):
            if value[j] > value[biggest]:
                biggest = j
        value[i],value[biggest] = value[biggest], value[i]



a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

selection_sort(a_list)

print(a_list)


