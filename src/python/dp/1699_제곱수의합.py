import sys, math


input = sys.stdin.readline


def solution(n):
    dp = [sys.maxsize] * 100001
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 1
    for i in range(5, n + 1):
        if math.sqrt(i) == math.floor(math.sqrt(i)):
            dp[i] = 1
        else:
            for j in range(1, math.floor(math.sqrt(i))):
                dp[i] = min(dp[j * j] + dp[i - j * j], dp[i])
    print(dp[n])


solution(int(input()))


