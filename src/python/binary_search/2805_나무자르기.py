import sys
import math

def getInput():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    return n, m, sorted(arr)


answer = 0


def cutTree(arr, cutter):
    total = 0
    for i in arr:
        if i - cutter > 0:
            total += i - cutter
    return total


def binarySearch(m, arr, start, last):
    global answer
    if start > last:
        return
    mid = (start + last) // 2
    if cutTree(arr, mid) >= m:
        if answer < mid:
            answer = mid
        binarySearch(m, arr, mid + 1, last)
    else:
        binarySearch(m, arr, start, mid - 1)


def solution():
    global answer
    n, m, arr = getInput()
    binarySearch(m, arr, 0, max(arr))
    print(answer)


solution()