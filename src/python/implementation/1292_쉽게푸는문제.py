import sys


def solution():
    s, e = map(int, sys.stdin.readline().split())
    arr = [0]
    for i in range(1, e + 1):
        for j in range(i):
            arr.append(i)
    ans = 0
    for i in range(s, e + 1):
        ans += arr[i]
    print(ans)


solution()
