import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def lis(arr, rev):
    if not arr:
        print("not array")
        return 0
    dp = [1 for _ in range(len(arr))]
    # 증가

    if rev:
        for i in range(1, len(arr)):
            for j in range(i, -1, -1):
                if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    # 감소
    else:
        for i in range(1, len(arr)):
            for j in range(i, -1, -1):
                if arr[i] < arr[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
    return max(dp)


def solution():
    IC, arr = getInput()
    res = 0
    for n in range(IC):
        maxNum = lis(arr[0 : n + 1], True) + lis(arr[n:], False)
        res = maxNum if maxNum > res else res
    return res - 1


print(solution())
# testCases = [
#     (17, [7, 2, 1, 1, 5, 2, 2, 3, 2, 3, 1, 2, 4, 5, 1, 2, 4], 6),
#     (10, [1, 5, 2, 1, 4, 3, 4, 5, 2, 1], 7),
#     (5, [1, 2, 3, 2, 1], 5),
#     (6, [1, 2, 3, 5, 5, 1], 5),
#     (5, [1, 2, 1, 1, 1], 3),
#     (2, [999, 1000], 2),
#     (6, [1, 2, 3, 3, 2, 1], 5),
#     (5, [1, 3, 1, 2, 1], 4),
#     (5, [1, 5, 4, 2, 3], 4),
#     (7, [5, 1, 6, 2, 6, 2, 1], 5),
#     (9, [5, 1, 6, 2, 7, 3, 7, 2, 1], 6),
#     (4, [1, 2, 2, 1], 3),
#     (6, [1, 2, 3, 2, 1, 4], 5),
#     (2, [1, 1], 1),
#     (4, [1, 1, 2, 1], 3),
#     (5, [5, 4, 3, 2, 3], 4),
#     (7, [9, 1, 2, 3, 2, 1, 9], 5),
#     (10, [10, 1, 3, 5, 7, 6, 3, 2, 1, 10], 8),
# ]

# for i in testCases:
#     temp = solution(i[0], i[1])
#     if i[2] != temp:
#         print(i, "false", temp)
