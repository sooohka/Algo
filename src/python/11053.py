import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    dp = [1 for _ in range(IC)]
    for i in range(1, IC):
            for j in range(i - 1, -1, -1):
                if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    print(dp)
    return max(dp)


print(solution())