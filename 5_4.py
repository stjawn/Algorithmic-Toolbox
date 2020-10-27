# Longest Common Subsequence
import sys

def LongestCommonSubsequence(A, B):
    m = len(A)
    n = len(B)
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(LongestCommonSubsequence(a, b))

# print(LongestCommonSubsequence([2,7,5],[2,5]))
# print(LongestCommonSubsequence([7],[1,2,3,4]))
# print(LongestCommonSubsequence([2,7,8,3],[5,2,8,7]))
# print(LongestCommonSubsequence([1,2,3,4,5],[0,0,3,4,5]))
