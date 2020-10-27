import sys

def mergeSort_inversions(A):
    global inversions
    if len(A) == 1:
        return A
    else:
        m = len(A) // 2
        B = mergeSort_inversions(A[:m])
        C = mergeSort_inversions(A[m:])
        output, count = merge(B,C)
        inversions += count
    # print(inversions)
    return output

def merge(B,C):
    D = list()
    count = 0
    while len(B) > 0 and len(C) > 0:
        if B[0] <= C[0]:
            D.append(B[0])
            del B[0]
        else:
            D.append(C[0])
            del C[0]
            count += len(B)
    D.extend(B)
    D.extend(C)
    return D, count


# print(mergeSort([2,3,9,2,9]))

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#
#
#     return number_of_inversions

inversions = 0
# print(mergeSort_inversions([9,8,7,3,2,1]))
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    mergeSort_inversions(a)
    print(inversions)
