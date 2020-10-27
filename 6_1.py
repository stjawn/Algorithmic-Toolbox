#discreteKnapsackNoRepetitionEqualValue(W,w,v) where v is constant e.g., gold
# replace w[i] with v[i], if w[i] <= j
import sys


def maxGold(W,w):
    dp = [[0 for j in range(len(w))] for i in range(W+1)]
    for i in range(len(w)):
        for j in range(1, W+1):
            dp[j][i] = dp[j][i-1]
            if w[i] <= j:
                val = dp[j-w[i]][i-1] + w[i]
                if dp[j][i] < val:
                    dp[j][i] = val
    return dp[W][len(w)-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(maxGold(W, w))

# print(maxGold(10,[1,4,8]))
