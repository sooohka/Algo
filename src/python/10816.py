# 5
# 4 1 5 2 3 이 배열에
# 5
# 1 3 7 9 5 이 수들이 존재하는지 확인

import sys


def getInputs():
    N = sys.stdin.readline()
    A = list(map(int, sys.stdin.readline().split()))
    M = sys.stdin.readline()
    B = list(map(int, sys.stdin.readline().split()))
    return N, A, M, B


def binaryLowerBound(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            if mid == 0 or arr[mid - 1] != n:
                return mid
        if arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return 0


def binaryUpperBound(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            if (mid == len(arr) - 1) or arr[mid + 1] != n:
                return mid
        if arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return 0


def solution():
    N, A, M, B = getInputs()
    # N = 10
    # A = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
    # M = 8
    # B = [10, 9, -5, 2, 3, 4, 5, -10]
    A = sorted(A)
    strs=''
    for i in B:
        upper = binaryUpperBound(A, i)
        lower = binaryLowerBound(A, i)
        if not upper:
            count = 0
        else:
            count = upper - lower + 1

        strs+=(str(count) + " ")
    sys.stdout.write(strs)

solution()


# TODO:21퍼 시간초과 해결하기
# for in 으로 요소있는지 검사하고 있으면 이진탐색 해보자
