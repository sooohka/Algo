import sys


def dfs(n, length, arr, temp, ans):
    # 종료조건
    if len(temp) == length:
        temp = int("".join(map(str, temp)))
        if temp <= n:
            ans.append(temp)
        # 로직
    else:
        for j in range(len(arr)):
            temp.append(arr[j])
            dfs(n, length, arr, temp, ans)
            temp.pop()


def getInput():
    n, k = map(int, sys.stdin.readline().split())
    length = len(str(n))
    arr = list(map(int, sys.stdin.readline().split()))
    return n, length, k, arr


def solution():
    n, length, k, arr = getInput()
    temp = []
    ans = []
    dfs(n, length, arr, temp, ans)
    dfs(n, length - 1, arr, temp, ans)
    print(max(ans))


solution()