import sys
import math


def getInput():
    h, y = map(int, sys.stdin.readline().split())
    return h, y


def solution():
    h, y = getInput()
    dp = [h] * 11
    for i in range(1, y + 1):
        dp[i] = math.floor(dp[i - 1] * 1.05)
        if i > 2 and dp[i] < dp[i - 3] * 1.2:
            dp[i] = math.floor(dp[i - 3] * 1.2)
        if i > 4 and dp[i] < dp[i - 5] * 1.35:
            dp[i] = math.floor(dp[i - 5] * 1.35)
    print(dp[y])


def rec(h, y):
    if y < 0:
        return -1
    if y == 0:
        return h
    return max(
        rec(math.floor(h * 1.05), y - 1),
        rec(math.floor(h * 1.20), y - 3),
        rec(math.floor(h * 1.35), y - 5),
    )


def solution2():
    h, y = getInput()
    print(rec(h, y))


solution2()