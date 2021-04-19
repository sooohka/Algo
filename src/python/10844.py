import sys


def solution():
    n = int(sys.stdin.readline())
    # 0번쨰 인덱스 사용안함, 1번째 인덱스 초기화
    dp = [False, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    # dp 0으로 초기화
    for i in range(2, n + 1):
        dp.append([0 for _ in range(10)])
    for i in range(2, n + 1):
        # j인덱스는 마지막 자리수를 의미한다.
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i - 1][1]
                continue
            if j == 9:
                dp[i][9] = dp[i - 1][8]
                continue
            dp[i][j] = dp[i - 1][j + 1] + dp[i - 1][j - 1]
    return sum(dp[n]) % 1000000000


print(solution())

# dp테이블을 자릿수로 나눠서 계산해보자
