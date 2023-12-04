def minsum_dp(goal,coins):
    dp = [None for i in range(goal+1)]
    dp[0] = list()

    for i in range(len(dp)):
        if dp[i] is None:
            continue
        for coin in coins:
            nextpos = i + coin
            if nextpos > len(dp)-1:
                continue
            if not dp[nextpos] or len(dp[nextpos]) > len(dp[i])+1:
                dp[nextpos] = dp[i] + [coin]

    return dp[goal]


def minsum_memo(goal,coins,memo = None):
    if memo is None:
        memo = dict()

    if goal in memo:
        return memo[goal]

    if goal == 0:
        return []

    if goal < 0:
        return False

    minres = float('+inf')
    bestattempt = False

    for coin in coins:
        res = minsum_memo(goal-coin,coins, memo)
        if isinstance(res,list):
            if minres > len(res)+1:
                bestattempt = res + [coin]
                minres = len(bestattempt)

    memo[goal] = bestattempt
    return bestattempt

caselist = [(8, [2, 3, 5]),  # true 3 5
             (7, [5, 3, 4, 7]),  # true 7
             (7, [2, 4]),  # false
             (8, [1, 4, 5]),  # true 4*2
             (63, [1, 5, 10, 21, 25]),  # true 21*3
             (99, [1, 2, 5, 25, 36]),  # true, 36*2 + 25 + 2
             (300, [7, 14])  # false, 2^m*n
             ]

for case in caselist:
    print(minsum_dp(*case))