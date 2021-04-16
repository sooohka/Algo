import sys


def getInput():
    IC = int(sys.stdin.readline())
    A = []
    for i in range(IC):
        a, b = sys.stdin.readline().split()
        A.append((int(a), b, i))

    return IC, A


def quickSort(arr, start, end, index):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left][index] <= arr[pivot][index]:
            left += 1
        while right >= start + 1 and arr[right][index] >= arr[pivot][index]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quickSort(arr, start, right - 1, index)
    quickSort(arr, right + 1, end, index)


def solution():
    IC, A = getInput()
    quickSort(A, 0, len(A) - 1, 0)
    strs = ""
    for i in range(len(A) - 1):
        if A[i][0] == A[i + 1][0]:
            temp = i
            arr = [A[i]]
            while i < len(A) - 1 and A[i][0] == A[i + 1][0]:
                i += 1
                arr.append(A[i])
            quickSort(arr, 0, len(arr) - 1, 2)
            for k in range(len(arr)):
                A[temp + k] = arr[k]
    for l in A:
        strs += str(l[0]) + " " + l[1] + "\n"
    sys.stdout.write(strs)


# def solution():
#     IC, A = getInput()
#     insertSort(A)
#     strs = ""
#     for l in A:
#         strs += str(l[0]) + " " + l[1] + "\n"
#     sys.stdout.write(strs)


# def insertSort(arr):
#     for i in range(len(arr)):
#         for j in range(i, 0, -1):
#             if arr[j][0] < arr[j - 1][0]:
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             else:
#                 break


solution()