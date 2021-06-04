import sys

input = sys.stdin.readline


def getInput():
    IC = int(input())
    arr = []
    for _ in range(IC):
        arr.append(int(input()))
    return arr


def solution():
    arr = getInput()
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    dp[4] = 7
    for i in range(5, 12):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] 
    for i in range(len(arr)):
        print(dp[arr[i]])


solution()
