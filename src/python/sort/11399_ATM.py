import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    arr.sort()
    times = [arr[0]]
    for i in range(1, len(arr)):
        times.append(times[i-1] + arr[i])
    print(sum(times))


solution()