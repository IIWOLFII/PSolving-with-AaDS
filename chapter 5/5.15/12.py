# bin search

def bin_search(num, alist, beg=0, end=None):
    if end is None:
        end = len(alist) - 1
    if beg > end:
        return False

    middle = (end + beg) // 2

    if alist[middle] == num:
        return True  # return middle for index
    elif alist[middle] > num:
        return bin_search(num, alist, beg, middle - 1)
    elif alist[middle] < num:
        return bin_search(num, alist, middle + 1, end)


a_list = [17, 20, 31, 44, 54, 54, 55, 77, 93]
print(a_list)
res = bin_search(93, a_list)
print(res)
