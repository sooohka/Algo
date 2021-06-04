import sys

input = sys.stdin.readline


def getInput():
    H, W = map(int, input().split())
    arr = []
    for _ in range(H):
        arr.append(list(input().strip()))
    return arr, H, W


def solution():
    arr, H, W = getInput()
    dp = [[-1 for _ in range(W)] for _ in range(H)]
    for i in range(len(arr)):
        dp.append([])
        for j in range(len(arr[i])):
            if arr[i][j] == "c":
                dp[i][j] = 0
    for i in range(len(dp)):
        for j in range(1, len(dp[i])):
            if dp[i][j] == 0 or dp[i][j - 1] == -1:
                continue
            dp[i][j] = dp[i][j - 1] + 1 if dp[i][j - 1] + 1 > dp[i][j] else dp[i][j]
    printer(dp)


def printer(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()


solution()
