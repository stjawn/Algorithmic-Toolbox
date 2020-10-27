#maximum value by placing parentheses
from math import inf

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def minAndMax(i,j,m,M,op):
    minimum = inf
    maximum = -inf
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        minimum = min(minimum,a,b,c,d)
        maximum = max(maximum,a,b,c,d)
    return(minimum,maximum)


def parentheses(expression):
    d = expression[:len(expression)+1:2]
    d = list(map(int, d))
    op = expression[1:len(expression):2]
    m = [[0 for j in range(len(d)+1)] for i in range(len(d)+1)]
    M = [[0 for j in range(len(d)+1)] for i in range(len(d)+1)]
    for i in range(len(d)):
        m[i][i] = d[i]
        M[i][i] = d[i]
    for s in range(1,len(d)):
        for i in range(len(d)-s):
            j = i + s
            m[i][j],M[i][j] = minAndMax(i,j,m,M,op)
            # print(m[i][j],M[i][j])
    return M[0][len(d)-1]


if __name__ == "__main__":
    print(parentheses(input()))



# print(parentheses('5-8+7*4-8+9'))
