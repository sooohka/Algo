import sys


def w(cache, a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if not cache[20][20][20]:
            cache[20][20][20] = w(cache, 20, 20, 20)
        return w(cache, 20, 20, 20)
    if a < b and b < c:
        if not cache[a][b][c - 1]:
            cache[a][b][c - 1] = w(cache, a, b, c - 1)
        if not cache[a][b - 1][c - 1]:
            cache[a][b - 1][c - 1] = w(cache, a, b - 1, c - 1)
        if not cache[a][b - 1][c]:
            cache[a][b - 1][c] = w(cache, a, b - 1, c)
        return cache[a][b][c - 1] + cache[a][b - 1][c - 1] - cache[a][b - 1][c]
    else:
        if not cache[a - 1][b][c]:
            cache[a - 1][b][c] = w(cache, a - 1, b, c)
        if not cache[a - 1][b - 1][c]:
            cache[a - 1][b - 1][c] = w(cache, a - 1, b - 1, c)
        if not cache[a - 1][b][c - 1]:
            cache[a - 1][b][c - 1] = w(cache, a - 1, b, c - 1)
        if not cache[a - 1][b - 1][c - 1]:
            cache[a - 1][b - 1][c - 1] = w(cache, a - 1, b - 1, c - 1)
        return (
            cache[a - 1][b][c]
            + cache[a - 1][b - 1][c]
            + cache[a - 1][b][c - 1]
            - cache[a - 1][b - 1][c - 1]
        )


def solution():
    cache = [[[0 for _ in range(50)] for _ in range(50)] for _ in range(50)]
    print(cache)
    while 1:
        a, b, c = list(map(int, sys.stdin.readline().split()))
        if a == -1 and b == -1 and c == -1:
            break
        ans = w(cache, a, b, c)
        print("w(%d, %d, %d) = %d" % (a, b, c, ans))


solution()
