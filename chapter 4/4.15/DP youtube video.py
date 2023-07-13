# https://www.youtube.com/watch?v=oBt53YbR9Kk

# personal tabulation observation: tabulation is not about finding something out then backtracing or doing anything ..
# .. else really, its about just slapping values on top of each other so you can return tab[goal] and it will be correct

def howsum_tab(goal, numlist):  # got the right result by accident, feelsbadman
    tablist = [False] * (goal + 1)
    tablist[0] = []

    for position in range(goal+1):
        if tablist[position] is False:
            continue

        for num in numlist:
            if (position + num) > goal:  # oob check
                continue

            tablist[position+num] = tablist[position] + [num]

            # print(f'tab+num from {position} at {position+num}', tablist[position+num])


            # if tablist[position+num] == goal:  # no need for early return, although if we overshoot, we might want ...
            #     return tablist[position]  # ... to stop since there is no way we can get to say 8 if we're at 9 with no success

    return tablist[goal]

print(howsum_tab(7, [2, 3]))  # t
# print(howsum_tab(7, [5, 3, 4, 7]))  # t
# print(howsum_tab(7, [2, 4]))  # f
# print(howsum_tab(8, [2, 3, 5]))  # t
# print(howsum_tab(300, [7, 14]))  # f


# def cansum_tab(goal, numlist):
#     tablist = [False] * (goal + 1)
#     tablist[0] = True
#
#
#     for position in range(goal+1):
#         if not tablist[position]:
#             continue
#
#         for num in numlist:
#
#             if (position + num) > goal:  # oob check
#                 continue
#
#             tablist[position+num] = True
#
#     return tablist[goal]
#
# print(cansum_tab(7,[2,3]))  # t
# print(cansum_tab(7,[5,3,4,7]))  # t
# print(cansum_tab(7,[2,4]))  # f
# print(cansum_tab(8,[2,3,5]))  # t
# print(cansum_tab(300,[7,14]))  # f


# def cansum_tab(goal, numlist):  # always returns true, does not work
#     tablist = [False] * (goal + 1)
#
#     for position in range(len(tablist)+1):
#         for num in numlist:
#             if (position + num) > goal:  # oob check
#                 continue
#
#             if position + num == goal:
#                 tablist[position+num] = True
#                 tablist[position] = True
#
#     return tablist[goal]
#
# print(cansum_tab(7,[2,3]))  # t
# print(cansum_tab(7,[5,3,4,7]))  # t
# print(cansum_tab(7,[2,4]))  # f
# print(cansum_tab(8,[2,3,5]))  # t
# print(cansum_tab(300,[7,14]))  # f



# def gridTraveler_tab(y, x): # its like linked list loop with slow and fast pointer - it works but makes 0 sense
#     field = [[0] * (x+1) for _ in range(y+1)]  # ffs i misplaced x and y all the way over here fuck me fuck me
#
#     field[1][1] = 1  # base case of recursive solution
#
#     for cury in range(y+1):  # without +1 it wont reach the y,x we are looking for
#         for curx in range(x+1):
#
#             curtile = field[cury][curx]
#
#             if curx+1 <= x:  # check for out of bounds
#                 field[cury][curx+1] += curtile  # how in the FUCK can this be out of fucking range fuck you UPD: dont assume anything, test EVERYTHING (i fucked up at very first line of fun)
#             if cury+1 <= y:   # check for out of bounds
#                 field[cury+1][curx] += curtile
#
#     # print('DEBUG', "=" *6)
#     # for row in field:
#     #     print(row)
#     # print('DEBUG', "=" *6)
#     return field[y][x]
#
#
# print(gridTraveler_tab(1, 1))
# print(gridTraveler_tab(2, 3))
# print(gridTraveler_tab(3, 2))
# print(gridTraveler_tab(3, 3))
# print(gridTraveler_tab(18, 18))


