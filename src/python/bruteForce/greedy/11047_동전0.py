import sys


def getInput():
    IC, K = map(int, sys.stdin.readline().split())
    arr = []
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return K, arr


def solution():
    K, arr = getInput()
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if K == 0:
            return count
        if K >= arr[i]:
            count += K // arr[i]
            K = K % arr[i]
    return count


sys.stdout.write(str(solution()))
