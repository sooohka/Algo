import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return IC, arr


# 자기랑 같은거 +1
def solution():
    IC, arr = getInput()
    # copy from arr
    dp = [[0 for _ in range(IC)] for _ in range(IC)]
    dp[0] = [arr[0][0]]
    # logic
    # 열의 길이+1까지
    for i in range(0, IC - 1):
        # 행의 길이 까지
        for j in range(len(arr[i + 1])):
            if j < len(arr[i + 1]) - 1 and dp[i + 1][j] < dp[i][j] + arr[i + 1][j]:
                dp[i + 1][j] = dp[i][j] + arr[i + 1][j]
            if j - 1 >= 0 and dp[i + 1][j] < dp[i][j - 1] + arr[i + 1][j]:
                dp[i + 1][j] = dp[i][j - 1] + arr[i + 1][j]
    print(max(dp[IC - 1]))


solution()