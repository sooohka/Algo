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
    dp = [[0] * (k + 1) for _ in range(IC)]
    for i in range(IC):
        # 전 행과 비교해 현재 dp업데이트
        for j in range(dp[i - 1][0], k + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= arr[i][0] and arr[i][1] > dp[i - 1][j]:
                dp[i][j] = arr[i][1]
        # 더한 무게가 k이하인 경우에 전에 있던 가치와 비교후 값 업데이트
        for l in range(k - arr[i][0], 0, -1):
            # 더한 무게
            w = l + arr[i][0]
            if arr[i][1] + dp[i - 1][l] > dp[i][w]:
                dp[i][w] = arr[i][1] + dp[i - 1][l]
    return max(dp[IC - 1])


print(solution())
