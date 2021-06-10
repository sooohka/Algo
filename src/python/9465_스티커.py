import sys

input = sys.stdin.readline


def getInput():
    IC = int(input())
    arr = []
    for _ in range(IC):
        temp = []
        input()
        temp.append(list(map(int, input().split())))
        temp.append(list(map(int, input().split())))
        arr.append(temp)
    return arr


def solution():
    arr = getInput()
    for test in arr:
        dp = [[0 for _ in range(len(test[0]) + 1)] for _ in range(2)]
        dp[0][1] = test[0][0]
        dp[1][1] = test[1][0]
        dp[0][2] = dp[1][1] + test[0][2]
        dp[1][2] = dp[0][1] + test[1][2]
        for i in range(2, len(test[0]) + 1):
            # 조건 때면 u[i][j+1] || u[i][j-1] ||u[i+1][j] ||u[i-1][j]
            # 윗줄
            dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + test[0][i - 1]
            # 아랫줄
            dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + test[1][i - 1]
        print(max(dp[0][-1], dp[1][-1]))


solution()
