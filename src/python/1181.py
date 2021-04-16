import sys


def getInput():
    IC = int(sys.stdin.readline())
    A = []
    for _ in range(IC):
        A.append(sys.stdin.readline())
    return IC, A


def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if len(arr[j]) <= len(arr[j - 1]):
                if len(arr[j]) == len(arr[j - 1]):
                    if arr[j] < arr[j - 1]:
                        arr[j - 1], arr[j] = arr[j], arr[j - 1]
                else:
                    arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break


def solution():
    IC, A = getInput()
    A = list(set(A))
    insertionSort(A)
    strs = ""
    for i in A:
        strs += i
    sys.stdout.write(strs)


solution()