# This problem is called the string edit distance problem, and is quite useful in many areas of research.
# Suppose that you want to transform the word algorithm into the word alligator.
# For each letter you can either copy the letter from one word to another at a cost of 5, you can
# delete a letter at cost of 20, or insert a letter at a cost of 20.
# The total cost to transform one word into another is used by spell-check programs to provide suggestions for words
# that are close to one another.
# Use dynamic programming techniques to develop an algorithm
# that gives you the smallest edit distance between any two words.


# now i get it
# https://archive.org/details/31DefiningMinimumEditDistanceStanfordNLPProfessorDanJurafskyChrisManning/3+-+1+-+Defining+Minimum+Edit+Distance+-+Stanford+NLP+-+Professor+Dan+Jurafsky+%26+Chris+Manning.mp4
# https://web.stanford.edu/class/cs124/lec/med.pdf
# https://www.youtube.com/watch?v=XYi2-LPrwm4

# http://www.inrg.csie.ntu.edu.tw/algorithm2013/homework/Wagner-74.pdf - must be in Elvish


# 931 / 1146 test cases passed

# the good solution uses tabulation
# too bad the book is as useless on teaching tabulation as any other source i can find - ppl give you complete ..
# .. matrix with logic attached to it instead of explaining how they got there

# cancer

def insert_copy(current,goal,targetindex):
    return current[:targetindex] + goal[targetindex] + current[targetindex + 1:]

def del_ete(current,targetindex):
    return current[:targetindex] + current[targetindex+1:]

def string_distance(current,goal, original = None, memo = None):
    if original is None:
        original = current
    if memo is None:
        memo = dict()

    if current in memo:
        return memo[current]
    if current == goal:
        return 0

    targetindex = 0
    for letter1,letter2 in zip(current,goal):
        if letter1 != letter2:
            break
        targetindex += 1

    res = None
    cheapest = float('+inf')

    if targetindex <= len(goal)-1:
        if goal[targetindex] not in original:
            val_inserting = insert_copy(current, goal, targetindex)
            res = string_distance(val_inserting, goal, original, memo) + 20
        else:
            val_copying = insert_copy(current, goal, targetindex)
            res = string_distance(val_copying, goal, original, memo) + 5

    if res:
        if cheapest > res:
            cheapest = res
            memo[current] = cheapest

    val_deleting = del_ete(current, targetindex)
    res = string_distance(val_deleting, goal, original,memo) + 20

    if cheapest > res:
        cheapest = res
        memo[current] = cheapest

    return cheapest




a = 'horse'
b = 'ros'
final = string_distance(a, b)
print(f'{a} --> {b}\ncost: {final}\n====')

a = 'intention'
b = 'execution'
final = string_distance(a, b)
print(f'{a} --> {b}\ncost: {final}\n====')

a = 'park'
b = 'spake'
final = string_distance(a, b)  # incorrect by 1 step
print(f'{a} --> {b}\ncost: {final}\n====')

# def string_distance(current,goal, original = None):
#     print(f"{current=}, {goal=}, {original=}")
#     if original is None:
#         original = current
#     if current == goal:
#         print('GOAL')
#         return 0
#
#     targetindex = 0
#     for letter1,letter2 in zip(current,goal):
#         if letter1 != letter2:
#             break
#         targetindex += 1
#
#     print(f'{targetindex=}')
#
#
#
#     if targetindex == len(current):
#         val_inserting = insert_copy(current,goal,targetindex)
#         string_distance(val_inserting ,goal, original)
#         return
#
#     if targetindex == len(goal):
#         print('current is bigger than goal')
#
#     elif goal[targetindex] not in original:
#         val_inserting = insert_copy(current, goal, targetindex)
#         print(f"{val_inserting=}")
#         string_distance(val_inserting ,goal, original)
#
#     else:
#         val_copying = insert_copy(current,goal,targetindex)
#         print(f"{val_copying=}")
#         string_distance(val_copying, goal, original)
#
#     val_deleting = del_ete(current, targetindex)
#     print(f"{val_deleting=}")
#     string_distance(val_deleting, goal, original)
#
#     return



