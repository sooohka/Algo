import sys


input = sys.stdin.readline


def solution(n):
    dp = [0] * 91
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    print(dp[n])


solution(int(input()))
