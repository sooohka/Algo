import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return arr


def solution():
    arr = getInput()
    for i in arr:
        floor = i[2] % i[0]
        room = 0
        if floor == 0:
            floor = i[0]
            room = -1
        print(floor, end="")
        if i[2] // i[0] < 9:
            print(0, end="")
        room += i[2] // i[0] + 1
        print(room)


solution()
t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    f = 0
    ho = 0
    if n % h == 0:
        f = h * 100
        ho = n // h
    else:
        f = (n % h) * 100
        ho = 1 + n // h
    print(f + ho)