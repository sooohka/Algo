# 정렬하는데 자기 좌표보다 작은 좌표 수만큼 배열 업데이트

import sys


def quickSort(arr, start, end):
    if start >= end:
        return arr
    pivot = start
    left = pivot + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right >= start + 1 and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
            break
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)

    return


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    copied = list((set(arr)))
    quickSort(copied, 0, len(copied) - 1)
    dic = {copied[i]: i for i in range(len(copied))}
    for i in arr:
        sys.stdout.write(str(dic[i]) + " ")
    return


solution()
