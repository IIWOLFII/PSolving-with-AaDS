def DPcoins_tracker(coins,change): # we also count coins now
    dp = [-1] * (change + 1)
    usedcoins = [-1] * (change + 1)

    dp[0] = 0
    lastcoin = 1

    for moneys in range(1,change+1):

        mincoins = float('inf')

        for coin in coins:
            if coin > moneys:
                continue

            curcoin = dp[moneys-coin] + 1

            if curcoin < mincoins:
                mincoins = curcoin
                lastcoin = coin

        dp[moneys] = mincoins
        usedcoins[moneys] = lastcoin

    display_coinhistory(change,usedcoins)

    return dp[change]

def display_coinhistory(change, usedcoins):
    print("Used following coins: ", end="")
    tempcash = change
    while tempcash > 0:
        print(usedcoins[tempcash], end=" ")
        tempcash -= usedcoins[tempcash]
    print('')

# coins = [1,5,10,21,25]
# change = 63

coins = [1,3,4,5]
change = 7

coins = [7,14]
change = 300

dp = DPcoins_tracker(coins,change)

print(f"We get {dp} coins for change of {change}")







# ok since we us DP we can RELIABLY lean back on previous results
# which is why we only need to do teh thing for EVERY coin that is not bigger than change:
# coincomparelist.append: dp[change - COIN] + 1
# why the fuck would that work?
# well what we are doing here is going ok so we need to add one coin ANYWAY hence the 1 *note 1*
# and then we check previous calculations for something like OK change - coin and then we already KNOW how much coins it
# is for the resulting 'change'

# *note 1* but now as im writing it i think, what if we're on 10 and we dont really need to add one coin do we
#
# OH no its ok because it goes (10 - 10) + 1 = 1 means we only use one coin, lets see all other coins:
# (10 - 1) + 1 = 10
# (10 - 5) + 1 = 6
# (10 - 10) + 1 = 1
# (10 - 15) + 1 = OVERFLOW
# we take min of all these
# OK OK OK it all makes sense slowly ,this is great

# def DPcoins(coins,change): # true DP at last - this took me like three days in total if not more, sheesh
#     dp = [-1] * (change + 1)
#     dp[0] = 0
#
#     for moneys in range(1,change+1):
#
#         mincoins = float('inf')
#
#         for coin in coins:
#             if coin > moneys:
#                 continue
#
#             curcoin = dp[moneys-coin] + 1
#             mincoins = min(mincoins, curcoin)   # cant really track coins used because in case of mincoins being 5
#                                                 # the next iteration of coin 10 will still set the coin to the biggest
#                                                 # 10 coin possible
#         dp[moneys] = mincoins
#
#     return dp[change]
#
#
# coins = [1,5,10,21,25]
# change = 63
#
# coinsused = []
#
# dp = DPcoins(coins,change)
#
# print(f"We get {dp} coins for change of {change}")


#  no way this actually works, i had to lie down for 10 minutes to figure this out, thats the sign of a struggle
#  not really a DP though since i still use recursions
#
# calls = 0
#
# def fuck_dp_from_scratch(coins, change): # not really a dp
#     dp = [0]*(change+1)  # we have change amount of positions with values of 0. Since we cant possibly have change of 0
#     # coins, any position will have the minimum amount of coins required for teh change, +1 to account for zero i guess
#
#     dp[0] = 0  # 0 change for no money
#
#     for moneys in range(1, change+1):  # we iterate from 1 to change itself
#
#         # NVM
#         #  if the change not in dp list then: WELL actually it will never be in dp since the numbers are always new
#         # NVM
#
#         min_amountofcoins_for_moneys = getminchange(coins,moneys,dp)
#         print(f"For change of {moneys} we get {min_amountofcoins_for_moneys} coins")
#         #  launch recursive function to find the change for new number, but since we go from 1 to change, it will stop
#         # //// btw EUREKA and leap to DP happened exactly here, keyword - "it will stop one iteration away" ////
#         #  first time it reaches previous known number, and will return that result plus whatever how many
#         #  coins it took to get to it
#
#         dp[moneys] = min_amountofcoins_for_moneys # we add to our dp list the result of ...
#     return dp  # ... how many coins we need for this much money
#
# def getminchange(coins,change,dp):
#     global calls
#     calls += 1
#
#     if change in coins:
#         return 1
#
#     elif dp[change] != 0:
#         return dp[change]
#
#     else:
#         leastnumofcoins = float('inf')  # smallest amount of coins for every possible coin denomination is here
#
#         for coin in coins:
#             if (change - coin) < 0 : #  if coin is bigger than our change then we skip this big coin
#                 continue
#
#             resultofcurrenycoin = 1 + getminchange(coins,change-coin,dp) # what we got from the recursion tree
#
#             #  for change of 7 :: 5 1 1 is more coins than 4 3, we choose the least amount of coins down below
#             leastnumofcoins = min(leastnumofcoins,resultofcurrenycoin)   # aka compare the branches of recursion
#
#         return leastnumofcoins
#
#
#
#
#
# coins = [1,5,10,21,25]
# change = 63
#
# pleasework = fuck_dp_from_scratch(coins, change)
#
# print("Calls:", calls)



# cool nonsense code from the book :)
def make_change_3(coin_value_list, change, min_coins):
    for cents in range(change + 1):  # change + 1 bcuz we start with 0
        coin_count = cents
        for j in [c for c in coin_value_list if c <= cents]:  # this shit makes no fucking sense, calculations out of asshole again wow nice
            if min_coins[cents - j] + 1 < coin_count:  # plus one my ass, there is no recursion depth why the fuck is this here
                coin_count = min_coins[cents - j] + 1  # why the fuck we just stop using the recursive function anyway what is going on holy shit im mad
        min_coins[cents] = coin_count  # how is this even a dp problem if we calculate from 0 all the way to the money input what in the goddamn
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
#             cache[curcash] = count
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
#     #total = 1 # replaced by just 1 - every depth is one coin, we recursively sum them anyway, no need to track
#     print(coins, cash)
#
#     if cash in coins:
#         return 1
#
#
#     min_coins = float('inf') #in order to loop through every coin direction, we need to be able to compare it between the pathways, hence this thing
#     for i in [i for i in coins if i <= cash]:
#         print(i)
#         min_coins = min(min_coins, 1 + count_change_1(coins,cash - i)) #total was used here originally in place of 1
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
