import sys


def rec(n, m, arr, cur):
    if len(arr) == m:
        print(" ".join(map(str, arr)))
    else:
        for i in range(cur, n + 1):
            cur = i
            arr.append(i)
            rec(n, m, arr, cur)
            arr.pop()


def solution():
    n, m = map(int, sys.stdin.readline().split())
    arr = []
    cur = 1
    rec(n, m, arr, cur)


solution()
