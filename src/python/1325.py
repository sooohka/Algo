import sys
from collections import deque


def getInput():
    N, M = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        arr[b].append(a)
    return N, arr

#recursion limit
def dfs(temp, A, arr, visited):
    for i in A:
        temp.add(i)
    else:
        for i in A:
            if not visited[i]:
                visited[i] = True
                dfs(temp, arr[i], arr, visited)


def bfs(temp, A, arr, visited):
    A = deque(A)
    first = 0
    while A:
        first = A.popleft()
        temp.add(first)
        visited[first] = True
        for i in range(len(arr[first])):
            if not visited[arr[first][i]]:
                A.append(arr[first][i])


def solution():
    N, arr = getInput()
    maxNum = 0
    ans = []
    for i in range(1, N + 1):
        temp = set([i])
        visited = [False] * (N + 1)
        # bfs(temp, arr[i], arr, visited)
        dfs(temp, arr[i], arr, visited)
        if len(temp) > maxNum:
            ans = []
            maxNum = len(temp)
            ans.append(i)
        elif len(temp) == maxNum:
            ans.append(i)
    for i in ans:
        sys.stdout.write(str(i) + " ")


solution()
