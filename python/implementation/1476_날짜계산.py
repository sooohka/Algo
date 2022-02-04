import sys


def solution():
    E, S, M = map(int, sys.stdin.readline().split())
    e, s, m = 1, 1, 1
    count = 1
    while True:
        if e == E and s == S and m == M:
            return count
        e += 1
        s += 1
        m += 1
        if not e <= 15:
            e = 1
        if not s <= 28:
            s = 1
        if not m <= 19:
            m = 1
        count += 1


print(solution())