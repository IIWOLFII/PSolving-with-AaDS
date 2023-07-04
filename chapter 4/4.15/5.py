def reverselist(li, revli = list()):
    if len(li) == 0:
        return

    reverselist(li[1:], revli)
    revli.append(li[0])

    return revli

a = ['A','B','C','DEEZ']

reva = reverselist(a)

print(reva)

