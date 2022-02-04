import sys


def solution(n):
    dp = [-1] * (5000 + 1)
    dp[3] = 1
    dp[5] = 1
    for i in range(6, n + 1):
        if not dp[i - 3] == -1:
            dp[i] = dp[i - 3] + 1
        if not dp[i - 5] == -1:
            if not dp[i] == -1:
                dp[i] = dp[i - 5] + 1 if dp[i - 5] + 1 < dp[i] else dp[i]
            else:
                dp[i] = dp[i - 5] + 1
    print(dp[n])


solution(int(sys.stdin.readline()))