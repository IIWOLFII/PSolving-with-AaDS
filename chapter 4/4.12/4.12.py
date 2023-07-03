# def make_change(coins,sum):
#     if sum <= 0:
#         return
#     for coin in coins:
#         if coin == sum:
#             print(f'dispensed coin {coin}')
#             return coin
# i dont fucking get it


def make_change_1(coin_denoms, change):
    if change in coin_denoms: ##???????what the fuck are you returning this for if this doesnt even get summed
        return 1 #what the fuck is going on i hate looking at this // 1 is minimum coin denom i-
    min_coins = float("inf") # guess we dont refer to the actual min coin from coin list because fuck yourself lol lmao // this is amount of coin if its in there the we shit out a coin nvm

    # lessercoins = [] #[c for c in coin_denoms if c <= change]
    # for i in coin_denoms:
    #     if i <= change:
    #         lessercoins.append(i)

    for i in [c for c in coin_denoms if c <= change]:
        num_coins = 1 + make_change_1(coin_denoms, change - i) #pulled this straight out of your asshole with no explanation, nice book retard
        min_coins = min(num_coins, min_coins) #its min because we aim for LEAST amount of coins

    print(min_coins)
    return min_coins
# what the fuck am i looking at why would any of this work

print(make_change_1([1, 5, 10, 25], 6))
