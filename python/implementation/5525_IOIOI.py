import sys


def getInput():
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    return N, M, S


def solution():
    N, M, S = getInput()
    count = 0
    ans = 0
    i = 1
    while i < M - 1:
        if S[i - 1 : i + 2] == "IOI":
            count += 1
            if count == N:
                ans += 1
                count -= 1
            i += 1
        else:
            count = 0
        i += 1
    print(ans)


solution()