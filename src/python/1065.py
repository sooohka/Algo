import sys


def solution(N):
    count = 0
    for i in range(1,N+1):
        count = count + 1 if isGood(i) else count
    print(count)


def isGood(i):
    sub = ((i // 10) % 10) - (i % 10)
    while i >= 10:
        if sub != ((i // 10) % 10) - (i % 10):
            return False
        i //= 10
    return True


def main():
    N = int(sys.stdin.readline())
    solution(N)


main()
