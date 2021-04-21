import sys


def dfs(m, arr, visited):
    # 출력
    if len(arr) == m:
        sys.stdout.write(" ".join(map(str, arr)) + "\n")
    else:
        for i in range(1, len(visited)):
            if not visited[i]:
                visited[i] = True
                arr.append(i)
                dfs(m, arr, visited)
                visited[i] = False
                arr.pop()


def solution():
    N, M = map(int, sys.stdin.readline().split())
    visited = [False] * (N + 1)
    arr = []
    dfs(M, arr, visited)


solution()