import sys, math


input = sys.stdin.readline


def solution(n):
    dp = [10000000000] * 50001
    dp[1] = 1  # 1
    dp[2] = 2  # 1 1
    dp[3] = 3  # 1 1 1
    dp[4] = 1  # 2
    dp[5] = 2  # 2 1
    dp[6] = 3  # 2 1 1
    dp[7] = 4  # 2 1 1 1
    dp[8] = 2  # 2 2
    dp[9] = 1  # 3

    dp[25] = 1
    for i in range(2, n + 1):
        if math.sqrt(i).is_integer():
            dp[i] = 1
            continue
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[j * j] + dp[i - (j * j)])
    print(dp[n])


solution(int(input()))
