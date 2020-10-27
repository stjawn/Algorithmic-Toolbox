import sys

def lastDigit(n):
    f = 0
    x = 0
    y = 1
    if n < 0:
        return 'Fibonacci undefined for negative input'
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n+1):
            f = ((x % 10) + (y % 10)) % 10
            x = y
            y = f
    return f

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(lastDigit(n))
