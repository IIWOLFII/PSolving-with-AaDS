# https://www.youtube.com/watch?v=oBt53YbR9Kk



# def travel(y,x, memo = dict()): #why wont it work wtf, i dont get when im supposed to memoize and which path
#     if y == 1 and x == 1:
#         print("Exit reached!")
#         return 1
#
#     if (x,y) in memo:
#         return memo[(x,y)]
#
#     if y - 1 > 0:
#         down = travel(y - 1, x) + 1
#         #memo[(x, y)] = down
#         return down
#
#     if x - 1 > 0:
#         right = travel(y, x - 1) + 1
#         #memo[(x, y)] = right
#         return right
#
#     return memo # fuck you problem, i dont know, youtube time
#
#
# m = 3
# n = 4  # m x n grid ---- 10 exit paths
#
# wtf = dict()
#
# a = travel(m,n, wtf)
#
# print(wtf)


def travel(y,x): # im silly and drew the thing with thoughts in mind of tracking my depth, where bottom would be 5
    print(y, x)    # and top would be 1, but this is recursion so its the other way around

    if y == 0 or x == 0:
        return 0

    if y == 1 and x == 1:
        return 1

    return travel(y - 1, x) + travel(y, x - 1)

m = 3
n = 4  # m x n grid ---- 10 exit paths

res = travel(m,n)

print(res)



# def travel(y,x): #i dont get it, where do i memoize ### fucked it up as well by using global and thinking about ...
#     global numex             # ... this the wrong way
#
#     print(y,x)
#
#     # if (x,y) in memo:
#     #     return memo[(x,y)]
#
#     if y == 1 and x == 1:
#         print("Exit reached!")
#         numex += 1
#         return
#
#     if y - 1 > 0:
#         travel(y - 1, x)
#
#     if x - 1 > 0:
#         travel(y, x - 1)
#     return
#
#
# m = 3
# n = 4  # m x n grid ---- 10 exit paths
#
# numex = 0
#
# travel(m,n)
#
# print(numex)

