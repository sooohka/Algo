import sys


def getInput():
    IC, k = sys.stdin.readline().split()
    IC = int(IC)
    k = int(k)
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return IC, k, arr


def solution():
    IC, k, arr = getInput()
    dp = [[0] * (k + 1) for _ in range(IC + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            cur = arr[i - 1]
            # if current index's weight + j dose not exceed K
            if j - cur[0] >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur[0]] + cur[1])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[len(dp) - 1][len(dp[0]) - 1]


print(solution())
