import sys

count = 0


def getInput():
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    arr = []
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    return k, arr


def dfs(k, new, visited, arr, ans):
    global count
    if len(new) == k:
        ans.append("".join(map(str, new)))
        count += 1

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            new.append(arr[i])
            dfs(k, new, visited, arr, ans)
            visited[i] = False
            new.pop()


def solution():
    k, arr = getInput()
    new = []
    ans = []
    visited = [False] * len(arr)
    dfs(k, new, visited, arr, ans)
    sys.stdout.write(str(len(set(ans))))


solution()
