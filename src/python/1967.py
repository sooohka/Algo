import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = [None for _ in range(IC + 1)] * (IC + 1)
    while True:
        try:
            a, b, c = map(int, sys.stdin.readline().split())
            arr[a][b] = c
        except:
            break
    return IC, arr


def solution():
    IC, arr = getInput()
    print(arr)
    pass


solution()