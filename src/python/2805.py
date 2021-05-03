import sys


def getInput():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    return n, m, arr


answer = 0


def cutTree(arr, cutter):
    total = 0
    sum(arr)
    for i in range(len(arr)):
        total += arr[i] - cutter if arr[i] - cutter > 0 else 0
    return total

#TODO: 하던거 이어서하기 
def binarySearch(m, arr, start, last):
    global answer
    if start >= last:
        return
    mid = (start + last) // 2
    if cutTree(arr, mid) >= m:
        if mid > answer:
            answer = mid
        binarySearch(m, arr, mid + 1, last)
    else:
        binarySearch(m, arr, start, mid - 1)


def solution():
    global answer
    n, m, arr = getInput()
    binarySearch(m, arr, min(arr), max(arr))
    print(answer)


solution()