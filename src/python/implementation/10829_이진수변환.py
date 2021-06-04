import sys


def rec(n, arr):
    if n == 1:
        arr.append(1)
        return arr
    arr.append(n%2)
    return rec(n // 2, arr)


def solution(n):
    arr = []
    rec(n,arr)
    arr.reverse()
    return "".join(map(str,arr))

print(solution(int(sys.stdin.readline())))