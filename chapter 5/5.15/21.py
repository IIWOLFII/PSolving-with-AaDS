def merge_sort(alist,begin= 0,end = None):
    if end is None:
        end = len(alist)
    if end - begin <= 1:
        return alist

    mid = (end+begin)//2

    merge_sort(alist,begin,mid)
    merge_sort(alist,mid, end)

    l = begin
    r = mid

    merged = list()

    while l < mid and r < end:
        if alist[l] <= alist[r]:
            merged.append(alist[l])
            l += 1
        else:
            merged.append(alist[r])
            r += 1

    while l < mid:
        merged.append(alist[l])
        l+=1
    while r < end:
        merged.append(alist[r])
        r+=1

    mergidx = 0
    for i in range(begin,end):
        alist[i] = merged[mergidx]
        mergidx += 1


a_list = [54, 26, 93, 17, 77, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)