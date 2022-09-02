from __future__ import print_function


def rec_mc(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_mc(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


def rec_dc(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + rec_dc(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins


def dp_make_change(coin_value_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


if __name__ == '__main__':
    amount = 63
    clist = [1, 5, 10, 21, 25]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print("Making change for", amount, "requires")
    print(dp_make_change(clist, amount, coin_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used, amount)
    print("The used list is as follows:")
    print(coins_used)
