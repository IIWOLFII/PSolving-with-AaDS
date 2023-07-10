# https://www.youtube.com/watch?v=oBt53YbR9Kk

def minsum_memo(num, numlist, memo=None):
    # global calls
    # calls += 1

    if memo is None:  # memo didnt work for ages bcuz this was // if not memo: // which translates to ...
        memo = dict()  # ... if len(memo) == 0 or memo is None but i only needed the second one, grrr

    if num in memo:
        return memo[num]
    if num < 0:
        return None
    if num == 0:
        return []

    minres = None

    for i in numlist:
        if i > num:  # reduces calls 496 -> 432 ~ by 15%
            continue

        res = minsum_memo(num - i, numlist, memo)

        if res is None:
            continue

        if minres is None or len(res) < len(minres):
            minres = res + [i]

    memo[num] = minres
    return minres


calls = 0

for case in [(8, [2, 3, 5]),  # true 3 5
             (7, [5, 3, 4, 7]),  # true 7
             (63, [1, 5, 10, 21, 25]),  # true 21*3
             (7, [2, 4]),  # false
             (8, [1, 4, 5]),  # true 4*2
             (99, [1, 2, 5, 25, 36]),  # true, 36*2 + 25 + 2
             (300, [7, 14])  # false, 2^m*n
             ]:
    print(minsum_memo(*case))
    # print("Calls:", calls)
    # calls = 0

# def howsum_memo(num, numlist, memo=None):  # looks better
#     if not memo:
#         memo = dict()
#
#     if num < 0:
#         return None
#     if num == 0:
#         return []
#
#     if num in memo:
#         return memo[num]
#
#     for i in numlist:
#         res = howsum_memo(num - i, numlist, memo)
#         memo[num] = res
#
#         if res is not None:
#             return [i] + res
#
#     # print(memo)
#     return None
#
# for case in [(7,[2,3]), #true
#              (7,[5,3,4,7]), #true
#              (7,[2,4]), # false
#              (8,[2,3,5]), # true
#              (300,[7,14]) # false, 2^m*n
#              ]:
#     print(howsum_memo(*case))

# def howsum_memo(num, numlist, memory = None, memo = None): #i keep writing so much redundant code wow
#     if not memory:
#         memory = list()
#     if not memo:
#         memo = dict()
#
#     if num < 0:
#         return False
#     if num == 0:
#         return []
#
#     return_value = "null"
#
#     if num in memo:
#         return memo[num]
#
#     for i in numlist:
#
#         res = howsum_memo(num - i, numlist, memory, memo)
#         memo[num] = res
#
#         if isinstance(res,list):
#             memory.append(i)
#             return_value = memory + res
#             break
#
#     #print(memo)
#     return return_value
#
# for case in [(7,[2,3]), #true
#              (7,[5,3,4,7]), #true
#              (7,[2,4]), # false
#              (8,[2,3,5]), # true
#              (300,[7,14]) # false, 2^m*n
#              ]:
#     print(howsum_memo(*case))

# def howsum(num, numlist, memory = None):
#     if not memory:
#         memory = list()
#
#     if num < 0:
#         return False
#     if num == 0:
#         return []
#
#     wtf = "null"
#     for i in numlist:
#         res = howsum(num - i, numlist, memory)
#
#         if isinstance(res,list):
#             memory.append(i)
#             wtf = memory + res
#             break
#
#     return wtf
#
# for case in [(7,[2,3]), #true
#              (7,[5,3,4,7]), #true
#              (7,[2,4]), # false
#              (8,[2,3,5]) # true
#              #(300,[7,14]) # false, 2^m*n
#              ]:
#
#     print(howsum(*case))


# # what the FUCK is going on
# # 1) if i slap memory to None and initialise a list if none then it returns single number
# # 2) if i leave it as is, it sums the lists BETWEEN the functions despite them being separate entities wtf?
# # 3) if i clear list manually then it works like it should
# # ???????????????????
# # ok this makes sense https://www.w3docs.com/snippets/python/least-astonishment-and-the-mutable-default-argument.html
# # option 1 is the right one but needs fixing so it actually works
#
# def howsum(num, numlist, memory = list()):
#     if num < 0:
#         return False
#
#     if num == 0:
#         return True
#
#     for i in numlist:
#         possible = howsum(num - i, numlist, memory)
#         if possible:
#             memory.append(i)
#             break
#
#     return memory
#
#
# for case in [(7,[2,3]), #true
#              (7,[5,3,4,7]), #true
#              (7,[2,4]), # false
#              (8,[2,3,5]) # true
#              #(300,[7,14]) # false, 2^m*n ## i can not memo because of persistent list thing, wtf is going on
#              ]:
#
#     print(howsum(*case,list()))  # wtf why do i have to add new list every time what is this heresy


# def cansum(num,numlist):
#     if num < 0:
#         return False
#
#     if num == 0:
#         return True
#
#     for i in numlist:
#         if cansum(num-i,numlist):
#             return True
#     return False
#
#
# print(cansum(7,[2,3])) # true
# print(cansum(7,[5,3,4,7])) # true
# print(cansum(7,[2,4])) # false
# print(cansum(8,[2,3,5])) # true
# print(cansum(8,[2,3,6])) # true

# def cansum(num,numlist): # my code is longer and messier
#     #print(num)
#     if num < 0:
#         return False
#
#     if num in numlist or num == 0:
#         return True
#
#     possible = False
#     for i in numlist:
#         if i > num:
#             #print(f"is {i} > {num}?\n {i > num}")
#             continue
#         possible = cansum(num-i,numlist)
#         if possible:
#             break
#     #print(f"Possible for {num} is {possible}")
#     return possible
#
#
# print(cansum(7,[2,3])) # true
# print(cansum(7,[5,3,4,7])) # true
# print(cansum(7,[2,4])) # false
# print(cansum(8,[2,3,5])) # true
# #print(cansum(8,[2,3,6])) # false (n^n*2 w/o memo)

# def travel_memo(y, x, memo = dict()):
#     print(y, x)
#
#     if (x,y) in memo:
#         return memo[(x,y)]
#
#     elif y == 0 or x == 0:
#         return 0
#
#     elif y == 1 and x == 1:
#         return 1
#
#     else:
#         memo[(x,y)] = travel_memo(y - 1, x, memo) + travel_memo(y, x - 1, memo)
#         return memo[(x,y)]
#
# m = 3
# n = 4  # m x n grid ---- 10 exit paths
#
# e = dict()
# res = travel_memo(m, n, e)
# print(res)
# print(e)

# def travel(y,x): # im silly and drew the thing with thoughts in mind of tracking my depth, where bottom would be 5
#     print(y, x)    # and top would be 1, but this is recursion so its the other way around
#
#     if y == 0 or x == 0:
#         return 0
#
#     if y == 1 and x == 1:
#         return 1
#
#     return travel(y - 1, x) + travel(y, x - 1)
#
# m = 3
# n = 4  # m x n grid ---- 10 exit paths
#
# res = travel(m,n)
#
# print(res)


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
