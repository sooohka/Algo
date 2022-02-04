import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return IC, arr


def solution():
    IC, arr = getInput()
    # logic
    cache = [0 for _ in range(101)]
    cache[1] = 1
    cache[2] = 1
    cache[3] = 1
    for i in range(4, 101):
        cache[i] = cache[i - 2] + cache[i - 3]
    for j in range(IC):
        print(cache[arr[j]])


solution()