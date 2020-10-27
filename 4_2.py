import sys

def majorityElementNaive(n,A):
    for i in range(n):
        current_element = A[i]
        count = 0
        for j in range(n):
            if A[j] == current_element:
                count += 1
        if count > n/2:
            return A[i]
    return 'no majority element'

def mergeSort(A):
    if len(A) == 1:
        return A
    else:
        m = len(A) // 2
        B = mergeSort(A[:m])
        C = mergeSort(A[m:])
        output = merge(B,C)
    return output

def merge(B,C):
    D = list()
    while len(B) > 0 and len(C) > 0:
        if B[0] <= C[0]:
            D.append(B[0])
            del B[0]
        else:
            D.append(C[0])
            del C[0]
    D.extend(B)
    D.extend(C)
    return D

def majorityElementNLogN(A):
    sorted = mergeSort(A)
    count = 1
    for i in range(1,len(sorted)):
        if sorted[i] == sorted[i-1]:
            count += 1
            if count > len(sorted)//2:
                return 1
        else:
            count = 1
    return -1

# print(majorityElementNLogN([2,3,9,2,2]))
# print(majorityElementNLogN([1,2,3,4]))
# print(majorityElementNLogN([1,2,3,1]))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if majorityElementNLogN(a) != -1:
        print(1)
    else:
        print(0)
