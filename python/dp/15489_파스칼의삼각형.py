import sys

input = sys.stdin.readline


def getInput():
    R, C, W = map(int, input().split())
    return R, C, W


def solution():
    R, C, W = getInput()
    dp = [[0 for _ in range(31)] for _ in range(31)]
    dp[1][1] = 1
    for i in range(2, len(dp)):
        for j in range(1, len(dp[i])):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    count = 0
    s = C
    for i in range(R, R + W):
        s += 1
        for j in range(C, s):
            count += dp[i][j]
    print(count)


solution()
