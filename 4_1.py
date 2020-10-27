import math
import sys

def binary_search(A, low, high, key):
    if high < low:
        return -1
    mid = math.floor((low + (high - low)/2))
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binary_search(A,low,mid-1,key)
    else:
        return binary_search(A,mid+1,high,key)


def BinarySearchList(n,a,k,b):
    output = list()
    for i in b:
        output.append(BinarySearch(a,0,n-1,i))
    return output


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, 0, n-1, x), end = ' ')

# print(BinarySearchList(5,[1,5,8,12,13],5,[8,1,23,1,11]))
