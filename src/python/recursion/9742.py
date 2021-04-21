import sys


def getInput():
    arr, n = map(str, sys.stdin.readline().strip().split())
    return arr, n


def dfs(arr, visited, ans, temp):
    if len(temp) == len(arr):
        ans.append("".join(map(str, temp)))
    else:
        for i in range(len(arr)):
            if not visited[i]:
                temp.append(arr[i])
                visited[i] = True
                dfs(arr, visited, ans, temp)
                temp.pop()
                visited[i] = False


def solution():
    arr, n = getInput()
    ans = []
    visited = [False] * len(arr)
    temp = []
    dfs(arr, visited, ans, temp)
    print(arr, n, "=", end=" ")
    if int(n) <= len(ans):
        print(ans[int(n) - 1])
    else:
        print("No permutation")
    return


while True:
    try:
        solution()
    except:
        break
