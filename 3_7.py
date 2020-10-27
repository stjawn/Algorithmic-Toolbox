import sys

def maxInt(a):
    int_output = list()
    while len(a) > 0:
        safe_int = int()
        for i in a:
            if isSafeInt(i,safe_int) == True:
                safe_int = i
        int_output.append(safe_int)
        a.remove(safe_int)
    str_output = map(str,int_output)
    output = str()
    for i in str_output:
        output += i
    return int(output)


def isSafeInt(a,b):
    if int(str(a)+str(b)) >= int(str(b)+str(a)):
        return True


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(maxInt(a))


# print(maxInt([21,2]))
# print(maxInt([9,4,6,1,9]))
# print(maxInt([23,39,92]))
