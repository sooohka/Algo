import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    dp = [0 for _ in range(IC)]
    dp[0] = arr[0]
    for i in range(1, IC):
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
    return max(dp)


# 음수인 값을 더해도 그 값이 0보다 크다면 안고 가도 되는값
# 결국엔 최종으로 dp테이블의 max값을 출력하면 되기때문
print(solution())
