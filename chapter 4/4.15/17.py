#Suppose you are a computer scientist/art thief who has broken into a major art gallery.
# All you have with you to haul out your stolen art is your knapsack which only holds W pounds of art, but
# for every piece of art you know its value and its weight.
# Write a dynamic programming function to help you maximize your profit.
# Here is a sample problem for you to get started: suppose your knapsack can hold a total weight of 20 pounds.
# You have 5 items as follows:
# item     weight      value
#   1        2           3
#   2        3           4
#   3        4           8
#   4        5           8
#   5        9          10


# these problems are extremely easy but i keep taking way too long
# i need to find an approach to these things or/and develop an intuition (how?)


def totalbagvalue(bag):
    totalvalue = 0

    for item in bag:
        totalvalue += value[int(item)]

    return totalvalue

def arttheif(slim, history = None):  # now i understand but it still feels like it shouldnt be working
    if history is None:
        history = ''

    v = ''
    maxvalue = float('-inf')

    if slim < 0:
        return None

    for item in items:
        if str(item) in history:
            continue

        res = arttheif(slim-weights[item], history + str(item))

        if res is not None:
            # we got string returned containing v which if nothing means that we just have reached the bottom case
            # aka no suitable items were found, or weight was just exceeded
            # so we shlap our current item to contents of v and if more expensive, set it to v at this scope, which we
            # pass along higher and then we do this loop until we reach initial return
            newv = res + str(item)
            newv_value = totalbagvalue(newv)
            if maxvalue < newv_value:
                maxvalue = newv_value
                v = newv

    return v

items = [i for i in range(5)]
weights = [2,3,4,5,9]
value = [3,4,8,8,10]
sacklimit = 20

items = [i for i in range(3)]
sacklimit = 4
value = [1,2,3]
weights = [4,5,1]

items = [i for i in range(3)]
sacklimit = 3
value = [1,2,3]
weights = [4,5,6]

items = [i for i in range(10)]
sacklimit = 165
value = [92,57,49,68,60,43,67,84,87,72]
weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]

items = [i for i in range(5)]
sacklimit = 7
value = [5,2,3,4,2]
weights = [4, 3, 2, 3, 1]

assert len(items) == len(weights) == len(value)

a = arttheif(sacklimit)

print(a)

for thing in a:
    thing = int(thing)
    print(f"Item {thing} worth {value[thing]} weights {weights[thing]}")

print(f"Space left: {sacklimit - sum([weights[int(thing)] for thing in a])}/{sacklimit} ")
print(f"Total value: {totalbagvalue(a)}")


# def canstealsomething(slim, bag = None):  # this problem is easy yet i struggle
#     if bag is None:
#         bag = ""
#
#     if slim < 0:
#         return None
#
#     res = None
#     bestvalue = float('-inf')
#     newitem = ''
#
#     for item in items:
#         if str(item) in bag:
#             continue
#
#         res = canstealsomething(slim-weights[item], bag + str(item))
#
#         if res is not None:
#             if bestvalue < totalbagvalue(bag):
#                 newitem = str(item) + res
#         else:
#             continue
#         # if total value of stuff in it is bigger than previous, set returning item to current item
#
#
#     return newitem


# def canstealsomething(slim, bag = None):  # does not work for no reason
#     global value,weights,items
#
#     if bag is None:
#         bag = []
#
#     if slim == 0:
#         return []
#     if slim < 0:
#         return None
#
#     curwealth = 0
#     maxwealth = float('-inf')
#     maxbag = []
#
#     for item in items:
#         if item in bag:
#             continue
#
#         bag.append(item)
#         res = canstealsomething(slim - weights[item], bag)
#
#         if res is None:
#             bag.pop(bag.index(item))
#             maxbag = bag
#         elif res is not None:
#             slim -= weights[item]
#             for thing in bag:
#                 curwealth += value[thing]
#
#             if maxwealth < curwealth:
#                 maxwealth = curwealth
#                 maxbag = bag.copy()
#
#     return maxbag