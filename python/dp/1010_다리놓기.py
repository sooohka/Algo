import sys

input = sys.stdin.readline


def getInput():
    IC = int(input())
    arr = []
    for _ in range(IC):
        n, m = map(int, input().split())
        arr.append([n, m])
    return arr


def solution():
    arr = getInput()
    dp = [[0 for _ in range((31))] for _ in range(31)]

    for j in range(31):
        dp[1][j] = j

    for i in range(31):
        dp[i][i] = 1

    for j in range(2, 31):
        for k in range(j + 1, 31):
            dp[j][k] = dp[j - 1][k - 1] + dp[j][k - 1]

    for i in range(len(arr)):
        n = arr[i][0]
        m = arr[i][1]
        print(dp[n][m])


solution()
