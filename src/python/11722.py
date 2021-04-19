import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def lis(N, arr):
    dp = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i, -1, -1):
            if arr[i] < arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp)


def solution():
    IC, arr = getInput()
    print(lis(IC, arr))


solution()
