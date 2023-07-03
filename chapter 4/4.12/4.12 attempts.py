def count_change_dp(coins, cash, cache=None):  # recursive non greedy, caching, 244 calls (206 without coin 21)
    if not cache:
        cache = [0] * coins + 1

    print(coins, cash, cache)

    for dp in range(cash + 1):  # add + 1 bcuz we start with 0
        if dp in cache:
            pass  # todo what the fuck do we do lol? why would it be there if we iterate 1 to fuck you this makes no sense


    if cash in coins: # todo i give up make this garbage fire work later once you find proper literature instead of this shit book
        return 1
    elif cash in cache:
        min_coins = cache[cash]
    else:
        min_coins = float(
            'inf')  # in order to loop through every coin direction, we need to be able to compare it between the pathways, hence this thing

        for i in [i for i in coins if i <= cash]:
            print(i)
            min_coins = min(min_coins, 1 + count_change_dp(coins, cash - i))
            cache[cash] = min_coins
    return min_coins


print(count_change_dp([1, 5, 10, 21, 25], 63))


# cool nonsense code from the book :)
def make_change_3(coin_value_list, change, min_coins):
    for cents in range(change + 1):  # change + 1 bcuz we start with 0
        coin_count = cents
        for j in [c for c in coin_value_list if
                  c <= cents]:  # this shit makes no fucking sense, calculations out of asshole again wow nice
            if min_coins[
                cents - j] + 1 < coin_count:  # plus one my ass, there is no recursion depth why the fuck is this here
                coin_count = min_coins[
                                 cents - j] + 1  # why the fuck we just stop using the recursive function anyway what is going on holy shit im mad
        min_coins[
            cents] = coin_count  # how is this even a dp problem if we calculate from 0 all the way to the money input what in the goddamn
    return min_coins[change]

# # FAIL
# def count_change_3(coins, cash):  # dynamic programming # i dont fucking get it again fuck off bro this makes no sense
#
#     cache = [0] * (cash + 1)
#     curcash = 1
#     while curcash != cash + 1:
#         print(coins, f'{curcash} out of {cash}', cache)
#         tempcash = curcash
#         min_coins = float('inf')
#
#         if cache[curcash] > 0:
#             pass
#         else:
#             count = 0
#             while tempcash > 0:
#                 for i in [i for i in coins if i <= curcash]:
#                     maxcoin = i
#                     tempcash -= maxcoin
#                     count += 1
#
#             cache[curcash] = count  # todo wtf is going on how do i calculate this what am i calculating
#
#         curcash += 1
#     return cache[cash]
#
#
# print(count_change_3([1, 5, 10, 21, 25], 63))

# def count_change_2(coins, cash, cache = dict()): # recursive non greedy, caching, 244 calls (206 without coin 21)
#     global calls
#     calls += 1
#     #total = 1 replaced by just 1 - every depth is one coin
#     print(coins, cash, cache)
#
#     if cash in coins:
#         return 1
#     elif cash in cache:
#         min_coins = cache[cash]
#     else:
#         min_coins = float('inf') #in order to loop through every coin direction, we need to be able to compare it between the pathways, hence this thing
#
#         for i in [i for i in coins if i <= cash]:
#             print(i)
#             min_coins = min(min_coins, 1 + count_change_2(coins,cash - i))
#             cache[cash] = min_coins
#
#     return min_coins
#
# print(count_change_2([1,5,10,21,25],63))
# print('calls:', calls)

# def count_change_1(coins, cash): # ok i get it now - recursive non greedy, slow
#     #total = 1 replaced by just 1 - every depth is one coin
#     print(coins, cash)
#
#     if cash in coins:
#         return 1
#
#
#     min_coins = float('inf') #in order to loop through every coin direction, we need to be able to compare it between the pathways, hence this thing
#     for i in [i for i in coins if i <= cash]:
#         print(i)
#         min_coins = min(min_coins, 1 + count_change_1(coins,cash - i))
#     return min_coins
#
# print(count_change_1([1,5,21,25],41))

# def count_change(coins, cash, changelist = []): #greedy but recurisve
#     #print(coins,cash,changelist)
#     if cash <= 0:
#         return changelist
#     for i in coins:
#         if i <= cash:
#             changelist.append(i)
#             return count_change(coins,cash - i,changelist)
#
# coins = [1,5,10,21,25]
# coins.reverse()
# print(count_change(coins,63))

# def count_change(coins, cash): #non recursive greedy
#     change = []
#     while cash > 0:
#         for i in coins:
#             while i <= cash:
#                 change.append(i)
#                 cash -= i
#     return change
#
# coins = [1,5,10,21,25]
# coins.reverse()
# print(count_change(coins,63))
