import sys


def dfs(m, visited, arr, cur):
    if (m) == len(arr):
        print(" ".join(map(str, arr)))
    else:
        for i in range(cur, len(visited)):
            cur = i
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                dfs(m, visited, arr, cur)
                visited[i] = False
                arr.pop()


def solution():
    n, m = map(int, sys.stdin.readline().split())
    visited = [False] * (n + 1)
    cur = 1
    arr = []
    dfs(m, visited, arr, cur)


solution()
