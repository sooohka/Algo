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
    print(arr)
    dp = [[0 for _ in range(5001)] for _ in range(5001)]
    dp[2]=1
    dp[4]=2
    dp[6]=5
    # 1. 나를 모두 감싸는 괄호
    # 2. 앞에 (), 뒤에 ()


solution()
