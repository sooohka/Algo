import sys

input = sys.stdin.readline


def getInput():
    n, k = map(int, input().split())
    return n, k


def solution():
    n, k = getInput()
    dp = [[0 for _ in range(31)] for _ in range(31)]
    for i in range(len(dp)):
        for j in range(1, i + 1):
            dp[i][j] = 1
    for i in range(3, n + 1):
        for j in range(2, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    print(dp[n][k])


solution()
import sys

input = sys.stdin.readline


def getInput():
    n, k = map(int, input().split())
    return n, k


def solution():
    n, k = getInput()
    dp = [[0 for _ in range(31)] for _ in range(31)]
    for i in range(len(dp)):
        for j in range(1, i + 1):
            dp[i][j] = 1
    for i in range(3, n + 1):
        for j in range(2, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    print(dp[n][k])


solution()
