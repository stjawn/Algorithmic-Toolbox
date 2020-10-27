import sys

def maxRevenue(a,b):
    s = 0
    a.sort(reverse = True)
    b.sort(reverse = True)
    for i in range(len(a)):
        p = a[i] * b[i]
        s += p
    return s



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(maxRevenue(a, b))

# print(maxRevenue(1,[23],[39]))
# print(maxRevenue(3,[1,3,-5],[-2,4,1]))
