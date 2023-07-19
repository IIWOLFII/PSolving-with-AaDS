# Write a program that solves the following problem. Three missionaries and three cannibals come to a river and
# find a boat that holds two people. Everyone must get across the river to continue on the journey.
# However, if the cannibals ever outnumber the missionaries on either bank, the missionaries will be eaten.
# Find a series of crossings that will get everyone safely to the other side of the river.

# time wasted 3+ hrs

# shouldnt have tried spliced attempts such as MM CM CC
# sending single guy is not an issue as long as u handle it properly
# still dont understand why we iterate m and c in range of boat slots
# still dont understand how he doesnt get stuck in a move by only looking at previous move

def islegal(currentbank):
    global leftbank, rightbank
    if leftbank['C'] > leftbank['M'] and leftbank['M'] > 0:
        return False
    if rightbank['C'] > rightbank['M'] and rightbank['M'] > 0:
        return False

    if sum(rightbank.values()) == 1 and sum(leftbank.values()) > 0 and currentbank == rightbank: # if right bank has only 1 person and the boat is also there that means only 1 went there last time
        return False  # horrible

    return True

def move1personto(who,to,fromm):
    if fromm[who] - 1 >= 0:
        fromm[who] = fromm[who] - 1
        to[who] = to[who] + 1
        return True
    else:
        return False

def solve(curbank, other, memo = None):  # i hope nothing happens to children of authors of this book for putting ..
    # .. this problem in recursive section considering this is a state search problem which is infinitely harder in recursion
    global lastmove

    if memo is None:
        memo = dict()

    success = False

    if not islegal(curbank):
        return False

    if sum(leftbank.values()) == 0:
        return True


    for attempt in ['CC','MM','CM','C','M']:
        if attempt == lastmove:
            continue

        if f"{leftbank},{rightbank},{attempt},{curbank}" in memo:
            a = memo[f"{leftbank},{rightbank},{attempt},{curbank}"]
            if not a:
                continue

        position = 1
        for i in attempt:
            suc = move1personto(i,other,curbank)
            if not suc: # if it is not unsuccessful but on first letter then it does nothing so no need to undo
                if position == 2: # if we are on second letter then we need to undo previous step
                    move1personto(i, curbank, other)
                break
            position += 1

        # if we ever find ourselfs in a situation with same everything and same moves that means we are in a loop

        memo[f"{leftbank},{rightbank},{attempt},{curbank}"] = False  # i cant believe this worked i want to die ..
                                                                    # .. we assume that any move is incorrect  ..
                                                                    # .. and its ok bcuz if we get True, it returns  ..
        lastmove = attempt                                          # .. True back up recursively below

        if suc == True:
            success = solve(other,curbank, memo)
        else:
            success = solve(curbank, other, memo)

        if not success:
            memo[f"{leftbank},{rightbank},{attempt},{curbank}"] = False
            for i in attempt:
                move1personto(i, curbank, other)
        else:
            return True





    return success




for ppl in range(1,5):  # 1 - 4 max
    print(f'{ppl} M and C')

    lastmove = ''
    people_per_group = ppl  # 5+ is impossible and overflows stack limit even if we raise it

    leftbank = {"M": people_per_group, "C": people_per_group, "LEFT":0}
    rightbank = {"M": 0, "C": 0, "RIGHT": 0}
    res = solve(leftbank, rightbank)

    print(res)
    print(leftbank,rightbank)
    print('====' * 4)





