import sys

def moneyChange(m):
    p = 1
    n = 5
    d = 10
    coins = 0
    if m >= d:
        coins += (m//d)
        m -= d * (m//d)
        coins += (m//n)
        m -= n * (m//n)
        coins += (m/p)
        return int(coins)
    elif m >= n:
        coins += (m//n)
        m -= n * (m//n)
        coins += (m/p)
        return int(coins)
    else:
        coins += (m/p)
        return int(coins)

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(moneyChange(m))
