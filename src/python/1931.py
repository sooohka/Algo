import sys

maximum = 1


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return IC, arr


def solution():
    global maximum
    IC, arr = getInput()
    arr.sort(key=lambda K: (K[1], K[0]))
    et = arr[0][1]
    for i in range(1, len(arr)):
        if arr[i][0] >= et:
            maximum += 1
            et = arr[i][1]
    sys.stdout.write(str(maximum))


solution()