# def gridTraveler_BFS(y, x): # NEVERMIND its a complete different logic which i dont get so far
#     # y += 1  # fucks this whole thing up
#     # x += 1  #
#
#     field = [[0] * y for _ in range(x)]
#     field[0][0] = 1  # "base case of recursive solution" # is not actually required
#
#     queue = [(0, 0)]
#
#     while queue:
#         cury, curx = queue.pop(0)
#         rightx = curx + 1
#         downy = cury + 1
#         if rightx < x:
#             field[cury][rightx] += 1
#             queue.append((cury, rightx))
#         if downy < y:
#             field[downy][curx] += 1
#             queue.append((downy, curx))
#         # print("queue:", queue)  # DEBUG visualization
#         #
#         # for i in field:
#         #     print(i)
#         # print("=" * 10)
#     for row in field:
#         print(row)
#     return field[y - 1][x - 1]
#
# a = gridTraveler_BFS(3, 3)
# print(a)


# def fib_tab(goal):
#     dp = [0, 1] + ([0] * (goal - 1))
#
#     for pos in range(goal):
#         pointer1 = pos + 1
#         pointer2 = pointer1 + 1
#
#         for pt in [pointer1, pointer2]:
#             if pt < len(dp):
#                 dp[pt] += dp[pos]
#
#     return dp[goal]
#
# print(fib_tab(6))
# print(fib_tab(7))
# print(fib_tab(8))
# print(fib_tab(50))


# def fibonacci_tab(goal,bruj): # wrong ## huh you just push through an array thats cool
#     res = bruj[goal-1] + bruj[goal-2]
#     return res
# bruj = [0,1]
# wanted = 6
# for i in range(2,wanted+1):
#     bruj.append(fibonacci_tab(i,bruj))
# print(bruj[-1])
# print("="*14)
# print(bruj)


# def allConstruct_memo(target, wordbank, memo = None):  # cleaned up
#     if memo is None:
#         memo = {}
#     if target in memo:
#         return memo[target]
#
#     if target == "":
#         return [[]]
#
#
#     mem = []
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res = allConstruct_memo(target[len(word):], wordbank, memo)
#
#             for i in range(len(res)):
#                 mem.append([word] + res[i])
#
#     memo[target] = mem
#     return mem
#
#
#
# a = allConstruct_memo('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])  # true 4
# print(a)
#
# a = allConstruct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
# print(a)
#
# a = allConstruct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])
# print(a)
#
# a = allConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeez', ['e', 'ee', 'eee', 'eeee', 'eeeee'])
# print(a) # not the worst case anymore

# a = allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee', ['e', 'ee', 'eee', 'eeee', 'eeeee'])
# print(a)


# def allConstruct(target, wordbank):  # how is it possible that i keep writing code that does nothing
#     if target == "":
#         return [[]]  # controls the final output apparently
#
#     mem = False  # empty lists dont get added to list sum so this is pointless
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res = allConstruct(target[len(word):], wordbank)
###########################
#             if res is False: # empty lists dont get added to list sum so this is pointless
#                 continue     #
#             else:            #############
#                 if isinstance(mem,bool): #
#                     mem = []             # empty lists dont get added to list sum so this is pointless
###########################
#                 for i in range(len(res)):  # i just wrote this and then it just works for no reason ok cool
#                     mem.append([word] + res[i])  # i dont understand why this works
#
#     return mem
#
#
#
# a = allConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c'])  # true 4
# print(a)
#
# a = allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'])
# print(a)

# def allConstruct(target, wordbank, memo = None):  # idk how to get this to work # yeah i give up, fuck recursion
#     print('|')                                  # despite everything i have no coherent grasp on how this works
#                                                 # works on paper but not here, fuck you allConstruct()
#     if target == "":
#         return []
#
#     mem = False
#     biglist = []
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res = allConstruct(target[len(word):], wordbank)  # idk at what point i already have full words
#             if res is False:
#                 continue
#             else:
#                 if isinstance(mem,bool):
#                     mem = []
#                     mem. append([word])
#                 else:
#                     if isinstance(res,str): print("ITS A STRING HOW???", res)
#                     for i in res:
#                         i.append(word)
#                         return res
#     print(mem)
#     #print(mem)
#     return mem
#
#
# print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # true 2
# # print(allConstruct('', ['cat', 'mouse']))  # true
# # print(allConstruct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # true
# #print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # false


# def countConstruct_memo(target, wordbank, memo = None):
#     if memo is None:
#         memo = dict()
#
#     if target in memo:
#         return memo[target]
#     if target == "":
#         return 1
#
#     res = 0
#
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res += countConstruct_memo(target[len(word):], wordbank, memo)
#
#     memo[target] = res
#     return res
#
#
# print(countConstruct_memo('abcdef', ["ab", "abc", "cd", "def", "abcd"]))  # true
# print(countConstruct_memo('purple', ['purp', 'p', 'ur', 'le', 'purpl']))  # true 2
# print(countConstruct_memo('', ['cat', 'mouse']))  # true
# print(countConstruct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # true
# print(countConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # false


