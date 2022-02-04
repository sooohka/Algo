import sys

input = sys.stdin.readline


def getInput():
    IC = int(input())
    # dont use 0 index
    arr = [0] * 501
    for _ in range(IC):
        a, b = map(int, input().split())
        arr[a] = b
    return arr, IC


def solution():
    arr, IC = getInput()
    # dont use 0 index
    dp = [0] * 501
    maxN = 0
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
                maxN = dp[i] if dp[i] > maxN else maxN
    print(IC - maxN)


solution()
