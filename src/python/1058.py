import sys


def getInput():
    N = int(sys.stdin.readline())
    arr = [[] for _ in range(N)]
    for i in range(N):
        A = list(sys.stdin.readline().strip())
        for j in range(len(A)):
            if A[j] == "Y":
                arr[i].append(j)
    return N, arr


def dfs(temp, A, arr, visited):
    for i in A:
        temp.add(i)
    for i in range(len(A)):
        if not visited[A[i]]:
            visited[A[i]] = True
            dfs(temp, arr[A[i]], arr, visited)


def solution():
    N, arr = getInput()
    ans = []
    for i in range(N):
        temp = set()
        visited = [False] * N
        dfs(temp, arr[i], arr, visited)
        ans.append(temp)
    if N == 1:
        sys.stdout.write("0")
    else:
        sys.stdout.write(str(len(max(ans)) - 1))


solution()
