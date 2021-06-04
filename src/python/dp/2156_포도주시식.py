import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = [0]
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return IC, arr


# 연속 세잔 못마심
def solution():
    IC, arr = getInput()
    dp = [0 for _ in range(IC + 1)]
    dp[1] = arr[1]
    for i in range(2, IC + 1):
        # 바로 전잔마시는 경우에는 전전잔은 마시면안됨
        if dp[i] < arr[i - 1] + dp[i - 3] + arr[i]:
            dp[i] = arr[i - 1] + dp[i - 3] + arr[i]
        # 바로 전전잔마시는 경우
        if dp[i] < dp[i - 2] + arr[i]:
            dp[i] = dp[i - 2] + arr[i]
        # 두번 안먹을 수도있는 경우가 존재
        if dp[i] < dp[i - 1]:
            dp[i] = dp[i - 1]
    return max(dp)


print(solution())