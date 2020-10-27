import sys

def gcd(a, b):
    if a > b:
        if b == 0:
            return a
        else:
            c = a % b
            return gcd(b, c)
    else:
        if a == 0:
            return b
        else:
            c = b % a
            return gcd(a, c)

def lcm(a, b):
    return int((a * b) / gcd(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
