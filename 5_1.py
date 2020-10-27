# Dynamic programming money change
import sys

def moneyChange(money):
    coins = [1,3,4]
    min_num_coins = [0]
    for m in range(1,money+1):
        min_num_coins.append(100000)
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(moneyChange(m))


# print(moneyChange(2))
# print(moneyChange(34))
