#improving quick sort

import sys
import random

def partition3(a, l, r):
    x = a[l]
    k = l
    for i in range(l+1,r+1):
        if a[i] <= x:
            k += 1
            a[i], a[k] = a[k], a[i]
    a[l], a[k] = a[k], a[l]
    j = l
    # print(a)
    for i in range(l, k):
        if a[i] < a[k]:
            a[i], a[j] = a[j], a[i]
            j += 1
    return j, k

# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j
#
# def randomized_quick_sort2(a, l, r):
#     if l >= r:
#         return a
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     #use partition3
#     m = partition2(a, l, r)
#     randomized_quick_sort2(a, l, m - 1);
#     randomized_quick_sort2(a, m + 1, r);

def randomized_quick_sort(a, l, r):
    if l >= r:
        # print(a)
        return
    q = random.randint(l, r)
    a[l], a[q] = a[q], a[l]
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m);
    randomized_quick_sort(a, n+1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    z, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, z - 1)
    for x in a:
        print(x, end=' ')


# print(randomized_quick_sort([2,3,9,2,2],0,4))
# print(randomized_quick_sort([1,2,3,4,5,6,7,8,9,10],0,9))
# print('----------')
# print(randomized_quick_sort([10,9,8,7,6,5,4,3,2,1],0,9))
