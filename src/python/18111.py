import sys


def getInput():
    n, m, item = map(int, sys.stdin.readline().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return item, arr


def solution():
    item, arr = getInput()
    

solution()