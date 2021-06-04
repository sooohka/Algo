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


def binarySearch(A, n):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2
        if A[mid] == n:
            return 1
        elif A[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return 0


def solution():
    # N, A, M, B = getInputs()
    N = 5
    A = [4, 1, 5, 2, 3]
    M = 5
    B = [1, 3, 7, 9, 5]
    A = sorted(A)
    for i in B:
        sys.stdout.write(str(binarySearch(A, i))+'\n')


solution()