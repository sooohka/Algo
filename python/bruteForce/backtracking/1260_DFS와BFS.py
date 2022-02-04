import sys
from collections import deque


def DFS(graph, cur, visited):
    visited[cur] = True
    print(cur, end=" ")
    for i in (graph[cur]):
        if not visited[i]:
            DFS(graph, i, visited)
    return


def BFS(graph, cur, visited):
    queue = deque()
    queue.append(cur)
    visited[cur] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in (graph[cur]):
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return


def getInputs():
    N, IC, start = list(map(int, sys.stdin.readline().split()))
    A = []
    for _ in range(IC):
        A.append(list(map(int, sys.stdin.readline().split())))

    graph = [[] for _ in range(N + 1)]
    for i in A:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    for j in range(len(graph)):
        graph[j]=sorted(graph[j])
    return N, graph, start


def solution():
    N, graph, start = getInputs()
    # graph = [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
    # N = 4
    # start = 1
    visited = [False] * (N + 1)
    DFS(graph, start, visited)
    visited = [False] * (N + 1)
    print()
    BFS(graph, start, visited)


# getInputs()

solution()
