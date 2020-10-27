import sys

def LongestCommonSubsequence(A, B, C):
    m = len(A)
    n = len(B)
    o = len(C)
    dp = [[[0 for i in range(o+1)] for j in range(n+1)] for k in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, o+1):
                if A[i-1] == B[j-1] == C[k-1]:
                    dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                else:
                    dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
    return dp[m][n][o]



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(LongestCommonSubsequence(a, b, c))


# print(LongestCommonSubsequence([1,2,3],[2,1,3],[1,3,5]))
# print(LongestCommonSubsequence([8,3,2,1,7],[8,2,1,3,8,10,7],[6,8,3,1,4,7]))
