import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    dp = [1 for _ in range(IC)]
    if len(dp) == 1:
        return 0
    for i in range(1, IC):
        for j in range(i, -1, -1):
            if arr[j] > arr[i]:
                dp[i] = dp[j] + 1 if dp[j] + 1 > dp[i] else dp[i]
    return IC - max(dp)


print(solution())
