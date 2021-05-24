import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = {}
    for _ in range(IC - 1):
        a, b = map(int, sys.stdin.readline().split())
        try:
            arr[a].append(b)
        except:
            arr[a] = [b]
    return arr


def solution():
    pass


solution()