# def countConstruct_memo(target, wordbank, memo = None): #returns the used constructs, is not what needed from this fun
#     if memo is None:
#         memo = dict()
#
#     if target in memo:
#         return memo[target]
#
#     if target == "":
#         return ""
#
#     res = False
#
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res = countConstruct_memo(target[len(word):], wordbank, memo)
#             if res is not False:
#                 res = word + "," + res
#                 break
#
#     memo[target] = res
#     return res
#
#
# print(countConstruct_memo('abcdef', ["ab", "abc", "cd", "def", "abcd"]))  # true
# print(countConstruct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # false
# print(countConstruct_memo('', ['cat', 'mouse']))  # true
# print(countConstruct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # true
# print(countConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # false


# def canConstruct_memo(target, wordbank, memo = None): #O((n*m^2) time O(m^2) space
#     if memo is None:
#         memo = dict()
#
#     if target in memo:
#         return memo[target]
#     if target == "":
#         return True
#
#     res = False
#
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             res = canConstruct_memo(target[len(word):], wordbank, memo)
#
#         if res:
#             break
#
#     memo[target] = res
#     return res
#
#
# print(canConstruct_memo('abcdef', ["ab", "abc", "cd", "def", "abcd"]))  # true
# print(canConstruct_memo('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))  # false
# print(canConstruct_memo('', ['cat', 'mouse']))  # true
# print(canConstruct_memo('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))  # true
# print(canConstruct_memo('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))  # false


# def canConstruct(target,wordbank): #O((n^m)*m) time O(m^2) space
#     if target == "":
#         return True
#
#     beg = end = False
#
#     for word in wordbank:
#         if word not in target:
#             continue
#
#         if target[:len(word)] == word:
#             beg = canConstruct(target[len(word):], wordbank)
#
#         # print(f"target[len(word):] == word ::: {target[len(word):]} == {word}")
#         # if target[len(word):] == word: # we dont actually need this i guess, it wont ever get there
#         #     end = canConstruct(target[:len(word)], wordbank)
#
#         if beg: # or end
#             return True
#
#     return False
#
# print(canConstruct('abcdef', ["ab","abc","cd","def","abcd"])) #true
# print(canConstruct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'])) #false
# print(canConstruct('', ['cat','mouse'])) #true
# print(canConstruct('enterapotentpot', ['a','p','ent', 'enter', 'ot', 'o', 't'])) #true
# print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e','ee','eee', 'eeee', 'eeeee', 'eeeeee'])) #false

# def minsum_memo(num, numlist, memo=None):
#     # global calls
#     # calls += 1
#
#     if memo is None:  # memo didnt work for ages bcuz this was // if not memo: // which translates to ...
#         memo = dict()  # ... // if len(memo) == 0 or memo is None // but i only needed the second condition, grrr
#
#     if num in memo:
#         return memo[num]
#     if num < 0:
#         return None
#     if num == 0:
#         return []
#
#     minres = None
#
#     for i in numlist:
#         if i > num:  # reduces calls 496 -> 432 ~ by 15%
#             continue
#
#         res = minsum_memo(num - i, numlist, memo)
#
#         if res is None:
#             continue
#
#         if minres is None or len(res) < len(minres):
#             minres = res + [i]
#
#     memo[num] = minres
#     return minres
#
#
# calls = 0
#
# for case in [(8, [2, 3, 5]),  # true 3 5
#              (7, [5, 3, 4, 7]),  # true 7
#              (63, [1, 5, 10, 21, 25]),  # true 21*3
#              (7, [2, 4]),  # false
#              (8, [1, 4, 5]),  # true 4*2
#              (99, [1, 2, 5, 25, 36]),  # true, 36*2 + 25 + 2
#              (300, [7, 14])  # false, 2^m*n
#              ]:
#     print(minsum_memo(*case))
#     # print("Calls:", calls)
#     # calls = 0

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
# m = 2
# n = 2  # m x n grid ---- 10 exit paths
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
