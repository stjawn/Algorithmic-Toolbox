def mpp(input):
    index1 = int()
    index2 = int()
    numList = input
    for i in range(len(numList)):
        if numList[i] >= numList[index1]:
            index1 = i
    greatest = numList[index1]
    del numList[index1]
    for i in range(len(numList)):
        if numList[i] >= numList[index2]:
            index2 = i
    second_greatest = numList[index2]
    return greatest * second_greatest


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(mpp(input_numbers))
