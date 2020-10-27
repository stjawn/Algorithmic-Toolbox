# edit distance
import sys

def editDistance(s1, s2):
    M = [[0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]
    for i in range(len(s2) + 1):
        M[i][0] = i
    for j in range(len(s1) + 1):
        M[0][j] = j
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j-1] == s2[i-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1]) + 1
    return M[len(s2)][len(s1)]


if __name__ == "__main__":
    print(editDistance(input(), input()))


# print(editDistance('ab','ab'))
# print(editDistance('short','ports'))
# print(editDistance('editing','distance'))
