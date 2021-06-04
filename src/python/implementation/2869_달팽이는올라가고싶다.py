import sys, math


def getInput():
    a, b, v = map(int, sys.stdin.readline().split())
    return a, b, v


def solution():
    a, b, v = getInput()
    v -= a
    return math.ceil(v / (a - b))+1


print(solution())
