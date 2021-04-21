import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(sys.stdin.readline())
    return IC, arr


def solution():
    IC, arr = getInput()
    count = 0
    for str in arr:
        temp = []
        FLAG = False
        for i in range(1, len(str)):
            if FLAG:
                break
            while str[i] == str[i - 1]:
                i += 1
            for j in temp:
                if j == str[i]:
                    count -= 1
                    FLAG = True
                    break
            temp.append(str[i - 1])
        count += 1
    print(count)


solution()