# def canload1person(who,where):
#     global leftbank,rightbank, boat
#     if where[who] - 1 > 0:
#         return True
#     return False
#
# def islegal():
#     global leftbank, rightbank, boat
#     if leftbank['C'] > leftbank['M']:
#         return False
#     if rightbank['C'] > rightbank['M']:
#         return False
#     return True
#
# def load1person(who,where):
#     global leftbank,rightbank, boat
#     where[who] -= 1
#     boat[who] += 1
#     print(f'Loaded 1 {who}')
#     return True
#
# def otherbank(bank):
#     if bank == leftbank:
#         return rightbank
#     else:
#         return leftbank
#
# def solve(currentbank):
#     success = False
#     other = otherbank(currentbank)
#
#     if sum(leftbank.values()) == 0:
#         return True
#
#     if sum(boat.values()) == 0:
#         return False
#
#     if not islegal():
#         return False
#
#     if canload1person('M',other):
#         load1person('M',other)
#         success = solve(other)
#     elif canload1person('C',other):
#         load1person('C',other)
#         success = solve(other)
#
#     return success
#
#     # try loading C
#     # recurse
#
#     # iterate through combinations of people
#     # load combination of people
#     # recurse
#     # if its false that means it tried the path and it didnt work all the way down or smth so undo the change
#     #   meaning try other paths or return false if none of them hit
#     # if its true that means it reached the base case and we backtrack while returning the way we got there return true
#
#
# lastperson = None
#
# people_per_group = 1
#
# leftbank = {"M": people_per_group, "C": people_per_group} #0
# boat = {"M": 0, "C": 0}
# rightbank = {"M": 0, "C": 0} #1
#
# res = solve(leftbank)
# print(res)
#
# # 000 ### _____   # input
# # 000 # _____ ##  # move cannibal bruddas over
# # 000 ## _____ #  # move cannibal bruddas over
# # 000  _____ ###  # move cannibal bruddas over -> # swap bruddas
# # 000 # _____ ##  # swap bruddas
# # 0 # _____ 00 ##  # swap bruddas
# # 00 ## _____ 0 #  # swap bruddas
# # ## _____ 000 #  # swap bruddas
# # ### _____ 000  # swap bruddas -> # move cannibal bruddas over
# # # _____ 000 ##  # move cannibal bruddas over
# # ## _____ 000 #  # move cannibal bruddas over
# #  _____ 000 ###  # move cannibal bruddas over
#
#
# # 00 ## _____  # input
# # 00 _____ ##  # move cannibal bruddas over -> # swap bruddas
# # 00 # _____ #  # swap bruddas
# # # _____ # 00  # swap bruddas
# # ## _____ 00  # swap bruddas -> # move cannibal bruddas over
# # _____ 00 ##  # move cannibal bruddas over
#
# # 0 # _____  # input
# # _____ 0 #  # move both  (special case ???)
#
#
#
# # def load1person(who):
# #     global leftbank, boat
# #     if leftbank[who]-1 <= 0:
# #         return False
# #     leftbank[who] -= 1
# #     boat[who] += 1
# #     print(f'Loaded 1 {who}')
# #     return True
# #
# # def unloadboat():
# #     global leftbank, boat
# #     while boat['M'] > 0:
# #         boat['M'] -= 1
# #         leftbank['M'] += 1
# #         # print('Unloaded 1 missionary')
# #
# #     while boat['C'] > 0:
# #         boat['C'] -= 1
# #         leftbank['C'] += 1
# #         # print('Unloaded 1 cannibal')
# #
# # def sendboat():
# #     global leftbank, rightbank, boat
# #
# #     print(f'Boat containing {boat} moves over to another shore')
# #     while boat['M'] > 0:
# #         boat['M'] -= 1
# #         rightbank['M'] += 1
# #         print('Unloaded 1 missionary')
# #
# #     while boat['C'] > 0:
# #         boat['C'] -= 1
# #         rightbank['C'] += 1
# #         print('Unloaded 1 cannibal')
# #
# # def returnboat(whowillreturn):
# #     rightbank[whowillreturn] -= 1
# #     leftbank[whowillreturn] += 1
# #     #print(f'Boat returns with 1 {whowillreturn}')
# #
# # def islegal():
# #     global leftbank, rightbank, boat
# #     if leftbank['C'] > leftbank['M']:
# #         return False
# #     if rightbank['C'] > rightbank['M']:
# #         return False
# #     return True
# #
# # def solve(persontoload=None, arg2=None):
# #     success = False
# #
# #     if sum(leftbank.values()) == 0:  # base case
# #         return True
# #
# #     if not islegal():
# #         return False
# #
# #     if persontoload is not None:
# #         a = load1person(persontoload)
# #         if a is False:
# #             return False
# #
# #     if arg2:
# #         sendboat()
# #         solve()
# #
# #     while success == False:
# #         success = solve('M', 'M')
# #         if not success:
# #
# #         success = solve('M', 'C')
# #         success = solve('C', 'C')
# #         success = solve('C')
# #         success = solve('M')
# #         break
# #
# #     # iterate through combinations of people
# #     # load combination of people
# #     # recurse
# #     # if its false that means it tried the path and it didnt work all the way down or smth so undo the change
# #     #   meaning try other paths or return false if none of them hit
# #     # if its true that means it reached the base case and we backtrack while returning the way we got there return true
# #
# #     return success