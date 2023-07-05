def DPcoins_tracker(coins,change):
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

coins = [1,5,8,10,25]
change = 33


dp = DPcoins_tracker(coins,change)

print(f"We get {dp} coins for change of {change}")