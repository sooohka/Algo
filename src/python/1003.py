import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return IC, arr


def fibozero(n, cache):
    if n == 1:
        return 0
    if n == 0:
        return 1
    if cache[n]:
        return cache[n]
    cache[n] = fibozero(n - 1, cache) + fibozero(n - 2, cache)
    return cache[n]


def fiboone(n, cache):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if cache[n]:
        return cache[n]
    cache[n] = fiboone(n - 1, cache) + fiboone(n - 2, cache)
    return cache[n]


def solution():
    IC, arr = getInput()
    cache1 = [0 for _ in range(41)]
    cache2 = [0 for _ in range(41)]
    for a in arr:
        zero = fibozero(a, cache1)
        one = fiboone(a, cache2)
        sys.stdout.write(str(zero) + " " + str(one) + "\n")


solution()
