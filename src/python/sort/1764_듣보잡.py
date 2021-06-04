import sys


def getInput():
    N, M = map(int, sys.stdin.readline().split())
    d = []
    b = []
    for _ in range(N):
        d.append(sys.stdin.readline().strip())
    for _ in range(M):
        b.append(sys.stdin.readline().strip())

    return sorted(b), sorted(d)


def solution():
    d, b = getInput()
    ans = []
    j = 0
    for i in d:
        if j >= len(b):
            break
        while j < len(b) and b[j] <= i:
            if b[j] == i:
                ans.append(i)
            j += 1
    print(len(ans))
    for i in ans:
        sys.stdout.write(i + "\n")


solution()
