import sys


def getInput():
    return int(sys.stdin.readline())


def solution():
    n = getInput()
    cache = [0 for _ in range(1000001)]
    cache[1] = 1
    cache[2] = 2
    for i in range(3, n + 1):
        cache[i] = (cache[i - 1] + cache[i - 2]) % 15746
    return cache[n]

print(solution())