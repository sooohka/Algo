import sys


def getInput():
    # IC = 5
    # A = [[3, 4], [1, 1], [1, -1], [2, 2], [3, 3]]
    IC = int(sys.stdin.readline())
    A = []
    for _ in range(IC):
        A.append(list(map(int, sys.stdin.readline().split())))

    return IC, A


def quickSort(A, start, end, index):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and A[left][index] <= A[pivot][index]:
            left += 1
        while right >= start + 1 and A[right][index] >= A[pivot][index]:
            right -= 1
        if left > right:
            A[right], A[pivot] = A[pivot], A[right]
            break
        else:
            A[right], A[left] = A[left], A[right]
    quickSort(A, start, right - 1, index)
    quickSort(A, right + 1, end, index)


def solution():
    IC, A = getInput()
    quickSort(A, 0, len(A) - 1, 1)
    for i in range(len(A) - 1):
        if A[i][1] == A[i + 1][1]:
            arr = [A[i]]
            ii = i
            while i < len(A) - 1 and A[i][1] == A[i + 1][1]:
                i += 1
                arr.append(A[i])
            quickSort(arr, 0, len(arr) - 1, 0)
            for j in range(len(arr)):
                A[ii + j] = arr[j]
    for i in A:
        print(i[0],i[1])

solution()