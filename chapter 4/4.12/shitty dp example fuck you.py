def make_change_4(coin_value_list, change, min_coins, coins_used):  # cool nonsense code from the book :)
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            print(f'cents: {cents}, j: {j} new_coin: {new_coin}')
            print(f'coin count = min_coins[cents - j] + 1 = min_coins[{cents - j}] + 1 = {min_coins[cents-j]} + 1')
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1  # this shit makes no fucking sense, calculations out of asshole again wow nice
                new_coin = j
        min_coins[cents] = coin_count  # why the fuck we just stop using the recursive function anyway what is going on holy shit im mad
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):  # what the fuck is this
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin, end=" ")
        coin = coin - this_coin
    print()


def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amnt + 1)
    coin_count = [0] * (amnt + 1)
    # i was so upset i didnt realise that it broke apart cuz of IDE so it wont exceed the styleguide lol
    print("Making change for {} requires the following {} coins: ".format( amnt, make_change_4(clist, amnt, coin_count, coins_used)),end="",)
    print_coins(coins_used, amnt)
    print("The used list is as follows:")
    print(coins_used)


main()
