import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return IC, arr


def solution():
    IC, arr = getInput()
    # 첫번째 인덱스 비용
    dp = []  # [[0 for _ in range(IC)] for _ in range(IC)]
    for i in range(IC):
        dp.append([0,0,0])
        for j in range(3):
            dp[i][j]=arr[i][j]
    if IC == 1:
        return min(arr[1])
    for i in range(1, IC):
        for j in range(3):
            dp[i][j] = dp[i - 1][(j + 1) % 3] + arr[i][j]
            if dp[i][j] > dp[i - 1][(j + 2) % 3] + arr[i][j]:
                dp[i][j] = dp[i - 1][(j + 2) % 3] + arr[i][j]
    return min(dp[IC - 1])


print(solution())

# 마지막 값에 대한 경우를 생각해보자 (금광문제랑 비슷!)
# 전전값 게산해보자
