import sys

def maxPrizes(n):
    prizes = list()
    p = 1
    while n > 0:
        if n >= (2*p + 1):
            prizes.append(p)
            n -= p
            p += 1
        else:
            prizes.append(n)
            n = 0
    return prizes


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = maxPrizes(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

# print(maxPrizes(6))
# print(maxPrizes(8))
# print(maxPrizes(2))
