

def fibonacci(n):
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
            f = x + y
            x = y
            y = f
        return f

n = int(input())

print(fibonacci(n))
