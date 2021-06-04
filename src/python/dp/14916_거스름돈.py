import sys

input = sys.stdin.readline


def solution(n):
    dp = [-1] * 100001
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    for i in range(6, n + 1):
        if i % 5 == 0:
            dp[i] = dp[i - 5] + 1
        elif i % 2 == 0:
            dp[i] = dp[i - 2] + 1
        elif (i - 5) % 2 == 0:
            dp[i] = dp[i - 2] + 1
    print(dp[n])


solution(int(input()))
