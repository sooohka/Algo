import sys


def getInput():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return n, arr


def get(arr):
    dp = [1 for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] > arr[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    return dp


def solution():
    # n, arr = 6, [10, 20, 10, 30, 20, 50]
    # n, arr = 10, [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
    n, arr = getInput()
    increment = get(arr)
    decrement = get(list(reversed(arr)))
    bitonic = map(lambda a, b: a + b, increment, list(reversed(decrement)))
    print(max(bitonic) - 1)


solution()
